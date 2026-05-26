import json
from pathlib import Path


DATA_PATH = Path(__file__).resolve().parents[1] / "data" / "sap_tcodes.json"


def load_tcodes() -> list[dict]:
    if not DATA_PATH.exists():
        raise FileNotFoundError(
            f"{DATA_PATH} not found. Run scripts/convert_md_to_json.py first."
        )

    with DATA_PATH.open("r", encoding="utf-8") as file:
        data = json.load(file)

    if not isinstance(data, list):
        raise ValueError("sap_tcodes.json must contain a list of records.")

    required_fields = {"tcode", "description", "module", "module_name"}

    for index, row in enumerate(data):
        missing_fields = required_fields - set(row)
        if missing_fields:
            raise ValueError(
                f"Record at index {index} is missing fields: {missing_fields}"
            )

    return data