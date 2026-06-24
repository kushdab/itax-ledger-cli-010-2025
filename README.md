# itax-ledger-cli-010-2025

A lightweight CLI tool for Kenyan freelancers to estimate their annual tax obligations for the 2024/2025 financial year.

## Features
- Calculates PAYE based on the latest 5-tier KRA individual tax rates (10% to 35%).
- Automatically applies the KES 28,800 annual personal relief.
- Optional VAT calculation for inclusive amounts.
- Deducts business expenses to determine taxable income.

## Usage
Run the script using Python 3:

```bash
# Calculate basic PAYE on 1.2M annual income
python cli.py --income 1200000

# Calculate tax with 200k expenses and VAT details
python cli.py --income 6000000 --expenses 200000 --vat
```

## Parameters
- `--income`: Total annual gross earnings in KES (Required).
- `--expenses`: Total business-related deductible expenses (Default: 0).
- `--vat`: Flag to display the 16% VAT portion within the gross income.