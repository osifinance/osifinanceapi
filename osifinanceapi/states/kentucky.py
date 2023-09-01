def add_doc(value):
    import os
    def _doc(func):
        func.__doc__ = os.path.basename(__file__).title() + value
        return func
    return _doc

doc_income = '''
    Income Taxes
    Sources - https://revenue.ky.gov/News/Pages/Dor-Announces-Updates-to-Individual-Income-Tax-for-2023-Tax-Year.aspx
              https://revenue.ky.gov/Individual/Individual-Income-Tax/Pages/default.aspx
    Summary - 4.5% of all income

    Deductions
    Sources - https://revenue.ky.gov/News/Pages/Dor-Announces-Updates-to-Individual-Income-Tax-for-2023-Tax-Year.aspx
    Summary - Married: $5,960
              Otherwise: $2,980

    Child and Dependent Care Credit
    Sources - https://revenue.ky.gov/Individual/Individual-Income-Tax/Pages/default.aspx
    Summary - 20% OF THE FEDERAL CREDIT
    
    Reciprocal Agreements
    Sources - https://revenue.ky.gov/Dor%20Training%20Materials/103%20KAR%2017.140.%20Individual%20income%20tax%20-%20reciprocity%20-%20nonresidents.pdf
    Summary - Ohio, Illinois, Michigan, Wisconsin, Pennsylvania, Indiana, West Virginia
    '''

doc_capital_gains = '''
    Capital Gains Taxes
    Sources - https://revenue.ky.gov/Individual/Individual-Income-Tax/Pages/default.aspx
    Summary - Net short-term and long-term capital gains are taxed as ordinary income.
    '''

doc_local = '''
    Local Income Taxes
    Sources - https://nfc.usda.gov/Publications/HR_Payroll/Taxes/Bulletins/2021/Taxes-21-32.htm?taxmap=true
    Summary - City                    Rate
              Bowling Green           1.85%
              Covington               2.45%*
              Florence                2.00%**
              Frankfort               1.95%
              Lexington-Fayette       2.25%
              Louisville              1.45%
              Owensboro               1.78%
              Paducah                 2.00%
              Richmond                2.00%
  
              * Maximum withholding wage base of $160,200*** (maximum annual withholding of $3,601.50).
              ** Maximum withholding wage base of $160,200*** (maximum annual withholding of $2,940.00).
              *** Assuming $147,000 limit increased along with the Social Security wage limit
    '''

@add_doc(doc_income+doc_capital_gains+doc_local)
def total(filing_status="single", county_residence="", capital_gains_short=0, capital_gains_long=0, credits_state=0, state_agi=0, income=0):
    return 1


@add_doc(doc_income)
def income(filing_status="single", county_residence="", capital_gains_short=0, capital_gains_long=0, credits_state=0, state_agi=0, income=0, dependents=0, filers_over_65=0):
    return 2


@add_doc(doc_capital_gains)
def capital_gains(filing_status="single", county_residence="", capital_gains_short=0, capital_gains_long=0, credits_state=0, state_agi=0, income=0, dependents=0, filers_over_65=0):
    return 3


@add_doc(doc_local)
def local(income=0, county_residence=""):
    return 4
