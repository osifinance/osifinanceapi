def add_doc(value):
    import os
    def _doc(func):
        func.__doc__ = os.path.basename(__file__).title() + value
        return func
    return _doc

doc_income = '''
    Income Taxes
    Sources - https://www.mass.gov/service-details/massachusetts-tax-rates
    Summary - Flat Rate of 5%

    Deductions 
    Sources - https://www.mass.gov/service-details/view-massachusetts-personal-income-tax-exemptions
    Summary - $1000 deduction per dependent

    Standard Deduction
    Sources - https://www.mass.gov/service-details/view-massachusetts-personal-income-tax-exemptions
    Summary - Single or Married Filing Seperately - $4,400
              Married Filing Jointly or QUALIFYING WIDOW - $8,800
              Head of Household - $6,800

    Credits
    Sources - https://www.mass.gov/service-details/view-child-and-dependent-related-credits
    Summary - $240 credit per dependent, max 2
    '''

doc_capital_gains = '''
    Capital Gains Taxes
    Sources - https://www.mass.gov/service-details/massachusetts-tax-rates
    Sumamry - Long-term: 5%
              Short-term: 12%
    '''

doc_local = '''
    Local Income Taxes
    Sources - https://www.mass.gov/personal-income-tax
    Summary - No local jurisdictions impose additional income taxes
    '''

@add_doc(doc_income+doc_capital_gains)
def total(filing_status="single", capital_gains_short=0, capital_gains_long=0, credits_state=0, state_agi=0, income=0, dependents=0):
    return 1

@add_doc(doc_income)
def income(filing_status="single", capital_gains_short=0, capital_gains_long=0, credits_state=0, state_agi=0, income=0, dependents=0):
    return 2
    
@add_doc(doc_capital_gains)
def capital_gains(capital_gains_short=0, capital_gains_long=0):
    return 3

@add_doc(doc_local)
def local():
    return 4