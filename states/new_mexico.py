def add_doc(value):
    import os
    def _doc(func):
        func.__doc__ = os.path.basename(__file__).title() + value
        return func
    return _doc

doc_income = '''
    Income Taxes
    Sources - https://klvg4oyd4j.execute-api.us-west-2.amazonaws.com/prod/PublicFiles/34821a9573ca43e7b06dfad20f5183fd/fdf3c548-8aba-4b9c-9eb4-bb564c716015/FYI-104.pdf
    Summary - Single or Married Filing Seperately
              If the amount                                                             
              Is over      but not over     Tax is                                   
              $6,925       $12,425          1.7% of income over $6,925
              $12,425      $17,925          $93.50 + 3.2% of ncome over $12,425
              $17,925      $22,925          $269.5 + 4.7% of income over $17,925
              $22,925      $216,925         $504.5 + 4.9% if income over $22,925
              $216,925                      $10,010.5 + 5.9% of income over 216,925
              
              Married or Head of Household
              If the amount                                                             
              Is over      but not over     Tax is                                   
              $13,850      $21,850          1.7% of income over $13,850
              $21,850      $29,850          $136 + 3.2% of income over $21,850
              $29,850      $37,850          $392 + 4.7% of income over $29,850
              $37,850      $328,850         $768 + 4.9% if income over $37,850
              $328,850                      $15,027 + 5.9% of income over 216,925

    Deductions Credits
    Sources - https://klvg4oyd4j.execute-api.us-west-2.amazonaws.com/prod/PublicFiles/34821a9573ca43e7b06dfad20f5183fd/0bf943fd-652e-4400-bb1b-cd8397eb5a95/2022pit-adj.pdf (Form)
              https://klvg4oyd4j.execute-api.us-west-2.amazonaws.com/prod/PublicFiles/34821a9573ca43e7b06dfad20f5183fd/2f1a6781-9534-4436-b427-1557f9592099/2022pit-adj-ins.pdf (Instructions)
    Summary - Very nuanced, see sources

    Social Security
    Sources - Sources - https://klvg4oyd4j.execute-api.us-west-2.amazonaws.com/prod/PublicFiles/34821a9573ca43e7b06dfad20f5183fd/0bf943fd-652e-4400-bb1b-cd8397eb5a95/2022pit-adj.pdf (Line 24. of PIT)
    Summary - Untaxed 
    '''

doc_capital_gains = '''
    Capital Gains Taxes
    Summary - https://klvg4oyd4j.execute-api.us-west-2.amazonaws.com/prod/PublicFiles/34821a9573ca43e7b06dfad20f5183fd/1afc56af-ea90-4d48-82e5-1f9aeb43255a/PITbook2022.pdf
    Sources - The first $1,000 of net capital gains are deducted or the greater of 40% of net capital gains are deducted from Adjusted Gross Income (AGI)
    '''

doc_local = '''
    Local Income Taxes
    Sources - https://klvg4oyd4j.execute-api.us-west-2.amazonaws.com/prod/PublicFiles/34821a9573ca43e7b06dfad20f5183fd/fdf3c548-8aba-4b9c-9eb4-bb564c716015/FYI-104.pdf
    Summary - No local jurisdictions impose additional income taxes
    '''

@add_doc(doc_income+doc_capital_gains+doc_local)
def total(filing_status="single", capital_gains_short=0, capital_gains_long=0, credits_state=0, state_agi=0, income=0, dependents=0):
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