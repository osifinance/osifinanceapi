def add_doc(value):
    import os
    def _doc(func):
        func.__doc__ = os.path.basename(__file__).title() + value
        return func
    return _doc

doc_income = '''
    Income Taxes
    Sources - https://www.arkansasedc.com/why-arkansas/business-climate/tax-structure/personal-income-tax
    Summary - PERSONAL INCOME TAX RateS For TAX YEAR BEGINNING JANUARY 1, 2022
              Income Tax Rate for Individuals with Net Income of Less Than or Equal to $84,500	 
              $0      - $4,999	0.0%
              $5,000  - $9,999	2.0%
              $10,000 - $14,299	3.0%
              $14,300 - $23,599	3.4%
              $23,600 - $84,500	4.9%
              Income Tax Rate for Individuals with a Net Income Greater Than $84,500	 
              $0      - $4,300	2.0%
              $4,301  - $8,500	4.0%
              $8,501+

    Standard Deduction
    Sources - https://www.dfa.arkansas.gov/images/uploads/incomeTaxOffice/2022_AR1000F_and_AR1000NR_Instructions.pdf (P.14)
    Summary - Married Filing Jointly: $4,540
              All Other Filers: $2,270

    Tax Credits
    Sources - https://www.dfa.arkansas.gov/images/uploads/incomeTaxOffice/2022_AR1000F_FullYearResidentIndividualIncomeTaxReturn.pdf (Line 7a.)
            - https://www.dfa.arkansas.gov/images/uploads/incomeTaxOffice/2022_AR1000F_and_AR1000NR_Instructions.pdf (P.12) 
    Summary - $29 per individual/spouse, dependent, and bonus for each spouse over 65
    '''

doc_capital_gains = '''
    Capital Gains Taxes
    Source - https://www.arkansasedc.com/why-arkansas/business-climate/tax-structure/capital-gains-tax-reduction
    Summary - 50% of net capital gains are deducted, as is any net capital gain in excess of $10M
    '''

doc_local = '''
    Local Income Taxes
    Sources - https://www.dfa.arkansas.gov/images/uploads/incomeTaxOffice/2022_AR1000F_and_AR1000NR_Instructions.pdf (P. 13)
    Summary - No jurisdictions impose additional income taxes

    '''

@add_doc(doc_income+doc_capital_gains+doc_local)
def total(filing_status="single", capital_gains_short=0, capital_gains_long=0, credits_state=0, state_agi=0, income=0, dependents=0, filers_over_65=0):
    return 1


@add_doc(doc_income)
def income(filing_status="single", capital_gains_short=0, capital_gains_long=0, credits_state=0, state_agi=0, income=0, dependents=0, filers_over_65=0):
    return 2


@add_doc(doc_capital_gains)
def capital_gains(filing_status="single", capital_gains_short=0, capital_gains_long=0, state_agi=0, income=0):
    return 3


@add_doc(doc_local)
def local():
    return 4
