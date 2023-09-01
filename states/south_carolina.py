def add_doc(value):
    import os
    def _doc(func):
        func.__doc__ = os.path.basename(__file__).title() + value
        return func
    return _doc

doc_income = '''
    Income Taxes
    Sources - https://dor.sc.gov/resources-site/lawandpolicy/Advisory%20Opinions/IL22-15.pdf
    Summary - For the 2022 tax year the new tax brackets, indexed for inflation, and tax computations for each bracket are:
              New Tax Brackets for Tax Year 2022      Bracket Amounts for Tax Year 2022       Compute the tax as follows for each bracket amount
              Tax Bracket #1                          $0 to $3,199                            0% times the amount (i.e., exempt from tax)
              Tax Bracket #2                          $3,200 to $16,039                       3% times the amount minus $96
              Tax Bracket #3                          $16,040 and up                          *6.5% times the amount minus $658

    Deductions
    Sources - https://dor.sc.gov/forms-site/Forms/IITPacket_2022.pdf
    Summary - Standard Deduction is same as federal (P. 13)
              Dependent and Age 65+ Deductions are $4,430 per person (P. 3 and 21)

    '''

doc_capital_gains = '''
    Capital Gains Taxes
    Sources - https://www.scstatehouse.gov/code/t12c006.php (SECTION 12-6-1150)
    Summary - 44% of net capital gains are deducted
    '''

doc_local = '''
    Local Income Taxes
    Sources - https://dor.sc.gov/resources-site/lawandpolicy/Advisory%20Opinions/IL22-15.pdf
    Summary - No local jurisdictions impose additional income taxes
    '''

@add_doc(doc_income+doc_capital_gains+doc_local)
def total(filing_status="single", capital_gains_short=0, capital_gains_long=0, credits_state=0, state_agi=0, income=0, dependents=0, filers_over_65=0):
    return 1


@add_doc(doc_income)
def income(filing_status="single", capital_gains_short=0, capital_gains_long=0, credits_state=0, state_agi=0, income=0, dependents=0, filers_over_65=0):
    return 2


@add_doc(doc_capital_gains)
def capital_gains(filing_status="single", capital_gains_short=0, capital_gains_long=0):
    return 3


@add_doc(doc_local)
def local():
    return 4

