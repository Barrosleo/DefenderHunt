#!/usr/bin/env python3
"""
Run a KQL query against Defender or Sentinel (simulated).
"""

import argparse
import os

def run_query(query_path):
    if not os.path.isfile(query_path):
        print(f"Query file not found: {query_path}")
        return

    with open(query_path, 'r') as f:
        query = f.read()

    print(f"Executing KQL Query from {query_path}:\n{query}\n")
    # TODO: Integrate with Defender/Sentinel API
    print("Query executed successfully. Results written to results.csv")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run KQL threat hunting queries")
    parser.add_argument('--query', required=True, help='Path to the .kql file')
    args = parser.parse_args()
    run_query(args.query)
