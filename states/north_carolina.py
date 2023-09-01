def add_doc(value):
    import os
    def _doc(func):
        func.__doc__ = os.path.basename(__file__).title() + value
        return func
    return _doc

doc_income = '''
    Income Taxes
    Sources - https://www.ncdor.gov/taxes-forms/tax-rate-schedules
    Summary - 2023: 4.75%
              2024: 4.6%
              2025: 4.5%
              2026: 4.25%
              2027+: 4%

    Deductions
    Sources - https://www.ncdor.gov/taxes-forms/individual-income-tax/north-carolina-standard-deduction-or-north-carolina-itemized-deductions
    Summary - If your filing status is:	                                    Your standard deduction is:
              Single	                                                    $12,750
              Married Filing Jointly/Qualifying Widow(er)/Surviving Spouse	$25,500
              Married Filing Separately	 
                  Spouse does not claim itemized deductions                 $12,750
                  Spouse claims itemized deductions                         $0
              Head of Household	                                            $19,125
    '''

doc_capital_gains = '''
    Capital Gains Taxes
    Sources - https://www.ncdor.gov/taxes-forms/individual-income-tax
    Summary - Net short-term and long-term capital gains are taxed as ordinary income.
    '''

doc_local = '''
    Local Income Taxes
    Sources - https://www.ncdor.gov/taxes-forms/individual-income-tax
    Summary - No local jurisdictions impose additional income taxes
    '''


@add_doc(doc_income+doc_capital_gains+doc_local)
def total(filing_status="single", capital_gains_short=0, capital_gains_long=0, credits_state=0, state_agi=0, income=0):
    return 1


@add_doc(doc_income)
def income(filing_status="single", capital_gains_short=0, capital_gains_long=0, credits_state=0, state_agi=0, income=0):
    return 2


@add_doc(doc_capital_gains)
def capital_gains(filing_status="single", capital_gains_short=0, capital_gains_long=0, credits_state=0, state_agi=0, income=0):
    return 3


@add_doc(doc_local)
def local():
    return 4
    