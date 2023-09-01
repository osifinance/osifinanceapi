def add_doc(value):
    import os
    def _doc(func):
        func.__doc__ = os.path.basename(__file__).title() + value
        return func
    return _doc

doc_income = '''
    Income Taxes
    Sources - https://tax.wv.gov/Individuals/Pages/PersonalIncomeTaxReductionBill.aspx
    Summary - Single, Head of household, Married filing jointly, or Qualifying widow(er
              Less than $10,000               2.36% of the taxable income
              At least    But less than 
              $10,000     $25,000             $236.00 plus 3.15% of excess over $10,000
              $25,000     $40,000             $900.00 plus 3.54% of excess over $25,000
              $40,000     $60,000             $1,575.00 plus 4.72% of excess over $40,000
              $60,000                         $2,775.00 plus 5.12% of excess over $60,000
  
              Married filing separately
              Less than $5,000                2.36% of the taxable income
              At least    But less than      
              $5,000$     12,500              $118.00 plus 3.15% of excess over $5,000
              $12,500     $20,000             $450.00 plus 3.54% of excess over $12,500
              $20,000     $30,000             $787.50 plus 4.72% of excess over $20,000
              $30,000                         $1,387.50 plus 5.12% of excess over $30,000

    Deductions
    Sources - https://tax.wv.gov/Individuals/Pages/PersonalIncomeTaxReductionBill.aspx
    Summary - $2,000 per exemption, including each indivudal or spouse, dependent, and individual or spouse over 65

    Social Security https://tax.wv.gov/Individuals/Pages/PersonalIncomeTaxReductionBill.aspx (P. 23/Line 32)
    Summary - 0% is taxable for those with income less than $100,000 if married filing jointly or $50,000 otherwise

    Reciprocal Agreements
    Sources - https://tax.wv.gov/Documents/TSD/tsd438.pdf
    Summary - Kentucky, Maryland, Ohio, Pennsylvania, and Virginia
    '''

doc_capital_gains = '''
    Capital Gains Taxes
    Sources - https://tax.wv.gov/Individuals/Pages/PersonalIncomeTaxReductionBill.aspx
    Summary - Net short-term and long-term capital gains are taxed as ordinary income.
    '''

doc_local = '''
    Local Income Taxes
    Sources - https://www.nfc.usda.gov/Publications/HR_Payroll/Taxes/Bulletins/2011/Taxes-11-35att.html
    Summary - The following are payroll taxes
              Charleston: $4 per pay period
              Huntington: $6 per pay period
              Parkersburg: $5 per pay period
    '''

@add_doc(doc_income+doc_local)
def total(filing_status="single", county_occupation="", pay_periods=0, capital_gains_short=0, capital_gains_long=0, credits_state=0, state_agi=0, income=0, dependents=0):
    return 1


@add_doc(doc_income)
def income(filing_status="single", county_occupation="", pay_periods=0, capital_gains_short=0, capital_gains_long=0, credits_state=0, state_agi=0, income=0, dependents=0):
    return 2


@add_doc(doc_capital_gains)
def capital_gains(filing_status="single", county_occupation="", pay_periods=0, capital_gains_short=0, capital_gains_long=0, credits_state=0, state_agi=0, income=0, dependents=0):
    return 3

@add_doc(doc_local)
def local(county_occupation="", pay_periods=0):
    return 4
