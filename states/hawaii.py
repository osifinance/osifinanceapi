def add_doc(value):
    import os
    def _doc(func):
        func.__doc__ = os.path.basename(__file__).title() + value
        return func
    return _doc

doc_income = '''
    Income Taxes
    Sources - https://tax.hawaii.gov/forms/d_18table-on/ (Page Last Updated: December 19, 2022)
              https://files.hawaii.gov/tax/forms/2018/18table-on.pdf (P. 14)
    Summary - Single Taxpayers and Married Filing Seperate Returns
              If taxable income is:                   Your tax is:
              Not over $2,400                         1.40% of taxable income
              Over $2,400 but not over $4,800         $34 plus 3.20% over $2,400
              Over $4,800 but not over $9,600         $110 plus 5.50% over $4,800
              Over $9,600 but not over $14,400        $374 plus 6.40% over $9,600
              Over $14,400 but not over $19,200       $682 plus 6.80% over $14,400
              Over $19,200 but not over $24,000       $1,030 plus 7.20% over $19,200
              Over $24,000 but not over $36,000       $1,354 plus 7.60% over $24,000
              Over $36,000 but not over $48,000       $2,266 plus 7.90% over $36,000
              Over $48,000 but not over $150,000      $3,214 plus 8.25% over $48,000
              Over $150,000 but not over $175,000     $11,629 plus 9.00% over $150,000
              Over $175,000 but not over $200,000     $13,879 plus 10.00% over $175,000
              Over $200,000                           $16,379 plus 11.00% over $200,000 
  
              Married Taxpayers Filing Joint Returns and Certain Widows and Widowers
              If taxable income is:                   Your tax is:
              Not over $4,800                         1.40% of taxable income
              Over $4,800 but not over $9,600         $67 plus 3.20% over $4,800
              Over $9,600 but not over $19,200        $221 plus 5.50% over $9,600
              Over $19,200 but not over $28,800       $749 plus 6.40% over $19,200
              Over $28,800 but not over $38,400       $1,363 plus 6.80% over $28,800
              Over $38,400 but not over $48,000       $2,016 plus 7.20% over $38,400
              Over $48,000 but not over $72,000       $2,707 plus 7.60% over $48,000
              Over $72,000 but not over $96,000       $4,531 plus 7.90% over $72,000
              Over $96,000 but not over $300,000      $6,427 plus 8.25% over $96,000
              Over $300,000 but not over $350,000     $23,257 plus 9.00% over $300,000
              Over $350,000 but not over $400,000     $27,757 plus 10.00% over $350,000
              Over $400,000                           $32,757 plus 11.00% over $400,000
                  
              Unmarried Heads Of Households
              If taxable income is:                   Your tax is:
              Not over $3,600                         1.40% of taxable income
              Over $3,600 but not over $7,200         $50 plus 3.20% over $3,600
              Over $7,200 but not over $14,400        $166 plus 5.50% over $7,200
              Over $14,400 but not over $21,600       $562 plus 6.40% over $14,400
              Over $21,600 but not over $28,800       $1,022 plus 6.80% over $21,600
              Over $28,800 but not over $36,000       $1,512 plus 7.20% over $28,800
              Over $36,000 but not over $54,000       $2,030 plus 7.60% over $36,000
              Over $54,000 but not over $72,000       $3,398 plus 7.90% over $54,000
              Over $72,000 but not over $225,000      $4,820 plus 8.25% over $72,000
              Over $225,000 but not over $262,500     $17,443 plus 9.00% over $225,000
              Over $262,500 but not over $300,000     $20,818 plus 10.00% over $262,500
              Over $300,000                           $24,568 plus 11.00% over $300,000

    Deductions
    Sources - https://files.hawaii.gov/tax/news/pubs/22outline.pdf
    Summary - Standard Deduction:
              Married Filing Jointly or SURVIVING SPOUSE WITH Dependent Child: $4,400
              Single or Married Filing Seperately: $2,200
    Head of Household: $3,212

    Exemptions
    Sources - https://files.hawaii.gov/tax/news/pubs/FastTaxRefGuide_2017.pdf
    Summary - Personal Exemption: $1,144 Per Person
              Age 65 or older: $1,250 per married person, $1,550 per non-married person
    '''

doc_capital_gains = '''
    Capital Gains Taxes
    Sources - https://www.tfhawaii.org/wordpress/state-tax-resources/mini-tax-guides/individual-income-tax-chapter-235/#:~:text=Long%20term%20capital%20gains%20are%20taxed%20at%20a%20maximum%20of%207.25%25.
              https://www.grassrootinstitute.org/2023/02/hb337-increasing-tax-on-capital-gains-a-bad-risk/
    Summary - Fluid situation, but it's currenlty 7.25%. The above testimony discusses a proposal to increase it to 9%
              Applies to net short-term and long-term capital gains
              Current Rate: 7.25%
              Proposed Rate: 9%
    '''

doc_local = '''
    Local Income Taxes
    Sources - https://files.hawaii.gov/tax/news/pubs/22outline.pdf
    Summary - No local jurisdictions impose additional income taxes
    '''

@add_doc(doc_income+doc_capital_gains+doc_local)
def total(filing_status="single", capital_gains_short=0, capital_gains_long=0, credits_state=0, state_agi=0, income=0, dependents=0, filers_over_65=0):
    return 1


@add_doc(filing_status="single", credits_state=0, state_agi=0, income=0, dependents=0, filers_over_65=0)
def income():
    return 2


@add_doc(doc_capital_gains)
def capital_gains(capital_gains_short=0, capital_gains_long=0):
    return 3


@add_doc(doc_local)
def local():
    return 4