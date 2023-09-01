def add_doc(value):
    import os
    def _doc(func):
        func.__doc__ = os.path.basename(__file__).title() + value
        return func
    return _doc

doc_income = '''
    Income Taxes
    Sources - https://dor.wa.gov/taxes-rates/income-tax
    Summary - No income tax
    '''

doc_capital_gains = '''
    Capital Gains Taxes
    Sources - https://dor.wa.gov/taxes-rates/other-taxes/capital-gains-tax
    Summary - 7% of net capital gains over $250,000
    '''

doc_local = '''
    Local Income Taxes
    Sources - https://dor.wa.gov/taxes-rates/income-tax
    Summary - No local income taxes
    '''

@add_doc(doc_income+doc_capital_gains+doc_local)
def total(capital_gains_short=0, capital_gains_long=0):
    return 1
    
    
@add_doc(doc_income)
def income():
    return 2


@add_doc(doc_capital_gains)
def capital_gains(capital_gains_short=0, capital_gains_long=0):
    return 3


@add_doc(doc_local)
def local():
    return 4