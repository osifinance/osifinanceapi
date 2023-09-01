def add_doc(value):
    import os
    def _doc(func):
        func.__doc__ = os.path.basename(__file__).title() + value
        return func
    return _doc

doc_income = '''
    Income Taxes
    Sources - https://www.revenue.alabama.gov/ultraviewer/viewer/basic_viewer/index.html?form=2023/02/22f40.pdf

              https://www.revenue.alabama.gov/faqs/what-is-alabamas-individual-income-tax-rate/
    Summary - For single persons, heads of families, and married persons filing separate returns:
                2% First $500 of taxable income
                $10 + 4% Next $2,500 of taxable income
                $110 + 5% All taxable income over $3,000

                For married persons filing a joint return:
                2% First $1,000 of taxable income
                $20 + 4% Next $5,000 of taxable income
                $220 + 5% All taxable income over $6,000

    Personal Exemption
    Sources - https://www.revenue.alabama.gov/ultraviewer/viewer/basic_viewer/index.html?form=2023/02/22f40.pdf (1-4)
              https://www.nfc.usda.gov/Publications/HR_Payroll/Taxes/Bulletins/2022/Taxes-22-24.htm?taxmap=true (5 c.)
    Summary - $3,000 for Married Filing Jointly or Head of Household
              $1,500 for Single or Married Filing Separately

    Standard Deduction
    Sources - https://www.nfc.usda.gov/Publications/HR_Payroll/Taxes/Bulletins/2022/Taxes-22-24.htm?taxmap=true (5 a.)
    Summary - Single
              If the Amount of Annual Wages Is:           The Amount of the Standard Deduction Is:
              Over $0 but not over $25,999.99             $3,000
              Over $25,999.99 but not over $26,499.99     $2,975
              Over $26,499.99 but not over $26,999.99     $2,950
              Over $26,999.99 but not over $27,499.99     $2,925
              Over $27,499.99 but not over $27,999.99     $2,900
              Over $27,999.99 but not over $28,499.99     $2,875
              Over $28,499.99 but not over $28,999.99     $2,850
              Over $28,999.99 but not over $29,499.99     $2,825
              Over $29,499.99 but not over $29,999.99     $2,800
              Over $29,999.99 but not over $30,499.99     $2,775
              Over $30,499.99 but not over $30,999.99     $2,750
              Over $30,999.99 but not over $31,499.99     $2,725
              Over $31,499.99 but not over $31,999.99     $2,700
              Over $31,999.99 but not over $32,499.99     $2,675
              Over $32,499.99 but not over $32,999.99     $2,650
              Over $32,999.99 but not over $33,499.99     $2,625
              Over $33,499.99 but not over $33,999.99     $2,600
              Over $33,999.99 but not over $34,499.99     $2,575
              Over $34,499.99 but not over $34,999.99     $2,550
              Over $34,999.99 but not over $35,499.99     $2,525
              Over $35,499.99                             $2,500
          
              Married Filing Separately
              If the Amount of Annual Wages Is:           The Amount of the Standard Deduction Is:
              Over $0 but not over $12,999.99             $4,250
              Over $12,999.99 but not over $13,249.99     $4,162
              Over $13,249.99 but not over $13,499.99     $4,074
              Over $13,499.99 but not over $13,749.99     $3,986
              Over $13,749.99 but not over $13,999.99     $3,898
              Over $13,999.99 but not over $14,249.99     $3,810
              Over $14,249.99 but not over $14,499.99     $3,722
              Over $14,499.99 but not over $14,749.99     $3,634
              Over $14,749.99 but not over $14,999.99     $3,546
              Over $14,999.99 but not over $15,249.99     $3,458
              Over $15,249.99 but not over $15,499.99     $3,370
              Over $15,499.99 but not over $15,749.99     $3,282
              Over $15,749.99 but not over $15,999.99     $3,194
              Over $15,999.99 but not over $16,249.99     $3,106
              Over $16,249.99 but not over $16,499.99     $3,018
              Over $16,499.99 but not over $16,749.99     $2,930
              Over $16,749.99 but not over $16,999.99     $2,842
              Over $16,999.99 but not over $17,249.99     $2,754
              Over $17,249.99 but not over $17,499.99     $2,666
              Over $17,499.99 but not over $17,749.99     $2,578
              Over $17,749.99                             $2,500
          
              Married Filing Jointly
              If the Amount of Annual Wages Is:           The Amount of the Standard Deduction Is:
              Over $0 but not over $25,999.99             $8,500
              Over $25,999.99 but not over $26,499.99     $8,325
              Over $26,499.99 but not over $26,999.99     $8,150
              Over $26,999.99 but not over $27,499.99     $7,975
              Over $27,499.99 but not over $27,999.99     $7,800
              Over $27,999.99 but not over $28,499.99     $7,625
              Over $28,499.99 but not over $28,999.99     $7,450
              Over $28,999.99 but not over $29,499.99     $7,275
              Over $29,499.99 but not over $29,999.99     $7,100
              Over $29,999.99 but not over $30,499.99     $6,925
              Over $30,499.99 but not over $30,999.99     $6,750
              Over $30,999.99 but not over $31,499.99     $6,575
              Over $31,499.99 but not over $31,999.99     $6,400
              Over $31,999.99 but not over $32,499.99     $6,225
              Over $32,499.99 but not over $32,999.99     $6,050
              Over $32,999.99 but not over $33,499.99     $5,875
              Over $33,499.99 but not over $33,999.99     $5,700
              Over $33,999.99 but not over $34,499.99     $5,525
              Over $34,499.99 but not over $34,999.99     $5,350
              Over $34,999.99 but not over $35,499.99     $5,175
              Over $35,499.99                             $5,000
          
              Head of Household
              If the Amount of Annual Wages Is:           The Amount of the Standard Deduction Is:
              Over $0 but not over $25,999.99             $5,200
              Over $25,999.99 but not over $26,499.99     $5,065
              Over $26,499.99 but not over $26,999.99     $4,930
              Over $26,999.99 but not over $27,499.99     $4,795
              Over $27,499.99 but not over $27,999.99     $4,660
              Over $27,999.99 but not over $28,499.99     $4,525
              Over $28,499.99 but not over $28,999.99     $4,390
              Over $28,999.99 but not over $29,499.99     $4,255
              Over $29,499.99 but not over $29,999.99     $4,120
              Over $29,999.99 but not over $30,499.99     $3,985
              Over $30,499.99 but not over $30,999.99     $3,850
              Over $30,999.99 but not over $31,499.99     $3,715
              Over $31,499.99 but not over $31,999.99     $3,580
              Over $31,999.99 but not over $32,499.99     $3,445
              Over $32,499.99 but not over $32,999.99     $3,310
              Over $32,999.99 but not over $33,499.99     $3,175
              Over $33,499.99 but not over $33,999.99     $3,040
              Over $33,999.99 but not over $34,499.99     $2,905
              Over $34,499.99 but not over $34,999.99     $2,770
              Over $34,999.99 but not over $35,499.99     $2,635
              Over $35,499.99                             $2,500

    Dependent Deduction
    Sources - https://www.nfc.usda.gov/Publications/HR_Payroll/Taxes/Bulletins/2022/Taxes-22-24.htm?taxmap=true (5 d.)
    Summary - If the Amount of Annual Wages Is:       The Amount Per Dependent Is:
              Over $0 but not over $50,000            $1,000
              Over $50,000 but not over $100,000      $500
              Over $100,000                           $300
    '''

