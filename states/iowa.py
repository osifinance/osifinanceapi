def add_doc(value):
    import os
    def _doc(func):
        func.__doc__ = os.path.basename(__file__).title() + value
        return func
    return _doc    

doc_income = '''
    Income Taxes (2023-2026)
    Sources - https://tax.iowa.gov/2023-changes-iowa-individual-income-tax#:~:text=Individual%20Income%20Tax%20Rates%20(HF%202317)&text=Beginning%20in%20tax%20year%202026,who%20file%20a%20joint%20return.
    Summary - Income Tax Brackets	Rates (Brackets double for married filing jointly)
              Lower Limit	    Upper Limit	    TY 2023	    TY 2024 	TY 2025	    TY 2026
              $0	            $6,000	        4.40%	    4.40%   	4.40%   	3.90%
              $6,001	        $30,000	        4.82%   	4.82%   	4.82%   	3.90%
              $30,001	        $75,000	        5.70%	    5.70%	    4.82%   	3.90%
              $75,001	And over            	6.00%	    5.70%   	4.82%   	3.90%

    Deductions
    Sources - https://tax.iowa.gov/2023-changes-iowa-individual-income-tax#:~:text=Individual%20Income%20Tax%20Rates%20(HF%202317)&text=Beginning%20in%20tax%20year%202026,who%20file%20a%20joint%20return.
    Summary - Same as federal Per 2023 changes

    Retirement Income Exclusion
    Sources- https://tax.iowa.gov/2023-changes-iowa-individual-income-tax#:~:text=Individual%20Income%20Tax%20Rates%20(HF%202317)&text=Beginning%20in%20tax%20year%202026,who%20file%20a%20joint%20return.
    Summary - Many complex perks, free traditional to IRA conversions, etc.

    Recirprocal Agreements
    Sources - https://tax.iowa.gov/iowa-illinois-reciprocal-agreement
    Summary - Illinois 
    '''

doc_capital_gains = '''
    Capital Gains Taxes
    Sources - https://tax.iowa.gov/2023-changes-iowa-individual-income-tax#:~:text=Individual%20Income%20Tax%20Rates%20(HF%202317)&text=Beginning%20in%20tax%20year%202026,who%20file%20a%20joint%20return.
    Summary - Net short-term and long-term capital gains are taxed as ordinary income.
    '''

doc_local = '''
    Local Income Taxes
    Sources - www.freetaxusa.com/FreeTaxUSA/formdownload?form=ia_school_dist.pdf
    Summary - Extremeley long list, click link
    '''

@add_doc(doc_income+doc_capital_gains+doc_local)
def total(filing_status="single", county_residence="", capital_gains_short=0, capital_gains_long=0, credits_state=0, state_agi=0, income=0, dependents=0):
    return 1


@add_doc(doc_income)
def income(filing_status="single", county_residence="", capital_gains_short=0, capital_gains_long=0, credits_state=0, state_agi=0, income=0, dependents=0):
    return 2


@add_doc(doc_capital_gains)
def capital_gains(filing_status="single", county_residence="", capital_gains_short=0, capital_gains_long=0, credits_state=0, state_agi=0, income=0, dependents=0):
    return 3


@add_doc(doc_local)
def local(filing_status="single", county_residence="", capital_gains_short=0, capital_gains_long=0, credits_state=0, state_agi=0, income=0, dependents=0):
    return 4