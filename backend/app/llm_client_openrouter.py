import os

import httpx
from dotenv import load_dotenv

load_dotenv()


OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENROUTER_MODEL = os.getenv(
    "OPENROUTER_MODEL",
    "deepseek/deepseek-chat-v3-0324:free",
)

print("OpenRouter model:", OPENROUTER_MODEL)
print("OpenRouter key loaded:", bool(OPENROUTER_API_KEY))


class LLMClientError(RuntimeError):
    pass


async def generate_tcode_explanation(query: str, results: list[dict]) -> str:
    if not results:
        return "No matching SAP T-Code found."

    if not OPENROUTER_API_KEY:
        return generate_fallback_explanation(query, results)

    context = build_context(results)

    system_prompt = """
You are an SAP S/4HANA transaction code assistant.

Rules:
- Use only the SAP T-Codes provided in the candidate list.
- Do not invent SAP transaction codes.
- Recommend the best matching T-Code first.
- Explain in simple, practical steps for a SAP beginner.
- Keep the answer clear, concise, and business-focused.
- If related alternatives exist, list them briefly.
- Do not mention backend, candidate records, JSON, API, or model internals.
"""

    user_prompt = f"""
User need:
{query}

Candidate SAP T-Codes:
{context}

Return the answer in this exact structure:

Recommended T-Code:
Module:
Purpose:

Why this code:

How to use in SAP:
1.
2.
3.
4.
5.

Related T-Codes:
-
"""

    payload = {
        "model": OPENROUTER_MODEL,
        "messages": [
            {"role": "system", "content": system_prompt.strip()},
            {"role": "user", "content": user_prompt.strip()},
        ],
        "temperature": 0.2,
        "max_tokens": 700,
    }

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "http://localhost:5173",
        "X-Title": "SAP T-Code Assistant",
    }

    try:
        async with httpx.AsyncClient(timeout=40) as client:
            response = await client.post(
                "https://openrouter.ai/api/v1/chat/completions",
                headers=headers,
                json=payload,
            )
    except httpx.TimeoutException as error:
        raise LLMClientError("OpenRouter request timed out.") from error
    except httpx.HTTPError as error:
        raise LLMClientError(f"OpenRouter connection failed: {error}") from error

    if response.status_code >= 400:
        raise LLMClientError(
            f"OpenRouter request failed: {response.status_code} {response.text}"
        )

    data = response.json()

    try:
        return data["choices"][0]["message"]["content"].strip()
    except (KeyError, IndexError, TypeError) as error:
        raise LLMClientError("OpenRouter returned an unexpected response format.") from error


def build_context(results: list[dict]) -> str:
    lines = []

    for index, row in enumerate(results, start=1):
        lines.append(
            f"{index}. T-Code: {row['tcode']} | "
            f"Description: {row['description']} | "
            f"Module: {row['module_name']} ({row['module']}) | "
            f"Score: {round(row['score'], 2)}"
        )

    return "\n".join(lines)


def generate_fallback_explanation(query: str, results: list[dict]) -> str:
    best = results[0]
    alternatives = results[1:4]

    lines = [
        f"Recommended T-Code: {best['tcode']}",
        f"Module: {best['module_name']}",
        f"Purpose: {best['description']}",
        "",
        "Why this code:",
        (
            f"The user asked: '{query}'. "
            f"The closest matching SAP transaction is {best['tcode']} "
            f"because it is used for: {best['description']}."
        ),
        "",
        "How to use in SAP:",
        "1. Open SAP Easy Access.",
        f"2. Enter {best['tcode']} in the command field.",
        "3. Press Enter.",
        "4. Fill in the required fields shown on the SAP screen.",
        "5. Execute, display, change, or save based on your business process.",
    ]

    if alternatives:
        lines.extend(["", "Related T-Codes:"])
        for item in alternatives:
            lines.append(
                f"- {item['tcode']}: {item['description']} ({item['module_name']})"
            )

    return "\n".join(lines)