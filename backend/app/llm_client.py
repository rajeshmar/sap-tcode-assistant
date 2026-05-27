from __future__ import annotations


class LLMClientError(RuntimeError):
    pass


MODULE_USAGE_HINTS = {
    "MM": {
        "name": "Materials Management",
        "common_fields": [
            "material number",
            "plant",
            "purchasing organization",
            "vendor",
            "storage location",
        ],
    },
    "IM": {
        "name": "Inventory Management",
        "common_fields": [
            "material number",
            "plant",
            "storage location",
            "batch",
            "movement type",
        ],
    },
    "SD": {
        "name": "Sales and Distribution",
        "common_fields": [
            "sales order number",
            "sales organization",
            "distribution channel",
            "division",
            "customer",
        ],
    },
    "PP": {
        "name": "Production Planning",
        "common_fields": [
            "material number",
            "plant",
            "production order",
            "planned order",
            "BOM",
            "work center",
        ],
    },
    "FI": {
        "name": "Finance",
        "common_fields": [
            "company code",
            "fiscal year",
            "document number",
            "vendor",
            "customer",
            "G/L account",
        ],
    },
    "CO": {
        "name": "Controlling",
        "common_fields": [
            "controlling area",
            "cost center",
            "internal order",
            "profit center",
            "cost element",
        ],
    },
    "WM": {
        "name": "Warehouse Management",
        "common_fields": [
            "warehouse number",
            "storage type",
            "storage bin",
            "material number",
            "transfer order",
        ],
    },
    "PM": {
        "name": "Plant Maintenance",
        "common_fields": [
            "equipment",
            "functional location",
            "maintenance order",
            "notification",
            "plant",
        ],
    },
    "QM": {
        "name": "Quality Management",
        "common_fields": [
            "inspection lot",
            "material number",
            "plant",
            "usage decision",
            "quality notification",
        ],
    },
    "PS": {
        "name": "Project System",
        "common_fields": [
            "project definition",
            "WBS element",
            "network",
            "activity",
            "budget",
        ],
    },
    "HR": {
        "name": "Human Resources",
        "common_fields": [
            "personnel number",
            "organizational unit",
            "position",
            "employee subgroup",
        ],
    },
    "SYS": {
        "name": "System",
        "common_fields": [
            "user",
            "role",
            "authorization object",
            "system client",
        ],
    },
}


ACTION_VERBS = {
    "create": ["create", "new", "add", "make"],
    "change": ["change", "edit", "modify", "update"],
    "display": ["display", "show", "view", "check", "see", "lookup", "look up"],
    "delete": ["delete", "remove"],
    "release": ["release", "approve", "approval"],
    "post": ["post", "posting", "book"],
    "list": ["list", "report", "overview"],
}


