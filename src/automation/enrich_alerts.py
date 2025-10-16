#!/usr/bin/env python3
"""
Enrich alert CSV with additional context (e.g., geolocation, threat score).
"""

import pandas as pd
import argparse

def enrich_alerts(input_csv, output_csv):
    df = pd.read_csv(input_csv)
    # Example enrichment: add a fake threat_score column
    df['threat_score'] = df['AlertName'].apply(lambda x: len(x) % 100)
    df.to_csv(output_csv, index=False)
    print(f"Enriched alerts saved to {output_csv}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Enrich alerts CSV")
    parser.add_argument('--input', required=True, help='Path to input alerts CSV')
    parser.add_argument('--output', required=True, help='Path to save enriched alerts CSV')
    args = parser.parse_args()
    enrich_alerts(args.input, args.output)
