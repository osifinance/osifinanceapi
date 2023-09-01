def add_doc(value):
    import os
    def _doc(func):
        func.__doc__ = os.path.basename(__file__).title() + value
        return func
    return _doc

doc_income = '''
    Income Taxes
    Sources - https://www.state.nj.us/treasury/taxation/taxtables.shtml
    Summary - Single or Married Filing Seperately
              If Taxable Income is:
              Over       But not over        Tax is
              $0         $20,000             1.4%  
              $20,000    $35,000             1.75% - $70
              $35,000    $40,000             3.5% - $682.50
              $40,000    $75,000             5.525% - $1,492.50
              $75,000    $500,000            6.37% - $2,126.25
              $500,000   $1,000,000          8.97% - $15,126.25
              $1,000,000                     10.75% - $32,926.25
                  
              Married/CU filing joint, Head of household, or Qualifying widow(er)/surviving CU partner STEP
              Single or Married Filing Seperately
              If Taxable Income is:
              Over       But not over        Tax is
              $0         $20,000             1.4%  
              $20,000    $50,000             1.75% - $70
              $50,000    $70,000             2.45% - $420
              $70,000    $80,000             3.5% - $1,154.5
              $80,000    $150,000            5.525% - $2,775
              $150,000   $500,000            6.37% - $4,042.5
              $500,000   $1,000,000          8.97% - $17,042.5
              $1,000,000                     10.75% - $34,842.5

    Exemptions
    Sources - https://www.state.nj.us/treasury/taxation/njit13.shtml
    Summary - Regular Exemptions
              You can claim a $1,000 exemption for yourself and your spouse/CU partner (if filing a joint return) or your Domestic Partner.
              
              Senior 65+ Exemptions
              You can claim a $1,000 exemption if you were 65 or older on the last day of the tax year. If you are filing jointly, your spouse can take a $1,000 exemption if they were 65 or older on the last day of the tax year. You cannot claim this exemption for your domestic partner or dependents.

              Dependent Exemptions
              You can claim a $1,500 exemption for each child or dependent who qualifies as your dependent for federal tax purposes.

    Reciprocal Agreements
    Sources - https://www.nj.gov/treasury/taxation/njit25.shtml
    Summary - Pennsylvania
    '''

doc_capital_gains = '''
    Capital Gains Taxes
    Sources - https://www.state.nj.us/treasury/taxation/individuals/freqqiti.shtml
    Summary - Net short-term and long-term capital gains are taxed as ordinary income.
    '''

doc_local = '''
    Local Income Taxes
    Sources - https://www.state.nj.us/treasury/taxation/localtax.shtml
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
def local(filing_status="single", capital_gains_short=0, capital_gains_long=0, credits_state=0, state_agi=0, income=0, dependents=0, filers_over_65=0):
    return 4