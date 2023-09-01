def add_doc(value):
    import os
    def _doc(func):
        func.__doc__ = os.path.basename(__file__).title() + value
        return func
    return _doc

doc_income = ''' 
    Income Taxes (2022)
    Sources - https://revenue.delaware.gov/software-developer/tax-rate-changes/
    Summary - Taxable income range	            Base	    Rate
              At least	    But less than
              $0	        $2,000	            $0	        0%
              $2,000	    $5,000	            $0	        2.2%
              $5,000	    $10,000	            $66	        3.9%
              $10,000	    $20,000	            $261	    4.8%
              $20,000	    $25,000	            $741	    5.2%
              $25,000	    $60,000	            $1,001	    5.55%
              $60,000		                    $2943.50	6.6%

    Deductions and Credits
    Sources - https://revenuefiles.delaware.gov/2022/PIT-RES_TY22_2022-01_PaperInteractive.pdf
              https://revenuefiles.delaware.gov/2022/PIT-RES_TY22_2022-02_Instructions.pdf
    Summary - Line 19: Standard Deduction 
              Married: $6,500
              Otherwise: $3,250

              Line 26A. - Personal Credits
              Number of Exemptions * $110 (Each filer, dependent, and spouse over 60)

              Line 30
              Child Tax Care Credit - 50% OF Federal Credit
    '''

doc_capital_gains = '''
    Capital Gains Taxes
    Sources - https://revenue.delaware.gov/frequently-asked-questions/personal-income-tax-faqs/
    Summary - Capital gains are taxed as ordinary income.
    '''

doc_local = '''
    Local Income Taxes
    Sources - https://www.newcastlede.gov/DocumentCenter/View/20147/City-of-Wilmington-Wage-Tax-Information-PDF
    Summary - Wilmington 1.25% Gross Wages
    '''

@add_doc(doc_income+doc_capital_gains+doc_local)
def total(filing_status="single", county_residence="", capital_gains_short=0, capital_gains_long=0, credits_state=0, state_agi=0, income=0, dependents=0, filers_over_65=0):
    return 1

@add_doc(doc_income)
def income(filing_status="single", county_residence="", capital_gains_short=0, capital_gains_long=0, credits_state=0, state_agi=0, income=0, dependents=0, filers_over_65=0):
    return 2
    
@add_doc(doc_capital_gains)
def capital_gains(filing_status="single", capital_gains_short=0, capital_gains_long=0, credits_state=0, state_agi=0, income=0, dependents=0, filers_over_65=0):
    return 3

@add_doc(doc_local)
def local(income=0):
    return 4
   