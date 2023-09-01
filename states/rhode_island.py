def add_doc(value):
    import os
    def _doc(func):
        func.__doc__ = os.path.basename(__file__).title() + value
        return func
    return _doc

doc_income = '''
    Income Taxes
    Sources - https://tax.ri.gov/sites/g/files/xkgbur541/files/2022-12/2023%20RI-1040ES_w.pdf (P. 1)
    Summary - Amount of wages is:
            - Over      But not over       Tax is:
              $0        $73,450            3.75%
              $73,450   $166,950           $2,754.38 plus 4.75% of the amount over $73,450
              $166,950                     $7,195.63 plus 5.99% of the amount over $166,950

    Standard Deduction and Exemptions
    Sources - https://tax.ri.gov/sites/g/files/xkgbur541/files/2022-12/2023%20RI-1040ES_w.pdf (P. 2)
    Summary - If AGI is less than $233,750:
              Married Filing Jointly: $20,000
              Head of Household: $15,050
              Married Filing Separately: $10,025
              Single: $10,000
              $4,700 per dependent
              Othwerwise, deductions are 4/5 divided by the ceiling of AGI - $233,750 / $6,700
    EIC
    Sources - https://tax.ri.gov/sites/g/files/xkgbur541/files/2022-12/2022_1040WE_w_0.pdf
    Summary - 15% of the federal EIC
    '''

doc_capital_gains = '''
    Capital Gains Taxes
    Sources - https://tax.ri.gov/sites/g/files/xkgbur541/files/2022-12/2023%20RI-1040ES_w.pdf
    Summary - Net short-term and long-term capital gains are taxed as ordinary income.
    '''

doc_local = '''
    Local Income Taxes
    Sources - https://tax.ri.gov/sites/g/files/xkgbur541/files/2022-12/2023%20RI-1040ES_w.pdf
    Summary - No local jurisdictions impose additional income taxes
    '''

@add_doc(doc_income+doc_capital_gains+doc_local)
def total(filing_status="single", capital_gains_short=0, capital_gains_long=0, credits_state=0, state_agi=0, income=0, dependents=0):
    return 1


@add_doc(doc_income)
def income(filing_status="single", capital_gains_short=0, capital_gains_long=0, credits_state=0, state_agi=0, income=0, dependents=0):
    return 2


@add_doc(doc_capital_gains)
def capital_gains(filing_status="single", capital_gains_short=0, capital_gains_long=0, credits_state=0, state_agi=0, income=0, dependents=0):
    return 3


@add_doc(doc_local)
def local():
    return 4
    