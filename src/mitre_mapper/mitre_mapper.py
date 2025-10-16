#!/usr/bin/env python3
"""
Map Indicators of Compromise (IOCs) to MITRE ATT&CK Techniques.
"""

import pandas as pd
import argparse

MAPPING = {
    'powershell': 'T1059',
    'rundll32': 'T1218',
    'wmic': 'T1047',
    'unauthorized_file_access': 'T1005'
}

def map_iocs(ioc_csv, output_csv=None):
    df = pd.read_csv(ioc_csv)
    df['MITRE_Technique'] = df['Indicator'].apply(
        lambda x: next((t for k,t in MAPPING.items() if k in x.lower()), 'T1055')
    )

    print(df[['Indicator', 'MITRE_Technique']])
    if output_csv:
        df.to_csv(output_csv, index=False)
        print(f"Mapped results saved to {output_csv}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Map IOCs to MITRE techniques")
    parser.add_argument('ioc_csv', help='Path to input CSV of IOCs')
    parser.add_argument('--output', help='Optional path to save mapped CSV')
    args = parser.parse_args()
    map_iocs(args.ioc_csv, args.output)
