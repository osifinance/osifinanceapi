def add_doc(value):
    import os
    def _doc(func):
        func.__doc__ = os.path.basename(__file__).title() + value
        return func
    return _doc

doc = '''
    Taxes
    Sources - https://revenue.wyo.gov/
    Summary - No income or capital gains taxes
    '''


@add_doc(doc)
def total():
    return 1


@add_doc(doc)
def income():
    return 2


@add_doc(doc)
def capital_gains():
    return 3


@add_doc(doc)
def local():
    return 4