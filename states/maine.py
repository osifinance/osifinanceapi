def add_doc(value):
    import os
    def _doc(func):
        func.__doc__ = os.path.basename(__file__).title() + value
        return func
    return _doc

doc_income = '''
    Income Taxes
    Sources - https://www.maine.gov/revenue/tax-return-forms/individual-income-tax-2022
              https://www.maine.gov/revenue/sites/maine.gov.revenue/files/inline-files/ind_tax_rate_sched_2022.pdf
    Summary - For Single Individuals and Married Persons Filing Separate Returns
              If the taxable income is:           The tax is:  
              Less than $23,000                   5.8% of Maine taxable income
              $23,000 but less than $54,450       $1,334 plus 6.75% of excess over $23,000
              $54,450 or more                     $3,457 plus 7.15% of excess over $54,450
                  
              Unmarried or Legally Separated Individuals who Qualify as Heads of Household
              If the taxable income is:           The tax is:  
              Less than $34,500                   5.8% of Maine taxable income
              $34,500 but less than $81,700       $2,001 plus 6.75% of excess over $34,500
              $81,700 or more                     $5,187 plus 7.15% of excess over $81,700       
  
              Married Individuals and Surviving Spouses Filing Joint Returns
              If the taxable income is:           The tax is:  
              Less than $46,000                   5.8% of Maine taxable income  
              $46,000 but less than $108,900      $2,668 plus 6.75% of excess over $46,000
              $108,900 or more                    $6,914 plus 7.15% of excess over $108,900 

    Standard Decution
    Sources - https://www.maine.gov/revenue/sites/maine.gov.revenue/files/inline-files/22_1040me_book_gen_instruc_revisedFeb23.pdf (P. 4)
    Summary - Deductions match 
    
    Exemptions
    Sources - https://www.maine.gov/revenue/sites/maine.gov.revenue/files/inline-files/22_1040me_book_gen_instruc_revisedFeb23.pdf (P. 4)
    Summary - $4,450 per individual/spouse, dependent, and individual/spouse over 65
    '''

doc_capital_gains = '''
    Capital Gains Taxes
    Sources - https://www.maine.gov/revenue/sites/maine.gov.revenue/files/inline-files/22_1040me_book_gen_instruc_revisedFeb23.pdf
    Summary - Net short-term and long-term capital gains are taxed as ordinary income.
    '''

doc_local = '''
    Local Income Taxes
    Sources - https://www.maine.gov/revenue/tax-return-forms/individual-income-tax-2022
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
