def add_doc(value):
    import os
    def _doc(func):
        func.__doc__ = os.path.basename(__file__).title() + value
        return func
    return _doc

doc_income = '''
    Income Taxes
    Sources - https://www.in.gov/dor/tax-forms/2022-individual-income-tax-forms/ (IT-40PNR Booklet)
    Summary - 3.23% on all income

    Deductions
    https://www.nfc.usda.gov/Publications/HR_Payroll/Taxes/Bulletins/2022/Taxes-22-32.htm
    $1,000 per spouse, person over 65, and minimum for all dependents
    $1,500 per qualifying dependent

    Reciprocal Agrrements
    Sources- 
    Summary Kentucky, Michigan, Ohio, Pennsylvania, Wisconsin
    '''

doc_capital_gains = '''
    Capital Gains Taxes
    Sources - https://www.in.gov/dor/tax-forms/2022-individual-income-tax-forms/ (IT-40PNR Booklet)
    Summary - Net short-term and long-term capital gains are taxed as ordinary income.
    '''

doc_local = '''
    Local Income Taxes
    Sources - https://www.in.gov/dor/files/2022-county-tax-rates-and-codes.pdf
    Summary - County
              Adams: 1.62%
              Allen: 1.48%
              Bartholomew: 1.75%
              Benton: 1.79%
              Blackford: 1.50%
              Boone: 1.50%
              Brown: 2.52%
              Carroll: 2.27%
              Cass: 2.60%
              Clark: 2.00%
              Clay: 2.25%
              Clinton: 2.25%
              Crawford: 1.00%
              Daviess: 1.50%
              Dearborn: 1.20%
              Decatur: 2.35%
              DeKalb: 2.13%
              Delaware: 1.50%
              Dubois: 1.00%
              Elkhart: 2.00%
              Fayette: 2.37%
              Floyd: 1.35%
              Fountain: 2.10%
              Franklin: 1.50%
              Fulton: 2.38%
              Gibson: 0.70%
              Grant: 2.55%
              Greene: 1.75%
              Hamilton: 1.00%
              Hancock: 1.74%
              Harrison: 1.00%
              Hendricks: 1.50%
              Henry: 1.50%
              Howard: 1.75%
              Huntington: 1.95%
              Jackson: 2.10%
              Jasper: 2.86%
              Jay: 2.45%
              Jefferson: 0.35%
              Jennings: 3.15%
              Johnson: 1.00%
              Knox: 1.00%
              Kosciusko: 1.00%
              LaGrange: 1.65%
              Lake: 1.50%
              LaPorte: 0.95%
              Lawrence: 1.75%
              Madison: 1.75%
              Marion: 2.02%
              Marshall: 1.25%
              Martin: 1.75%
              Miami: 2.54%
              Monroe: 1.35%
              Montgomery: 2.30%
              Morgan: 2.72%
              Newton: 1.00%
              Noble: 1.75%
              Ohio: 1.25%
              Orange: 1.75%
              Owen: 1.30%
              Parke: 2.65%
              Perry: 1.81%
              Pike: 0.75%
              Porter: 0.50%
              Posey: 1.25%
              Pulaski: 3.38%
              Putnam: 2.00%
              Randolph: 2.25%
              Ripley: 1.38%
              Rush: 2.10%
              St. Joseph: 1.75%
              Scott: 2.16%
              Shelby: 1.50%
              Spencer: 0.80%
              Starke: 1.71%
              Steuben: 1.79%
              Sullivan: 0.60%
              Switzerland: 1.00%
              Tippecanoe: 1.10%
              Tipton: 2.60%
              Union: 1.75%
              Vanderburgh: 1.20%
              Vermillion: 1.50%
              Vigo: 2.00%
              Wabash: 2.90%
              Warren: 2.12%
              Warrick: 0.50%
              Washington: 2.00%
              Wayne: 1.50%
              Wells: 2.10%
              White: 2.32%
              Whitley: 1.48%
              Other: 0%
    '''

@add_doc(doc_income+doc_capital_gains+doc_local)
def total(filing_status="single", county_residence="", capital_gains_short=0, capital_gains_long=0, credits_state=0, state_agi=0, income=0, dependents=0, filers_over_65=0):
    return 1


@add_doc(doc_income)
def income(filing_status="single", county_residence="", capital_gains_short=0, capital_gains_long=0, credits_state=0, state_agi=0, income=0, dependents=0, filers_over_65=0):
    return 2


@add_doc(doc_capital_gains)
def capital_gains(filing_status="single", county_residence="", capital_gains_short=0, capital_gains_long=0, credits_state=0, state_agi=0, income=0, dependents=0, filers_over_65=0):
    return 3


@add_doc(doc_local)
def income(county_residence="", state_agi=0, income=0, dependents=0, filers_over_65=0):
    return 4
