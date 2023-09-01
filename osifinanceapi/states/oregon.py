def add_doc(value):
    import os
    def _doc(func):
        func.__doc__ = os.path.basename(__file__).title() + value
        return func
    return _doc

doc_income = '''
    Income Taxes
    sources - https://www.oregon.gov/dor/programs/individuals/Pages/PIT.aspx
              https://www.oregon.gov/dor/programs/individuals/Documents/Full%20year%20resident,%20Form%20or-40%20filers.pdf
              https://www.oregon.gov/dor/programs/individuals/Documents/Part-year%20and%20nonresident,%20Form%20or-40-P%20and%20or-40-N%20filers.pdf.pdf

    Summary - Tax rate charts Chart S:
              For persons filing single or married filing separately— 
              If your taxable income is not over $3,750 .......................................................................................your tax is 4.75% of taxable income
              If your taxable income is over $3,750 but not over $9,450 .............................your tax is $178 plus 6.75% of excess over $3,750
              If your taxable income is over $9,450 but not over $125,000 ........................your tax is $563 plus 8.75% of excess over $9,450
              If your taxable income is over $125,000 ........................................................your tax is $10,674 plus 9.9% of excess over $125,000
                  
              Chart J: For persons filing jointly, head of household, or qualifying surviving spouse with dependent child—
              If your taxable income is not over $7,500 .......................................................................................your tax is 4.75% of taxable income
              If your taxable income is over $7,500 but not over $18,900 ...........................your tax is $356 plus 6.75% of excess over $7,500
              If your taxable income is over $18,900 but not over $250,000 ................your tax is $1,126 plus 8.75% of excess over $18,900
              If your taxable income is over $250,000....................................................... your tax is $21,347 plus 9.9% of excess over $250,000

    Standard Deduction
    Sources - https://www.oregon.gov/dor/forms/FormsPubs/form-or-40_101-040_2022.pdf (P. 3)
    Summary - Married filing jointly or qualifying widow(er): $4,840
              Single or married filing seperately: $2,420
              Head of household: $3,895

    Dependent and age over 65 Credits
    Sources - https://www.oregon.gov/dor/forms/FormsPubs/form-or-40_101-040_2022.pdf (P. 4)
    Summary - $219 per dependent, if income is below $100,00 ($200,000 for married filing jointly)
    '''
doc_capital_gains = '''
    Capital Gains Taxes
    Sources - https://www.oregon.gov/dor/forms/FormsPubs/form-or-40_101-040_2022.pdf (P. 3)
    Summary - Net short-term and long-term capital gains are taxed as ordinary income.
    '''

doc_local = '''
    Local Income Taxes
    Sources - https://www.oregon.gov/dor/programs/individuals/Pages/PIT.aspx
    Summary - No local jurisdictions impose additional income taxes
    '''

@add_doc(doc_income+doc_capital_gains+doc_local)
def total(filing_status="single", capital_gains_short=0, capital_gains_long=0, credits_state=0, state_agi=0, income=0, dependents=0, filers_over_65=0):
    return 1


@add_doc(doc_income)
def income(filing_status="single", capital_gains_short=0, capital_gains_long=0, credits_state=0, state_agi=0, income=0, dependents=0, filers_over_65=0):
    return 2


@add_doc(doc_capital_gains)
def capital_gains(filing_status="single", capital_gains_short=0, capital_gains_long=0, credits_state=0, state_agi=0, income=0, dependents=0, filers_over_65=0):
    return 3


@add_doc(doc_local)
def local():
    return 4