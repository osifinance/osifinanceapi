def add_doc(value):
    import os
    def _doc(func):
        func.__doc__ = os.path.basename(__file__).title() + value
        return func
    return _doc

doc_income = '''
    Income Taxes
    Sources - https://tax.idaho.gov/taxes/income-tax/individual-income/individual-income-tax-rate-schedule/
    Single
    At least	Less than	Tax	Rate
    $1	        $1,662	    $0.00	plus 1.0% of the amount over $0
    $1,662  	$4,987	    $16.62	plus 3.0% of the amount over $1,662
    $4,987	    $8,311	    $116.36	plus 4.5% of the amount over $4,987
    $8,311		            $265.96	plus 6.0% of the amount over $8,311
    Married
    At least	Less than	Tax	Rate
    $1	        $3,324	    $0.00	plus 1.0% of the amount over $0
    $3,324	    $9,974	    $33.24	plus 3.0% of the amount over $3,324
    $9,974	    $16,622	    $232.72	plus 4.5% of the amount over $9,974
    $16,622		            $531.92	plus 6.0% of the amount over $16,622

    Deductions 
    Sources - https://tax.idaho.gov/wp-content/uploads/forms/EIN00046/EIN00046_03-01-2023.pdf (P.8)
    Summary - Same as federal
    '''

doc_capital_gains = '''
    Capital Gains Taxes
    Sources - https://tax.idaho.gov/taxes/income-tax/individual-income/idaho-source-income/
    Summary - Short-term capital gains are taxed as ordinary income.
    '''

doc_local = '''
    Local Income Taxes
    Sources - https://tax.idaho.gov/taxes/income-tax/individual-income/idaho-source-income/
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