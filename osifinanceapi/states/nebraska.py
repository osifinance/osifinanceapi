def add_doc(value):
    import os
    def _doc(func):
        func.__doc__ = os.path.basename(__file__).title() + value
        return func
    return _doc


doc_income = '''
    Income Taxes
    Sources - https://revenue.nebraska.gov/sites/revenue.nebraska.gov/files/doc/2023_Circular_EN_8-429r2023_Whole_Book_11.pdf
    Summary - Single or Head of Household
              If the taxable income is:           
              Over:       But not over:      The tax is:
              $3,060      $5,990             $0 plus 2.26% of the amount over $3,060
              $5,990      $19,470            $66.22 plus 3.22% of the amount over $5,990
              $19,470     $28,210            $500.28 plus 4.91% of the amount over $19,470
              $28,210     $35,820            $929.41 plus 6.20% of the amount over $28,210
              $35,820     $67,270            $1,401.23 plus 6.39% of the amount over $35,820
              $67,270                        $3,410.89  plus 6.75% of the amonut over $67,270
  
              Married Filing Jointly or Qualifying Widow(er)
              If the taxable income is:           
              Over:       But not over:      The tax is:
              $7,530      $11,610            $0 plus 2.26% of the amount over $7,530
              $11,610     $28,910            $92.21 plus 3.22% of the amount over $11,610
              $28,910     $44,980            $649.27 plus 4.91% of the amount over $28,910
              $44,980     $55,810            $1,438.31 plus 6.20% of the amount over $44,980
              $55,810     $74,010            $2,109.77 plus 6.39% of the amount over $55,810
              $74,010                        $3,272.75  plus 6.75% of the amonut over $67,270

    Standard Deduction
    Sources - https://revenue.nebraska.gov/sites/revenue.nebraska.gov/files/doc/2022_Ne_Individual_Income_Tax_Booklet_8-307-2022_final_6.pdf (P.9)
    Summary - If you or your spourse are over 65:  Neither      One         Both
              Single                               $7,350       $9,050      
              Married Filing Jointly               $14,700      $18,100     $21,500
              Married Filing Separately            $7,350       $8,750      $10,150
              Head of Household                    $10,750      $12,450     

    Credits
    Sources - https://revenue.nebraska.gov/sites/revenue.nebraska.gov/files/doc/2022_Ne_Individual_Income_Tax_Booklet_8-307-2022_final_6.pdf (p.23-24)
    Summary - $146 per filer and dependent (max 3 dependents)
    '''

doc_capital_gains = '''
    Capital Gains Taxes
    Sources - https://revenue.nebraska.gov/sites/revenue.nebraska.gov/files/doc/2022_Ne_Individual_Income_Tax_Booklet_8-307-2022_final_6.pdf (p. 9)
    Summary - Net short-term and long-term capital gains are taxed as ordinary income.
    '''

doc_local = '''
    Local Income Taxes
    Sources - https://revenue.nebraska.gov/sites/revenue.nebraska.gov/files/doc/2022_Ne_Individual_Income_Tax_Booklet_8-307-2022_final_6.pdf (p. 9)
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
def local():
    return 4