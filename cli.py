import sys
import argparse

# KRA Tax Brackets 2024/2025 (Annual)
TAX_BRACKETS = [
    (288000, 0.10),    # First 288,000
    (100000, 0.25),    # Next 100,000
    (5612000, 0.30),   # Next 5,612,000
    (3600000, 0.325),  # Next 3,600,000
    (float('inf'), 0.35) # Above 9,600,000
]
ANNUAL_PERSONAL_RELIEF = 28800.0
VAT_RATE = 0.16

def calculate_paye(annual_taxable_pay):
    """Calculates annual PAYE based on KRA tiers and deducts personal relief."""
    tax = 0.0
    remaining_income = annual_taxable_pay

    for limit, rate in TAX_BRACKETS:
        if remaining_income <= 0:
            break
        taxable_at_this_rate = min(remaining_income, limit)
        tax += taxable_at_this_rate * rate
        remaining_income -= taxable_at_this_rate

    # Apply personal relief
    final_tax = max(0, tax - ANNUAL_PERSONAL_RELIEF)
    return final_tax, tax

def calculate_vat(sales_amount, inclusive=True):
    """Calculates VAT portion from gross sales (inclusive) or adds to net (exclusive)."""
    if inclusive:
        vat_amount = sales_amount - (sales_amount / (1 + VAT_RATE))
        net_amount = sales_amount - vat_amount
    else:
        vat_amount = sales_amount * VAT_RATE
        net_amount = sales_amount
    return vat_amount, net_amount

def main():
    parser = argparse.ArgumentParser(
        description="iTax Ledger CLI - Kenyan Freelancer Tax Calculator (2025)"
    )
    parser.add_argument("--income", type=float, help="Total annual gross income (KES)", required=True)
    parser.add_argument("--expenses", type=float, default=0.0, help="Total deductible business expenses (KES)")
    parser.add_argument("--vat", action="store_true", help="Calculate VAT obligation (assumes income is VAT inclusive)")
    
    args = parser.parse_args()

    gross_income = args.income
    expenses = args.expenses
    taxable_income = max(0, gross_income - expenses)

    print("=" * 45)
    print(f"iTax Ledger Report - FY 2024/2025")
    print("=" * 45)
    print(f"Gross Annual Income:    KES {gross_income:12,.2f}")
    print(f"Business Expenses:      KES {expenses:12,.2f}")
    print(f"Taxable Income:         KES {taxable_income:12,.2f}")
    print("-" * 45)

    # PAYE Calculation
    paye_due, gross_tax = calculate_paye(taxable_income)
    print(f"Gross Tax Charged:      KES {gross_tax:12,.2f}")
    print(f"Personal Relief:      - KES {ANNUAL_PERSONAL_RELIEF:12,.2f}")
    print(f"Net PAYE Payable:       KES {paye_due:12,.2f}")
    
    # VAT Calculation
    if args.vat:
        vat_due, _ = calculate_vat(gross_income, inclusive=True)
        print("-" * 45)
        print(f"VAT Component (16%):    KES {vat_due:12,.2f}")
        print("(Note: VAT applies if annual turnover > 5M KES)")

    print("=" * 45)
    print(f"Estimated Take-home:    KES {(taxable_income - paye_due):12,.2f}")
    print("=" * 45)
    print("Disclaimer: Use for estimation only. Consult a KRA professional.")

if __name__ == "__main__":
    main()