from rapidfuzz import fuzz


ACTION_WORDS = {
    "display": ["display", "show", "view", "check", "see", "lookup", "look up"],
    "create": ["create", "make", "add", "new"],
    "change": ["change", "edit", "modify", "update"],
    "delete": ["delete", "remove"],
}


KNOWN_INTENTS = [
    # Material Master
    {
        "keywords": [
            "check material",
            "display material",
            "view material",
            "show material",
            "material details",
            "material master display",
        ],
        "preferred_tcodes": {"MM03": 60},
    },
    {
        "keywords": ["create material", "new material", "add material", "material creation"],
        "preferred_tcodes": {"MM01": 60},
    },
    {
        "keywords": ["change material", "edit material", "update material", "material change"],
        "preferred_tcodes": {"MM02": 60},
    },
    {
        "keywords": ["material list", "list materials"],
        "preferred_tcodes": {"MM60": 60},
    },

    # Stock / Inventory
    {
        "keywords": [
            "stock overview",
            "check stock",
            "display stock",
            "view stock",
            "material stock",
            "available stock",
            "stock details",
        ],
        "preferred_tcodes": {"MMBE": 70, "MB52": 35, "MB51": 20, "MD04": 15},
    },

    # Purchasing
    {
        "keywords": ["create purchase order", "make purchase order", "new po", "create po"],
        "preferred_tcodes": {"ME21N": 70},
    },
    {
        "keywords": ["change purchase order", "edit purchase order", "change po"],
        "preferred_tcodes": {"ME22N": 70},
    },
    {
        "keywords": ["display purchase order", "check purchase order", "view po", "display po"],
        "preferred_tcodes": {"ME23N": 70},
    },
    {
        "keywords": ["create purchase requisition", "new purchase requisition", "create pr"],
        "preferred_tcodes": {"ME51N": 70},
    },
    {
        "keywords": ["change purchase requisition", "edit purchase requisition", "change pr"],
        "preferred_tcodes": {"ME52N": 70},
    },
    {
        "keywords": ["display purchase requisition", "view purchase requisition", "display pr"],
        "preferred_tcodes": {"ME53N": 70},
    },

    # Sales
    {
        "keywords": ["create sales order", "new sales order"],
        "preferred_tcodes": {"VA01": 70},
    },
    {
        "keywords": ["change sales order", "edit sales order"],
        "preferred_tcodes": {"VA02": 70},
    },
    {
        "keywords": ["display sales order", "check sales order", "view sales order"],
        "preferred_tcodes": {"VA03": 70},
    },

    # Production Planning
    {
        "keywords": ["production planning", "pp module", "production module"],
        "preferred_tcodes": {
            "CO01": 45,
            "CO02": 35,
            "CO03": 40,
            "MD01": 40,
            "MD04": 35,
            "CS01": 25,
            "CS02": 25,
            "CS03": 30,
        },
    },
    {
        "keywords": ["create production order", "new production order", "production order create"],
        "preferred_tcodes": {"CO01": 90},
    },
    {
        "keywords": ["change production order", "edit production order", "production order change"],
        "preferred_tcodes": {"CO02": 90},
    },
    {
        "keywords": [
            "display production order",
            "view production order",
            "check production order",
            "production order display",
        ],
        "preferred_tcodes": {"CO03": 90},
    },
    {
        "keywords": ["mrp run", "run mrp", "material requirements planning", "total planning"],
        "preferred_tcodes": {"MD01": 90, "MD02": 45, "MD03": 40},
    },
    {
        "keywords": ["stock requirements list", "stock requirement list", "md04", "requirements list"],
        "preferred_tcodes": {"MD04": 90},
    },
    {
        "keywords": ["create planned order", "new planned order"],
        "preferred_tcodes": {"MD11": 80},
    },
    {
        "keywords": ["change planned order", "edit planned order"],
        "preferred_tcodes": {"MD12": 80},
    },
    {
        "keywords": ["display planned order", "view planned order", "check planned order"],
        "preferred_tcodes": {"MD13": 80},
    },
    {
        "keywords": ["create bom", "create bill of material"],
        "preferred_tcodes": {"CS01": 80},
    },
    {
        "keywords": ["change bom", "edit bom", "change bill of material"],
        "preferred_tcodes": {"CS02": 80},
    },
    {
        "keywords": ["display bom", "view bom", "display bill of material"],
        "preferred_tcodes": {"CS03": 80},
    },
    {
        "keywords": ["create routing", "new routing"],
        "preferred_tcodes": {"CA01": 80},
    },
    {
        "keywords": ["change routing", "edit routing"],
        "preferred_tcodes": {"CA02": 80},
    },
    {
        "keywords": ["display routing", "view routing"],
        "preferred_tcodes": {"CA03": 80},
    },

    # Finance
    {
        "keywords": ["display accounting document", "view accounting document", "check accounting document"],
        "preferred_tcodes": {"FB03": 80},
    },
    {
        "keywords": ["post vendor invoice", "enter vendor invoice", "create vendor invoice"],
        "preferred_tcodes": {"FB60": 80},
    },
    {
        "keywords": ["display vendor balance", "vendor balance"],
        "preferred_tcodes": {"FK10N": 70},
    },
    {
        "keywords": ["display customer balance", "customer balance"],
        "preferred_tcodes": {"FD10N": 70},
    },

    # Quality Management
    {
        "keywords": ["display inspection lot", "check inspection lot", "inspection lot"],
        "preferred_tcodes": {"QA03": 80, "QA32": 45, "QA33": 45},
    },
    {
        "keywords": ["record usage decision", "usage decision"],
        "preferred_tcodes": {"QA11": 80},
    },

    # Plant Maintenance
    {
        "keywords": ["create maintenance order", "new maintenance order"],
        "preferred_tcodes": {"IW31": 80},
    },
    {
        "keywords": ["change maintenance order", "edit maintenance order"],
        "preferred_tcodes": {"IW32": 80},
    },
    {
        "keywords": ["display maintenance order", "view maintenance order"],
        "preferred_tcodes": {"IW33": 80},
    },
    {
        "keywords": ["display equipment", "view equipment", "check equipment"],
        "preferred_tcodes": {"IE03": 80},
    },
]


