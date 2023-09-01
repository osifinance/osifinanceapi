def add_doc(value):
    import os
    def _doc(func):
        func.__doc__ = os.path.basename(__file__).title() + value
        return func
    return _doc

doc_income = '''
Income Taxes
Sources - https://dor.mo.gov/taxation/individual/tax-types/income/year-changes/
Summary - If the Missouri taxable income is     The tax is
          $0 to $111	                        $0
          At least $112 but not over $1,121	    1.5% of the Missouri taxable income
          Over $1,121 but not over $2,242	    $17 plus 2.0% of excess over $1,121
          Over $2,242 but not over $3,363	    $39 plus 2.5% of excess over $2,242
          Over $3,363 but not over $4,484	    $67 plus 3.0% of excess over $3,363
          Over $4,484 but not over $5,605	    $101 plus 3.5% of excess over $4,484
          Over $5,605 but not over $6,726	    $140 plus 4.0% of excess over $5,605
          Over $6,726 but not over $7,847	    $185 plus 4.5% of excess over $6,726
          Over $7,847 but not over $8,968	    $235 plus 5.0% of excess over $7,847
          Over $8,968	                        $291 plus 5.3% of excess over $8,968

Standard Deduction
Sources - https://dor.mo.gov/taxation/individual/tax-types/income/year-changes/
Summary - Same as federal
'''

doc_capital_gains = '''
    Capital Gains Taxes
    Sources - https://dor.mo.gov/taxation/individual/tax-types/income/year-changes/
    Summary - Net short-term and long-term capital gains are taxed as ordinary income.
    '''

doc_local = '''
    Local Income Taxes
    Sources - https://www.kcmo.gov/city-hall/departments/finance/earnings-tax
              https://www.stlouis-mo.gov/government/departments/collector/earnings-tax/individual-earnings-tax-info.cfm
    Summary - KCMO 1%
              St. Louis 1%
    '''

@add_doc(doc_income+doc_capital_gains+doc_local)
def total(filing_status="single", county_residence="", capital_gains_short=0, capital_gains_long=0, credits_state=0, state_agi=0, income=0, dependents=0, filers_over_65=0):
    return 1


@add_doc(doc_income)
def income(filing_status="single", county_residence="", capital_gains_short=0, capital_gains_long=0, credits_state=0, state_agi=0, income=0, dependents=0, filers_over_65=0):

    return 2

@add_doc(doc_local)
def capital_gains(filing_status="single", county_residence="", capital_gains_short=0, capital_gains_long=0, credits_state=0, state_agi=0, income=0, dependents=0, filers_over_65=0):
    return 3


@add_doc(doc_local)
def local(filing_status="single", county_residence="", capital_gains_short=0, capital_gains_long=0, credits_state=0, state_agi=0, income=0, dependents=0, filers_over_65=0):
    return 4
