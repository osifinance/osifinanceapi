def add_doc(value):
    import os
    def _doc(func):
        func.__doc__ = os.path.basename(__file__).title() + value
        return func
    return _doc

doc_income = '''
    Income Taxes
    Sources - https://tax.ohio.gov/individual/resources/annual-tax-rates
    Summary - For taxable years beginning in 2022:
              Ohio Taxable Income	Tax Calculation
              0 - $26,050           0.000%
              $26,051 - $46,100     $360.69 + 2.765% of excess over $26,050
              $46,100- $92,150      $915.07 + 3.226% of excess over $46,100
              $92,150 - $115,300    $2,400.64 + 3.688% of excess over $92,150
              more than $115,300    $3,254.41+ 3.990% of excess over $115,300
              Deductions
              
    Exmptions
    Sources - https://tax.ohio.gov/static/forms/ohio_individual/individual/2022/it1040-sd100-instruction-booklet.pdf (Line 4)
    Summary - Per person (spouse and dependents))
              MAGI                Exemption Factor
              < $40,000           $2,400
              $40,001 - $80,000   $2,150
              > $80,000           $1,900

    Credits
    Sources - https://tax.ohio.gov/static/forms/ohio_individual/individual/2022/it1040-sd100-instruction-booklet.pdf
    Summary - Line 3 : Lump Sum Retirement Credit
              Line 4 : Senior Citizen Credit
              Line 12 : Joint filing credit

    Reciprocal Agreements
    Sources - https://tax.ohio.gov/static/forms/employer_withholding/generic/wth_it4nr.pdf
    Summary - The following 5 states have reciprocity agreements with Ohio

    EIC
    Sources - https://tax.ohio.gov/static/forms/ohio_individual/individual/2022/it1040-sd100-instruction-booklet.pdf (Line 13)
    Summary - 30% of federal EIC
    '''
doc_capital_gains = '''
    Capital Gains Taxes
    Sources - https://tax.ohio.gov/static/forms/ohio_individual/individual/2022/it1040-sd100-instruction-booklet.pdf (Line 14)
    Summary - Net short-term and long-term capital gains are taxed as ordinary income.
    '''

doc_local = '''
    Local Income Taxes
    Sources - https://www.ritaohio.com/TaxRatesTable
    Summary - Very long list, see source
    '''

@add_doc(doc_income+doc_capital_gains+doc_local)
def total(filing_status="single", county_residence="", capital_gains_short=0, capital_gains_long=0, credits_state=0, state_agi=0, income=0, dependents=0):
    return 1


@add_doc(doc_income)
def income(filing_status="single", county_residence="", capital_gains_short=0, capital_gains_long=0, credits_state=0, state_agi=0, income=0, dependents=0):
    return 2


@add_doc(doc_income)
def capital_gains(filing_status="single", county_residence="", capital_gains_short=0, capital_gains_long=0, credits_state=0, state_agi=0, income=0, dependents=0):
    return 3

    
@add_doc(doc_local)
def local(filing_status="single", county_residence="", capital_gains_short=0, capital_gains_long=0, credits_state=0, state_agi=0, income=0, dependents=0):
    return 4