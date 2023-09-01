def add_doc(value):
    import os
    def _doc(func):
        func.__doc__ = os.path.basename(__file__).title() + value
        return func
    return _doc


doc_income = '''
    Income Taxes
    Sources - https://mtrevenue.gov/wp-content/uploads/dlm_uploads/2023/02/Form_2_2022-1.pdf (P. 8)
    Summary - If your Montana taxable income is:
              More than         But not more than      Your tax is:
              $0                 $3,300                1%
              $3,300             $5,800                2% - $33
              $5,800             $8,900                3% - $91
              $8,900             $12,000               4% - $180
              $12,000            $15,400               5% - $300
              $15,400            $19,800               6% - $454
              $19,800                                  6.75% - $603

    Reciprocal Agreements
    Sources - https://mtrevenue.gov/wp-content/uploads/2022/12/montana-employees-withholding-allowance-and-exemption-certificate-form-mw-4.pdf
    Summary - North Dakota

    Standard Deduction
    Sources - https://mtrevenue.gov/wp-content/uploads/dlm_uploads/2023/02/Form_2_2022-1.pdf (P. 7)
    Summary - Married Filing Jointly or Head of Household
              $4,520 if your Montana taxable income is $22,600 or less
              20% of your Montana taxable income if your Montana taxable income is more than $22,600 but not more than $50,900
              $10,180 if your Montana taxable income is more than $50,900
  
              Single or Married Filing Separately
              $2,260 if your Montana taxable income is $22,600 or less
              20% of your Montana taxable income if your Montana taxable income is more than $22,600 but not more than $50,900
              $10,180 if your Montana taxable income is more than $50,900

    Exemptions
    Sources - https://mtrevenue.gov/wp-content/uploads/dlm_uploads/2023/02/Form_2_2022-1.pdf (P. 1)
    Summary - $2,710 for each dependent or individual or spouse over the age 65

    EIC
    Sources = https://mtrevenue.gov/wp-content/uploads/dlm_uploads/2023/02/Form_2_2022-1.pdf (P. 1)
    Summary = 3% of federal EIC
    '''

doc_capital_gains = '''
    Capital Gains Taxes
    Sources - https://mtrevenue.gov/2021/11/29/simplification-of-montana-income-taxation/?utm_source=rss&utm_medium=rss&utm_campaign=simplification-of-montana-income-taxation
    Summary - 30% of long term gains are deducted, but all gains are treated as ordinary income
    '''

doc_local = '''
    Local Income Taxes
    Sources - https://mtrevenue.gov/wp-content/uploads/dlm_uploads/2023/02/Form_2_2022-1.pdf (P. 8)
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