def add_doc(value):
    import os
    def _doc(func):
        func.__doc__ = os.path.basename(__file__).title() + value
        return func
    return _doc


doc_income = '''
    Income Taxes
    Sources - https://www.michigan.gov/taxes/iit/new-developments-for-tax-year-2022
    Summary - Flat rate of 4.25%

    Exemptions
    Sources - https://www.michigan.gov/taxes/-/media/Project/Websites/taxes/Forms/2023/2023-SUW/446_Withholding-Guide_2023.pdf?rev=177ca3d8cb034392bf84e317ed78c320&hash=19C5F42F43A89A91863D229349F48883#:~:text=The%20exemption%20amount%20is%20%245%2C400,employee's%20Michigan%20income%20tax%20return.
    Summary - $5,400 for personal and dependent exemptions

    Standard DeductionS (Same as exemptions)
    Sources - https://www.michigan.gov/taxes/iit/retirement-and-pension-benefits/michigan-standard-deduction#:~:text=This%20deduction%20is%20referred%20to,using%20the%20Tier%20Structure%20Subtraction
    Summary - If over age 67, $40,000 for married filing jointly, $20,000 for all others

    Reciprocal Agreements
    Sources - https://www.michigan.gov/taxes/-/media/Project/Websites/taxes/Forms/2023/2023-SUW/446_Withholding-Guide_2023.pdf?rev=177ca3d8cb034392bf84e317ed78c320&hash=19C5F42F43A89A91863D229349F48883#:~:text=The%20exemption%20amount%20is%20%245%2C400,employee's%20Michigan%20income%20tax%20return.
              https://www.michigan.gov/taxes/questions/iit/accordion/residency/are-my-wages-earned-in-another-state-taxable-in-michigan-if-i-am-a-michigan-resident-1
    Summary - Illinois, Indiana, Kentucky, Minnesota, Ohio, and Wisconsin
    '''

doc_capital_gains = '''
    Capital Gains
    Sources - https://www.michigan.gov/taxes/-/media/Project/Websites/taxes/Forms/2022/2022-IIT-Forms/BOOK_MI-1040.pdf?rev=4524f1cbbc0243b194ab05a6680be75b&hash=40DFE71E651F7C1D65C31F6CD03D944F
    Summary - If Age 67 or older, interest, dividends, and capital gains are deductible up to $25,394 for married filing jointly and $12,697 for all others
              Otherwise, net capital gains are treated as ordinary income
    '''

doc_local = '''
    Local Income Taxes
    Sources - https://www.michigan.gov/taxes/questions/iit/accordion/general/what-cities-impose-an-income-tax
    Summary - Non-Resident is 50% of the following rates
              Albion	          1%
              Battle Creek  	  1%
              Benton Harbor       1%
              Big Rapids	      1%
              Detroit             2.4%
              East Lansing	      1%
              Flint 	          1%	
              Grand Rapids        1.5%
              Grayling	          1% 
              Hamtramck	          1%
              Highland Park       2%
              Hudson	          1%
              Ionia	              1%
              Jackson	          1%
              Lansing	          1%
              Lapeer	          1%
              Muskegon	          1%
              Muskegon Heights    1%
              Pontiac	          1%
              Port Huron          1%
              Portland	          1%
              Saginaw             1.5%
              Springfield	      1%
              Walker	          1%
    '''

@add_doc(doc_income+doc_capital_gains+doc_local)
def total(filing_status="single", county_residence="", county_occupation="", capital_gains_short=0, capital_gains_long=0, credits_state=0, state_agi=0, income=0, dependents=0, age_over_67=False):
    return 1


@add_doc(doc_income)
def income(filing_status="single", county_residence="", county_occupation="", capital_gains_short=0, capital_gains_long=0, credits_state=0, state_agi=0, income=0, dependents=0, age_over_67=False):
    return 2


@add_doc(doc_capital_gains)
def capital_gains(filing_status="single", county_residence="", county_occupation="", capital_gains_short=0, capital_gains_long=0, credits_state=0, state_agi=0, income=0, dependents=0, age_over_67=False):
    return 3


@add_doc(doc_local)
def local(filing_status="single", county_residence="", county_occupation="", capital_gains_short=0, capital_gains_long=0, credits_state=0, state_agi=0, income=0, dependents=0, age_over_67=False):
    return 4