MODULE_CODE_BOOSTS = {
    "finance": "FI",
    "controlling": "CO",
    "inventory management": "IM",
    "materials management": "MM",
    "material management": "MM",
    "warehouse management": "WM",
    "plant maintenance": "PM",
    "production planning": "PP",
    "project system": "PS",
    "quality management": "QM",
    "sales and distribution": "SD",
    "human resources": "HR",
    "system": "SYS",
}


def search_tcodes(
    query: str,
    records: list[dict],
    module: str | None = None,
    top_k: int = 5,
) -> list[dict]:
    query_clean = query.lower().strip()

    if not query_clean:
        return []

    filtered_records = records

    if module:
        filtered_records = [
            row
            for row in records
            if row["module"].lower() == module.lower()
            or row["module_name"].lower() == module.lower()
        ]

    scored_results: list[dict] = []

    for row in filtered_records:
        score = calculate_score(query_clean, row)

        if score <= 25:
            continue

        scored_results.append(
            {
                **row,
                "score": min(float(score), 100.0),
            }
        )

    scored_results.sort(
        key=lambda item: (
            item["score"],
            module_priority(query_clean, item),
            exact_action_priority(query_clean, item),
        ),
        reverse=True,
    )

    return scored_results[:top_k]


def calculate_score(query: str, row: dict) -> float:
    tcode = row["tcode"]
    description = row["description"].lower()
    module = row["module"]
    module_lower = module.lower()
    module_name = row["module_name"].lower()

    searchable_text = f"{tcode} {description} {module_lower} {module_name}".lower()

    score = max(
        fuzz.partial_ratio(query, searchable_text),
        fuzz.token_set_ratio(query, searchable_text),
    )

    # Direct T-Code search should always win.
    if query.upper() == tcode:
        score += 100

    if query.upper() in tcode:
        score += 45

    # Strong business-intent boosting.
    matched_known_intent = False

    for intent in KNOWN_INTENTS:
        if any(keyword in query for keyword in intent["keywords"]):
            matched_known_intent = True

            if tcode in intent["preferred_tcodes"]:
                score += intent["preferred_tcodes"][tcode]
            else:
                score -= 35

    # Module phrase boost.
    for module_phrase, module_code in MODULE_CODE_BOOSTS.items():
        if module_phrase in query and module == module_code:
            score += 20

    # Match action words against SAP description.
    if has_action(query, "display") and description.startswith("display"):
        score += 15

    if has_action(query, "create") and description.startswith("create"):
        score += 15

    if has_action(query, "change") and description.startswith("change"):
        score += 15

    if has_action(query, "delete") and description.startswith("delete"):
        score += 15

    # Important SAP-specific corrections.
    score = apply_penalties(query, row, score, matched_known_intent)

    return max(score, 0)


def apply_penalties(
    query: str,
    row: dict,
    score: float,
    matched_known_intent: bool,
) -> float:
    tcode = row["tcode"]
    description = row["description"].lower()
    module = row["module"]

    # If user asks for PP production order, prefer CO01/CO02/CO03 over CO module KKF* orders.
    if "production order" in query and module != "PP":
        score -= 60

    if "create production order" in query and tcode != "CO01":
        score -= 50

    if "change production order" in query and tcode != "CO02":
        score -= 50

    if "display production order" in query and tcode != "CO03":
        score -= 50

    # Penalize irrelevant material group hits when user asks for material master.
    if "material" in query and "material group" in description:
        score -= 35

    if "check material" in query and not description.startswith("display material"):
        score -= 30

    if "create material" in query and not description.startswith("create material"):
        score -= 30

    if "change material" in query and not description.startswith("change material"):
        score -= 30

    # If a known intent matched, reduce unrelated modules unless they are preferred.
    if matched_known_intent:
        if "purchase order" in query and module != "MM":
            score -= 25

        if "sales order" in query and module != "SD":
            score -= 25

        if "stock" in query and module not in {"IM", "MM", "WM", "PP"}:
            score -= 25

    return score


def module_priority(query: str, row: dict) -> int:
    module = row["module"]

    if "production order" in query and module == "PP":
        return 100

    if "purchase order" in query and module == "MM":
        return 100

    if "sales order" in query and module == "SD":
        return 100

    if "material" in query and module == "MM":
        return 90

    if "stock" in query and module in {"IM", "MM", "WM"}:
        return 90

    return 0


def exact_action_priority(query: str, row: dict) -> int:
    description = row["description"].lower()

    if "create" in query and description.startswith("create"):
        return 50

    if "change" in query and description.startswith("change"):
        return 50

    if "display" in query and description.startswith("display"):
        return 50

    if "check" in query and description.startswith("display"):
        return 40

    return 0


def has_action(query: str, action: str) -> bool:
    return any(word in query for word in ACTION_WORDS[action])