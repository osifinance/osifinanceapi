def add_doc(value):
    import os
    def _doc(func):
        func.__doc__ = os.path.basename(__file__).title() + value
        return func
    return _doc

doc_income = '''
    Income Taxes
    Sources - https://oklahoma.gov/content/dam/ok/en/tax/documents/resources/publications/businesses/withholding-tables/WHTables-2022.pdf
    Summary - Single or Married Filing Seperately
              If the amount of wages is:
              Over        but less than   The amount of income tax to withhold is:
              $0          $6,350          $0
              $6,350      $7,350          $0 + 0.25% of the excess over $6,350
              $7,350      $8,850          $2.50 + 0.75% of the excess over $7,350
              $8,850      $10,100         $13.75 + 1.75% of the excess over $8,850
              $10,100     $11,250         $35.63 + 2.75% of the excess over $10,100
              $11,250     $13,550         $67.25 + 3.75% of the excess over $11,250
              $13,550                     $153.50 + 4.75% of the excess over $13,550 
  
              Married Filing Jointly, Head of Household, and Qualifying Widower
              If the amount of wages is:
              Over        but less than   The amount of income tax to withhold is:
              $0          $12,700         $0   
              $12,700     $14,700         $0 + 0.25% of the excess over $12,700
              $14,700     $17,700         $5.00 + 0.75% of the excess over $14,700
              $17,700     $20,200         $27.50 + 1.75% of the excess over $17,700
              $20,200     $22,500         $71.25 + 2.75% of the excess over $20,200
              $22,500     $24,900         $134.50 + 3.75% of the excess over $22,500
              $24,900                     $224.50 + 4.75% of the excess over $24,900

    Deductions
    Sources - https://oklahoma.gov/content/dam/ok/en/tax/documents/forms/individuals/current/511-NR-Pkt.pdf
    Summary - Oklahoma allows $1,000 for each exemption claimed at the top of page 1 of Form 511-NR.
              This includes dependents, each spuse, and another exemption for each spouse above the age of 65.

    Standard DeductionS 
    Sources - https://oklahoma.gov/content/dam/ok/en/tax/documents/forms/individuals/current/511-NR-Pkt.pdf (P. 13)
    Summary - Single or Married Filing Separately: $6,350
              Married Filing Jointly or Qualifying Widow(er): $12,700
              Head of Household: $9,350
    '''

doc_capital_gains = '''
    Capital Gains Taxes
    Sources - https://oklahoma.gov/content/dam/ok/en/tax/documents/forms/individuals/current/511-NR-Pkt.pdf (P. 13)
    Summary - Net short-term and long-term capital gains are taxed as ordinary income.
    '''

doc_local = '''
    Local Income Taxes
    Sources - https://oklahoma.gov/content/dam/ok/en/tax/documents/forms/individuals/current/511-NR-Pkt.pdf (P. 13)
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