SPECIFIC_STEP_HINTS = {
    "MM01": [
        "Enter the material type and industry sector.",
        "Select the required material views.",
        "Enter organizational levels such as plant and storage location.",
        "Maintain the required material master data.",
        "Save the material master record.",
    ],
    "MM02": [
        "Enter the material number.",
        "Select the views you want to change.",
        "Enter organizational levels such as plant and storage location if required.",
        "Update the required fields.",
        "Save the changes.",
    ],
    "MM03": [
        "Enter the material number.",
        "Select the views you want to display.",
        "Enter plant and storage location if required.",
        "Review the material master details.",
        "Exit the transaction when finished.",
    ],
    "MMBE": [
        "Enter the material number.",
        "Enter plant and storage location if required.",
        "Execute the transaction.",
        "Review stock by plant, storage location, batch, and stock type.",
        "Expand the stock tree for more details.",
    ],
    "ME21N": [
        "Enter vendor, purchasing organization, purchasing group, and company code.",
        "Add material, quantity, plant, delivery date, and price.",
        "Check item details, account assignment, and delivery information.",
        "Use Check to validate the document.",
        "Save the purchase order.",
    ],
    "ME22N": [
        "Open the existing purchase order.",
        "Change the required header or item details.",
        "Validate price, quantity, delivery date, and plant.",
        "Use Check to verify the document.",
        "Save the changes.",
    ],
    "ME23N": [
        "Open the purchase order.",
        "Enter or select the purchase order number.",
        "Review header, item, delivery, and history details.",
        "Check document flow or PO history if needed.",
        "Exit the transaction when finished.",
    ],
    "VA01": [
        "Enter order type, sales organization, distribution channel, and division.",
        "Enter sold-to party, ship-to party, material, quantity, and plant.",
        "Check pricing, availability, and delivery details.",
        "Validate the sales order.",
        "Save the sales order.",
    ],
    "VA02": [
        "Enter the sales order number.",
        "Change the required header or item details.",
        "Check pricing, delivery, and availability if relevant.",
        "Validate the sales order.",
        "Save the changes.",
    ],
    "VA03": [
        "Enter the sales order number.",
        "Review header and item details.",
        "Check pricing, delivery status, and document flow if needed.",
        "Review schedule lines and partner details if required.",
        "Exit the transaction when finished.",
    ],
    "CO01": [
        "Enter material number, plant, and order type.",
        "Enter quantity, basic dates, and scheduling details.",
        "Review BOM components and routing operations if available.",
        "Release the order if your process requires it.",
        "Save the production order.",
    ],
    "CO02": [
        "Enter the production order number.",
        "Change quantity, dates, components, operations, or status as required.",
        "Check material availability and scheduling if needed.",
        "Validate the changes.",
        "Save the production order.",
    ],
    "CO03": [
        "Enter the production order number.",
        "Review order header, components, operations, and status.",
        "Check confirmations, goods movements, and costs if required.",
        "Review document flow or logs if needed.",
        "Exit the transaction when finished.",
    ],
    "MD01": [
        "Enter plant and planning parameters.",
        "Choose the MRP processing scope.",
        "Execute the MRP run.",
        "Review planning results after completion.",
        "Check generated planned orders or purchase requisitions.",
    ],
    "MD04": [
        "Enter material number and plant.",
        "Execute the transaction.",
        "Review stock, requirements, planned orders, purchase orders, and reservations.",
        "Identify shortages or excess supply.",
        "Open related documents if further analysis is needed.",
    ],
    "CS01": [
        "Enter material, plant, BOM usage, and valid-from date.",
        "Add BOM components and quantities.",
        "Maintain item category and component details.",
        "Validate the BOM structure.",
        "Save the BOM.",
    ],
    "CS02": [
        "Enter material, plant, BOM usage, and valid-from date.",
        "Change components, quantities, or item details.",
        "Validate the BOM changes.",
        "Check consistency if needed.",
        "Save the BOM.",
    ],
    "CS03": [
        "Enter material, plant, BOM usage, and valid-from date.",
        "Display the BOM structure.",
        "Review components, quantities, and item categories.",
        "Check validity and alternative BOM if needed.",
        "Exit the transaction when finished.",
    ],
}


async def generate_tcode_explanation(query: str, results: list[dict]) -> str:
    """
    Local RAG-style explanation generator.

    Flow:
    1. search.py retrieves the most relevant SAP T-Code records from sap_tcodes.json.
    2. This function uses the retrieved records as context.
    3. It generates a deterministic explanation without OpenRouter or any external API.

    This is fast, free, and reliable for your current SAP T-Code assistant.
    """
    if not results:
        return "No matching SAP T-Code found. Try using a more specific business process."

    best = results[0]
    alternatives = results[1:4]

    return build_answer(query=query, best=best, alternatives=alternatives)


def build_answer(query: str, best: dict, alternatives: list[dict]) -> str:
    tcode = clean_value(best.get("tcode"))
    description = clean_value(best.get("description"))
    module = clean_value(best.get("module"))
    module_name = clean_value(best.get("module_name"))
    score = round(float(best.get("score", 0)))

    detected_action = detect_action(query=query, description=description)
    confidence_label = get_confidence_label(score)

    lines = [
        f"Recommended T-Code: {tcode}",
        f"Module: {module_name}",
        f"Purpose: {description}",
        f"Confidence: {confidence_label} ({score}%)",
        "",
        "Why this code:",
        build_reason(query=query, tcode=tcode, description=description, module_name=module_name, action=detected_action),
        "",
        "How to use in SAP:",
    ]

    steps = build_usage_steps(tcode=tcode, description=description, module=module, action=detected_action)

    for index, step in enumerate(steps, start=1):
        lines.append(f"{index}. {step}")

    required_fields = get_required_fields(module=module, tcode=tcode)

    if required_fields:
        lines.extend(
            [
                "",
                "Typical fields you may need:",
            ]
        )
        for field in required_fields:
            lines.append(f"- {field}")

    if alternatives:
        lines.extend(
            [
                "",
                "Related T-Codes:",
            ]
        )

        for item in alternatives:
            alt_tcode = clean_value(item.get("tcode"))
            alt_description = clean_value(item.get("description"))
            alt_module_name = clean_value(item.get("module_name"))
            alt_score = round(float(item.get("score", 0)))
            lines.append(
                f"- {alt_tcode}: {alt_description} ({alt_module_name}, match {alt_score}%)"
            )

    lines.extend(
        [
            "",
            "Note:",
            "Use this T-Code only if you have the required SAP authorization. Field names and screens may vary based on your company configuration.",
        ]
    )

    return "\n".join(lines)


