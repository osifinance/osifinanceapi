def add_doc(value):
    import os
    def _doc(func):
        func.__doc__ = os.path.basename(__file__).title() + value
        return func
    return _doc

doc_income ='''
    Income Taxes
    Sources - https://otr.cfo.dc.gov/page/dc-individual-and-fiduciary-income-tax-rates
    Summary - Tax Rates: The tax rates for tax years beginning after 12/31/2021 are:
              If the taxable income is:	The tax is:
              Not over $10,000	4% of the taxable income.
              Over $10,000 but not over $40,000	$400, plus 6% of the excess over $10,000.
              Over $40,000 but not over $60,000	$2,200, plus 6.5% of the excess over $40,000.
              Over $60,000 but not over $250,000	$3,500, plus 8.5% of the excess over $60,000.
              Over $250,000 but not over $500,000	$19,650, plus 9.25% of the excess over $250,000.
              Over $500,000 but not over $1,000,000	$42,775, plus 9.75% of the excess above $500,000.
              Over $1,000,000	$91,525, plus 10.75% of the excess above $1,000,000.

    Deductions
    Sources - https://otr.cfo.dc.gov/page/individual-income-tax-filing-faqs
    SUmmary - Federal deductions apply

    Reciprocal Agreements
    Sources - https://otr.cfo.dc.gov/page/individual-income-special-circumstances-faqs
    Summary - Only D.C. residents pay D.C. taxes
    '''

doc_capital_gains = '''
    Capital Gains Taxes
    Sources - https://otr.cfo.dc.gov/release/district-columbia-tax-rate-changes-effective-october-1-2020
    Summary - Short-term capital gains are taxed as ordinary income.
    '''

doc_local = '''
    Local Income Taxes
    Sources - https://otr.cfo.dc.gov/page/individual-income-tax-filing-faqs
    Summary - No local jurisdictions impose additional income taxes
    '''

@add_doc(doc_income+doc_capital_gains+doc_local)
def total(capital_gains_short=0, capital_gains_long=0, credits_state=0, state_agi=0, income=0):
    return 1


@add_doc(doc_income)
def income(capital_gains_short=0, capital_gains_long=0, credits_state=0, state_agi=0, income=0):
    return 2


@add_doc(doc_capital_gains)
def capital_gains(capital_gains_short=0, capital_gains_long=0, credits_state=0, state_agi=0, income=0):
    return 3


@add_doc(doc_local)
def local():
    return 4