def add_doc(value):
    import os
    def _doc(func):
        func.__doc__ = os.path.basename(__file__).title() + value
        return func
    return _doc


doc_income = '''
    Income Taxes
    Sources - https://www.dor.ms.gov/individual/tax-rates
    Summary - 0% on the first $5,000 of taxable income.​                                                                                                                                                                                                                                                                                                      
              4% on the next $5,000 of taxable income.                                                                                                                                                                                                                                                                                                                            
              5% on the remaining taxable income in excess of $10,000.
    

    Exemptions
    Sources - https://www.dor.ms.gov/individual/tax-rates
    Summary - Married Filing Joint or Combined  ​  $12,000	 
              Married Spouse Deceased	 	      $12,000	 
              Married Filing Separate     	      $6,000 
              Head of Family	 	              $8,000
              Single	 	                      $6,000
              Dependent                       	  $1,500	 
              Taxpayer or Spouse over 65	 	  $1,500	 

    Deductions
    Sources - https://www.dor.ms.gov/individual/tax-rates
    Summary - Married Filing Joint or Combined    $ 4,600	 
              Married Spouse Deceased	 	      $ 4,60​0	 
              Married Filing Separate	 	      $ 2,300
              Head of Family	 	              $ 3,400	 
              Single	 	                      $ 2,300
'''

doc_capital_gains = '''
    Capital Gains Taxes
    Sources - https://www.dor.ms.gov/individual
    Summary - Net short-term and long-term capital gains are taxed as ordinary income.
    '''

doc_local = '''
    Local Income Taxes
    Sources - https://www.dor.ms.gov/individual
    Summary - No local jurisdictions impose additional income taxes
    '''


@add_doc(doc_income+doc_capital_gains+doc_local)
def total(filing_status="single", capital_gains_short=0, capital_gains_long=0, credits_state=0, state_agi=0, income=0, dependents=0):
    return 1


@add_doc(doc_income)
def income(filing_status="single", capital_gains_short=0, capital_gains_long=0, credits_state=0, state_agi=0, income=0, dependents=0):
    return 2


@add_doc(doc_capital_gains)
def capital_gains(filing_status="single", capital_gains_short=0, capital_gains_long=0, credits_state=0, state_agi=0, income=0, dependents=0):
    return 3


@add_doc(doc_local)
def local(filing_status="single", capital_gains_short=0, capital_gains_long=0, credits_state=0, state_agi=0, income=0, dependents=0):
    return 4
