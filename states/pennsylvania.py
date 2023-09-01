def add_doc(value):
    import os
    def _doc(func):
        func.__doc__ = os.path.basename(__file__).title() + value
        return func
    return _doc

doc_income = '''    
    Income Taxes
    Sources- https://www.revenue.pa.gov/Tax%20Rates/Pages/default.aspx
    Summary - Flat rate of 3.07%

    Deductions
    Sources - https://www.revenue.pa.gov/FormsandPublications/FormsforIndividuals/PIT/Documents/2022/2022_pa-40in.pdf (P. 9)
    Summary - None

    Reciprocal Agreements
    https://www.revenue.pa.gov/FormsandPublications/FormsforBusinesses/EmployerWithholding/Documents/rev-419.pdf
    Indiana, New Jersey, Maryland, Ohio, and West Virginia
    '''

doc_capital_gains = '''
    Capital Gains Taxes
    Sources - https://www.revenue.pa.gov/FormsandPublications/FormsforIndividuals/PIT/Documents/2022/2022_pa-40in.pdf (P. 15)
    Summary - Net short-term and long-term capital gains are taxed as ordinary income.
    '''

doc_local = '''
    Local Income Taxes
    Sources - https://www.nfc.usda.gov/Publications/HR_Payroll/Taxes/Bulletins/2022/Taxes-22-25.htm
    Summary - City                    Resident Percentage     Nonresident Percentage
              Bethlehem               1.0000                  1.0000
              Bradford                1.0000                  1.0000
              Caln Township           1.0000                  1.0000
              Camp Hill               2.0000                  1.0000
              Carlisle                1.6000                  1.0000
              Erie                    1.6500                  1.6500
              Fairview Township       1.0000                  1.0000
              Greene Township         1.7000                  1.0000
              Gregg Township          1.8000                  1.0000
              Hanover                 1.0000                  1.0000
              Harrisburg              2.0000                  1.0000
              Horsham Township        1.0000                  1.0000
              Kelly Township          2.0000                  1.0000
              Lancaster               1.1000                  1.0000
              Monroeville             1.5000                  1.0000
              Philadelphia            3.7900                  3.4400
              Pittsburgh              3.0000                  1.0000
              Plains Township         1.000                   1.0000
              Reading                 3.6000                  1.0000
              Scranton                3.4000                  1.0000
              South Lebanon Township  1.0000                  0.0000
              South Park Township     1.0000                  1.0000
              Susquehanna Township    1.0000                  1.0000
              Tinicum Township        1.0000                  1.0000
              Tredyffrin Township     0.0000                  0.0000
              Warminster Township     1.0000                  1.0000
              Wilkes-Barre            3.0000                  1.0000
              York Township           1.0000                  1.0000
    '''

@add_doc(doc_income+doc_local)
def total(county_residence="", county_occupation="", capital_gains_short=0, capital_gains_long=0, credits_state=0, state_agi=0, income=0):
    return 1


@add_doc(doc_income)
def income(county_residence="", county_occupation="", capital_gains_short=0, capital_gains_long=0, credits_state=0, state_agi=0, income=0):
    return 2


@add_doc(doc_capital_gains)
def capital_gains(county_residence="", county_occupation="", capital_gains_short=0, capital_gains_long=0, credits_state=0, state_agi=0, income=0):
    return 3


@add_doc(doc_local)
def local(county_residence="", county_occupation="", capital_gains_short=0, capital_gains_long=0, credits_state=0, state_agi=0, income=0):
    return 3