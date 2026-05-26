from pathlib import Path
import json
import re

MODULE_MAP = {
    "FI": "Finance",
    "CO": "Controlling",
    "IM": "Inventory Management",
    "MM": "Materials Management",
    "WM": "Warehouse Management",
    "PM": "Plant Maintenance",
    "PP": "Production Planning",
    "PS": "Project System",
    "QM": "Quality Management",
    "SD": "Sales and Distribution",
    "HR": "Human Resources",
    "SYS": "System",
}

ROOT = Path(__file__).resolve().parents[1]
MD_PATH = ROOT / "data" / "SAP_S4_HANA_T_Code.md"
JSON_PATH = ROOT / "data" / "sap_tcodes.json"


def parse_tcodes(markdown_text: str) -> list[dict]:
    records: list[dict] = []

    # Matches rows like:
    # | MM03 | Display Material | MM |
    pattern = re.compile(
        r"^\|\s*([A-Z0-9./_\-=]+)\s*\|\s*(.*?)\s*\|\s*([A-Z]{2,3})\s*\|$",
        re.MULTILINE,
    )

    for match in pattern.finditer(markdown_text):
        tcode = match.group(1).strip()
        description = re.sub(r"\s+", " ", match.group(2).strip())
        module = match.group(3).strip()

        if tcode.lower() == "t-code":
            continue

        records.append(
            {
                "tcode": tcode,
                "description": description,
                "module": module,
                "module_name": MODULE_MAP.get(module, module),
            }
        )

    # Remove duplicates
    unique = {}
    for row in records:
        key = (row["tcode"], row["description"], row["module"])
        unique[key] = row

    return sorted(unique.values(), key=lambda x: (x["module"], x["tcode"]))


def main() -> None:
    markdown_text = MD_PATH.read_text(encoding="utf-8")
    records = parse_tcodes(markdown_text)

    if not records:
        raise ValueError("No SAP T-Code records found. Check Markdown table format.")

    JSON_PATH.write_text(json.dumps(records, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Created {JSON_PATH} with {len(records)} records.")


if __name__ == "__main__":
    main()