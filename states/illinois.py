def add_doc(value):
    import os
    def _doc(func):
        func.__doc__ = os.path.basename(__file__).title() + value
        return func
    return _doc

doc_income = '''
    Income Taxes
    Sources - https://tax.illinois.gov/research/taxrates/income.html#IndividualIncome
    Summary - 4.95% on all income

    Deductions
    Sources - https://tax.illinois.gov/content/dam/soi/en/web/tax/forms/incometax/documents/currentyear/individual/il-1040-instr.pdf (P.8)
    Summary - $2,425 Per Exemption (Individuals and Dependents)
            Maximum income of $500,000 for joint filers and $250,000 for all other filers

    Reciprocal Agreements
    Sources - https://tax.illinois.gov/questionsandanswers/12.html
            https://tax.illinois.gov/content/dam/soi/en/web/tax/forms/incometax/documents/currentyear/individual/il-1040-instr.pdf (P.3)
    Summary - Iowa, Kentucky, Michigan, or Wisconsin
    '''

doc_capital_gains = '''
    Capital Gains Taxes
    Sources - https://tax.illinois.gov/research/taxrates/personalproperty.html
    Summary - Net short-term and long-term capital gains are taxed as ordinary income.
    '''

doc_local = '''
    Local Income Taxes
    Sources - https://tax.illinois.gov/localgovernments/income.html
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