def build_reason(
    query: str,
    tcode: str,
    description: str,
    module_name: str,
    action: str,
) -> str:
    query_clean = query.strip()

    if action == "display":
        action_text = "view or check existing information"
    elif action == "create":
        action_text = "create a new business document or master data record"
    elif action == "change":
        action_text = "modify an existing business document or master data record"
    elif action == "delete":
        action_text = "remove or mark data for deletion"
    elif action == "release":
        action_text = "approve or release a business document"
    elif action == "post":
        action_text = "post a transaction into SAP"
    elif action == "list":
        action_text = "review a list, report, or overview"
    else:
        action_text = "perform the requested SAP business activity"

    return (
        f'You asked: "{query_clean}". '
        f"{tcode} is the best match because it is used for '{description}' "
        f"in the {module_name} area. This fits your need to {action_text}."
    )


def build_usage_steps(
    tcode: str,
    description: str,
    module: str,
    action: str,
) -> list[str]:
    if tcode in SPECIFIC_STEP_HINTS:
        return [
            "Open SAP Easy Access.",
            f"Enter {tcode} in the SAP command field.",
            "Press Enter.",
            *SPECIFIC_STEP_HINTS[tcode],
        ]

    generic_steps = [
        "Open SAP Easy Access.",
        f"Enter {tcode} in the SAP command field.",
        "Press Enter.",
    ]

    if action == "create":
        generic_steps.extend(
            [
                "Enter the required organizational and business data.",
                "Complete all mandatory fields shown by SAP.",
                "Check the document or master data for errors.",
                "Save the record.",
            ]
        )
    elif action == "change":
        generic_steps.extend(
            [
                "Enter the existing document number or master data key.",
                "Update the required fields.",
                "Review the changes carefully.",
                "Save the changes.",
            ]
        )
    elif action == "display":
        generic_steps.extend(
            [
                "Enter the document number, material, customer, vendor, plant, or other required key.",
                "Execute or press Enter.",
                "Review the displayed information.",
                "Exit the transaction when finished.",
            ]
        )
    elif action == "release":
        generic_steps.extend(
            [
                "Enter the document or object selection criteria.",
                "Review the item that needs approval or release.",
                "Confirm the release action if it is correct.",
                "Save or execute the release.",
            ]
        )
    elif action == "post":
        generic_steps.extend(
            [
                "Enter the required posting data.",
                "Review company code, posting date, document date, and line items.",
                "Check the document for errors.",
                "Post or save the transaction.",
            ]
        )
    else:
        generic_steps.extend(
            [
                "Enter the required selection values.",
                "Execute the transaction.",
                "Review the result screen.",
                "Open related documents if further analysis is needed.",
            ]
        )

    return generic_steps


def get_required_fields(module: str, tcode: str) -> list[str]:
    if tcode in {"MM01", "MM02", "MM03", "MM60"}:
        return ["material number", "plant", "storage location", "material view"]

    if tcode in {"MMBE", "MB52", "MB51", "MD04"}:
        return ["material number", "plant", "storage location", "batch"]

    if tcode in {"ME21N", "ME22N", "ME23N"}:
        return ["purchase order number", "vendor", "purchasing organization", "plant"]

    if tcode in {"ME51N", "ME52N", "ME53N"}:
        return ["purchase requisition number", "material number", "plant", "quantity"]

    if tcode in {"VA01", "VA02", "VA03"}:
        return ["sales order number", "customer", "sales organization", "distribution channel"]

    if tcode in {"CO01", "CO02", "CO03"}:
        return ["production order number", "material number", "plant", "order type"]

    if tcode in {"CS01", "CS02", "CS03"}:
        return ["material number", "plant", "BOM usage", "valid-from date"]

    if tcode in {"MD01", "MD02", "MD03"}:
        return ["plant", "material number", "MRP controller", "planning parameters"]

    if tcode in {"FB03", "FB60", "FB70", "FBL1N", "FBL3N", "FBL5N"}:
        return ["company code", "document number", "fiscal year", "posting date"]

    module_config = MODULE_USAGE_HINTS.get(module)
    if not module_config:
        return []

    return module_config["common_fields"]


def detect_action(query: str, description: str) -> str:
    text = f"{query} {description}".lower()

    for action, keywords in ACTION_VERBS.items():
        if any(keyword in text for keyword in keywords):
            return action

    description_clean = description.lower()

    if description_clean.startswith("create"):
        return "create"

    if description_clean.startswith("change"):
        return "change"

    if description_clean.startswith("display"):
        return "display"

    if description_clean.startswith("release"):
        return "release"

    if description_clean.startswith("post"):
        return "post"

    if "list" in description_clean or "overview" in description_clean or "report" in description_clean:
        return "list"

    return "general"


def get_confidence_label(score: int) -> str:
    if score >= 90:
        return "High"
    if score >= 70:
        return "Medium"
    return "Low"


def clean_value(value: object) -> str:
    if value is None:
        return ""

    return str(value).strip()