def add_doc(value):
    import os
    def _doc(func):
        func.__doc__ = os.path.basename(__file__).title() + value
        return func
    return _doc

doc_income = '''
    Income Taxes
    Sources - https://azdor.gov/forms/individual/form-140-x-y-tables
    Summary - Single or Married Filing Separate
              Taxable Income
              Is over         But not over    Tax Rate
              $0              $28,653         2.55%
              $28,653                         2.98% + $731
      
              Married Filing Joint or Head of Household
              Taxable Income
              Is over         But not over    Tax Rate
              $0              $57,305         2.55%
              $57,305                         2.98% + $1,461

    Standard/Itemized Deductions
    Sources - https://azdor.gov/forms/individual/form-140-x-y-tables
    Summary - Federal deductions apply

    Dependent Credit
    Sources - https://azdor.gov/forms/individual/form-140-x-y-tables
    Summary - $100 per dependent
              Married Filing Joint: $400,000 Threshold
              Otherwise: $200,000 Threshold
              If AGI - Threshold is greater than $19,000, you cannot claim the deduction
              However, if AGI - Threshold > 0, the following formula applies:
              [20 - Ceiling{((AGI - $19,000) / $1,000)}] / 20 * dependent credit
  
              Table V. P. 22
              If AGI - Threshold > 0 :
              $ 1-1,000      .95   $10,001-11,000   .45
              $ 1,001-2,000  .90   $11,001-12,000   .40
              $ 2,001-3,000  .85   $12,001-13,000   .35
              $ 3,001-4,000  .80   $13,001-14,000   .30
              $ 4,001-5,000  .75   $14,001-15,000   .25
              $ 5,001-6,000  .70   $15,001-16,000   .20
              $ 6,001-7,000  .65   $16,001-17,000   .15
              $ 7,001-8,000  .60   $17,001-18,000   .10
              $ 8,001-9,000  .55   $18,001-19,000   .05
              $ 9,001-10,000 .50   $19,001+         .00

    Reciprocal Agreements
    Sources - https://azdor.gov/businesses-arizona/withholding-tax/withholding-exceptions
    Summary - California, Indiana, Oregon, and Virginia
    '''

doc_capital_gains = '''
    Capital Gains Taxes
    Sources - https://azdor.gov/individuals/income-tax-filing-assistance/identifying-other-taxable-income#:~:text=In%20regards%20to%20capital%20gains,the%20individual's%20regular%20tax%20rate.
    Summary - Short-term capital gains are taxed as ordinary income.
    '''

doc_local = '''
    Local Income Taxes
    No local jurisdictions impose additional income taxes
    '''

@add_doc(doc_income+doc_capital_gains+doc_local)
def total(filing_status="single", capital_gains_short=0, capital_gains_long=0, state_agi=0, income=0, dependents=0, stateDeductions=0, credits_state=0):
    return 1


@add_doc(doc_income)
def income(filing_status="single", capital_gains_short=0, capital_gains_long=0, state_agi=0, income=0, dependents=0, stateDeductions=0, credits_state=0):
    return 2


@add_doc(doc_capital_gains)
def capital_gains(filing_status="single", capital_gains_short=0, capital_gains_long=0, state_agi=0, income=0, dependents=0, stateDeductions=0, credits_state=0):
    return 3


@add_doc(doc_local)
def local():
    return 4
