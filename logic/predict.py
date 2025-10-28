# logic/predict.py

import json
from typing import Dict
from dash import html
from db.db_utils import insert_input

# Known SNP risk associations (based on scientific literature)
SNP_RISK_MAPPING = {
    "rs429358": {
        "risk": "High",
        "disease": "Alzheimer's Disease",
        "description": "APOE4 variant - associated with increased risk of Alzheimer's"
    },
    "rs7412": {
        "risk": "Moderate",
        "disease": "Alzheimer's Disease",
        "description": "APOE2 variant - may provide some protection against Alzheimer's"
    },
    "rs6265": {
        "risk": "Moderate",
        "disease": "Parkinson's Disease",
        "description": "BDNF variant - linked to cognitive decline"
    },
    "rs356219": {
        "risk": "High",
        "disease": "Parkinson's Disease",
        "description": "SNCA variant - associated with increased PD risk"
    },
    "rs3764650": {
        "risk": "Moderate",
        "disease": "Alzheimer's Disease",
        "description": "ABCA7 variant - linked to late-onset Alzheimer's"
    }
}

def run_prediction(snp_input: str) -> Dict:
    if not snp_input:
        return {}

    snps = [s.strip().lower() for s in snp_input.split(",")]
    results = {}

    # ✅ Build the results first
    for snp in snps:
        if snp in SNP_RISK_MAPPING:
            info = SNP_RISK_MAPPING[snp]
            if info["disease"] not in results:
                results[info["disease"]] = {
                    "risk_level": info["risk"],
                    "details": [f"{snp}: {info['description']}"]
                }
            else:
                results[info["disease"]]["details"].append(
                    f"{snp}: {info['description']}"
                )

    if not results:
        results = {
            "Unknown": {
                "risk_level": "Unknown",
                "details": ["No known risk associations for provided SNPs"]
            }
        }

    # ✅ Now save the input and result after building it
    insert_input(snp_input, results, username="test_user")

    return results


def format_results_table(results: Dict):
    rows = []
    for disease, info in results.items():
        risk_color = {
            "High": "#ff4d4d",
            "Moderate": "#ffa64d",
            "Low": "#4dff4d",
            "Unknown": "#808080"
        }.get(info["risk_level"], "#808080")

        details = html.Ul([
            html.Li(detail) for detail in info["details"]
        ])

        rows.append(html.Div(className='result-row', children=[
            html.H4(disease),
            html.Div(className='risk-badge',
                     style={'backgroundColor': risk_color},
                     children=f"Risk Level: {info['risk_level']}"),
            html.Div(className='risk-details', children=details)
        ]))

    return html.Div([
        html.H3("Prediction Results:"),
        html.Div(className='results-container', children=rows)
    ])
