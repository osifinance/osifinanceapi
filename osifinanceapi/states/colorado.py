def add_doc(value):
    import os
    def _doc(func):
        func.__doc__ = os.path.basename(__file__).title() + value
        return func
    return _doc

doc_income = '''
    Income Taxes
    Sources -https://leg.colorado.gov/agencies/legislative-council-staff/individual-income-tax%C2%A0
    Summary - Flat Rate: 4.55%

    Deductions
    Sources - https://leg.colorado.gov/agencies/legislative-council-staff/individual-income-tax%C2%A0
    Summary - None
    '''

doc_capital_gains = '''
    Capital Gains Taxes
    Sources - https://tax.colorado.gov/sites/tax/files/documents/ITT_Capital_Gain_Subtraction_Feb_2022.pdf
    Summary - Net short-term capital gains are taxed at the same rate as ordinary income.
    '''

doc_local = '''
    Local Income Taxes
    Sources - https://www.auroragov.org/business_services/taxes/occupational_privilege_tax
            https://www.denvergov.org/Government/Agencies-Departments-Offices/Agencies-Departments-Offices-Directory/Department-of-Finance/Our-Divisions/Treasury/Business-Tax-Information#:~:text=Occupational%20privilege%20tax,-%28show%20below%29&text=Each%20taxable%20employee%20is%20liable,month%20for%20each%20taxable%20employee.
            https://www.glendale.co.us/355/Occupational-Privilege-Tax
            https://www.greenwoodvillage.com/1220/Occupational-Privilege-Tax-OPT
            https://ci.sheridan.co.us/288/Occupational-Privilege-Tax
    Summary - Aurora: $2 per month
            Denver: $5.75 per month
            Glendale: $5 per month    
            Greenwood Village: $2 per month
            Sheridan: $3 per month
    '''

@add_doc(doc_income+doc_capital_gains+doc_local)
def total(credits_state=0, county_residence="", capital_gains_short=0, capital_gains_long=0, state_agi=0, income=0):
    return 1


@add_doc(doc_income)
def income(credits_state=0, county_residence="", capital_gains_short=0, capital_gains_long=0, state_agi=0, income=0):
    return 2


def capital_gains(doc_capital_gains):
    return 3


@add_doc(doc_local)
def local(county_residence=""):
    return 4