doc_capital_gains = '''
    Capital Gains Taxes
    Sources - https://www.revenue.alabama.gov/individual-corporate/income-to-be-reported-on-the-alabama-income-tax-return/
    Summary - Net short-term and long-term capital gains are taxed as ordinary income.
    '''

doc_local = '''
    Local Income Taxes
    Sources - https://www.almonline.org/TaxRates.aspx
    Summary - County          Tax Rate
              Attalla         2%
              Auburn          1%
              Bear Creek      1%
              Bessemer        1%
              Birmingham      1%
              Brilliant       1%
              Fairfield       1%
              Gadsden         2%
              Glencoe         2%
              Goodwater       0.75%
              Guin            1%
              Hacklebug       1%
              Haleyville      1%
              Hamilton        1%
              Leeds           1%
              Lynn            1%
              Midfield        1%
              Mosses          1%
              Opelika         1.5%
              Rainbow City    2%
              Red Bay         0.5%
              Shorter         1%
              Southside       2%
              Sulligent       1%
              Tuskegee        2%
    '''

@add_doc(doc_income+doc_capital_gains+doc_local)
def total(filing_status="single", county_residence="", capital_gains_short=0, capital_gains_long=0, credits_state=0, state_agi=0, income=0, dependents=0):
    return 1


@add_doc(doc_income+doc_local)
def income(filing_status="single", county_residence="", capital_gains_short=0, capital_gains_long=0, credits_state=0, state_agi=0, income=0, dependents=0):
    return 1


@add_doc(doc_income+doc_local)
def capital_gains(filing_status="single", county_residence="", capital_gains_short=0, capital_gains_long=0, credits_state=0, state_agi=0, income=0, dependents=0):
    return 1


@add_doc(doc_local)
def local(filing_status="single", county_residence="", capital_gains_short=0, capital_gains_long=0, credits_state=0, state_agi=0, income=0, dependents=0):
    return 4