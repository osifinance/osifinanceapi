def add_doc(value):
    import os
    def _doc(func):
        func.__doc__ = os.path.basename(__file__).title() + value
        return func
    return _doc

doc_income = '''
    Income Taxes
    Sources - https://incometax.utah.gov/paying/tax-rates
              https://tax.utah.gov/forms/current/tc-40.pdf
    Summary - Flat rate of 4.85%

    Deductions
    Sources - https://tax.utah.gov/forms/current/tc-40.pdf (Box 17)
    Summary - Federal deductions apply prior to the following phaseout thresholds
              6% of Federal deductions applies as a tax credit, not refundable
              Single or Married Filing Separately: $15,548
              Married Filing Jointly or Qualifying Widow(er): $31,096
              Head of Household: $23,322
              1.3% of AGI over the thresholds is added back to AGI

    Dependent Deduction
    Sources - https://tax.utah.gov/forms/current/tc-40.pdf (Box 2, 11)
    Summary - $1,802 per dependent
    '''

doc_capital_gains = '''
    Capital Gains Taxes
    Sources - https://tax.utah.gov/forms/current/tc-40.pdf
    Summary - Net short-term and long-term capital gains are taxed as ordinary income.
    '''

doc_local = '''
    Local Income Taxes
    Sources - https://tax.utah.gov/forms/current/tc-40.pdf
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