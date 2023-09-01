def add_doc(value):
    import os
    def _doc(func):
        func.__doc__ = os.path.basename(__file__).title() + value
        return func
    return _doc

doc_income = '''
    Income Taxes
    Sources - https://portal.ct.gov/-/media/DRS/Forms/2022/Income/2022-CT-1040-Instructions_1222.pdf (Table B)
              https://www.cga.ct.gov/2022/rpt/pdf/2022-R-0108.pdf 
              https://www.cga.ct.gov/current/pub/chap_229.htm#sec_12-703 
    Summary - Connecticut Taxable Income
              Tax Rate    Single and Married Filing Separately   Head of Household        Married Filing Jointly
              3%          $0 to $10,000                          $0 to $16,000             $0 to 20,000 
              5%          $10,001 to $50,000                     $16,001 to $80,000        $20,001 to $100,000
              5.5%        $50,001 to $100,000                    $80,001 to $160,000       $100,001 to $200,000
              6%          $100,001 to $200,000                   $160,001 to $320,000      $200,001 to $400,000
              6.5%        $200,001 to $250,000                   $320,001 to $400,000      $400,001 to $500,000
              6.9%        $250,001 to $500,000                   $400,001 to $800,000      $500,01 to $1,000,000
              6.99%       > $500,000                             > $800,000                > $1,000,000

    Deductions and Credits
    Sources - https://portal.ct.gov/-/media/DRS/Forms/2022/Income/2022-CT-1040-Instructions_1222.pdf
    Summary - Table A - Personal Exemption
              Single      Married Filing Separately        Married Filing Jointly          Head of Household
              $15,000     $12,000                          $24,000                         $19,000
              If AGI < 2 * Exemption, then full amount of exemption is allowed, otherwise the exemption is phased out beginning at 2 * Exemption.
              The following phase out formula applies (the exemption cannot be negative):
              Final Exemption = Exemption - ceiling{(AGI - 2 * Exemption) / 1,000} * 1,000
              
              Table C - 3% Tax Rate Phase-Out Add-Back
              Single                                  Married Filing Separately               Married Filing Jointly                   Head of Household
              AGI < 56,500 : 0                       AGI < 50,250 : 0                       AGI < 100,500 : 0                       AGI < 78,500 : 0
              AGI > 56,500:                           AGI > 50,250:                           AGI > 100,500:                           AGI > 78,500:
              ceiling{(AGI - 56,500) / 5,000} * 20    ceiling{(AGI - 50,250) / 2,500} * 20    ceiling{(AGI - 100,500) / 5,000} * 40    ceiling{(AGI - 78,500) / 4,000} * 32
              max : 200 at 101,500+                  max : 200 at 72,750+                   max 400 at 145,500_                      max 320 at 114,500+
              
              Table D - Tax Recapture
              SIngle and Married Filing Separately        Married Filing Jointly                  Head of Household
              200,000 < AGI < 345,000:                    400,000 < AGI < 690,000:                320,000 < AGI < 552,000:
              celing{(AGI - 200,000)/5,000} * 90          celing{(AGI - 400,000)/10,000} * 180    celing{(AGI - 320,000)/8,000} * 140
              345,000 < AGI < 500,000:                    690,000 < AGI < 1,000,000:              552,000 < AGI < 800,000:
              2,700                                       5,500                                   4,200
              490,000 < AGI < 540,000:                    1,000,000 < AGI < 10,080,000:           800,000 < AGI < 864,000:
              celing{(AGI - 500,000)/5,000} * 50          celing{(AGI - 1,000,000)/10,000} * 100  celing{(AGI - 800,000)/8,000} * 80
              Max Recapture : 3,150 at 540,00+           Max Recapture : 6,300 at 1,080,000+    Max Recapture : 4,920 at 864,000+
              
              Table E - Personal Tax Credits (Percentage of Federal EIC)
              Single and Married Filing Seperately
              Adjusted Gross Income               Amount of Credit
              Over $15,000, but not over $18,800  75%
              Over $18,800, but not over $19,300  70%
              Over $19,300, but not over $19,800  65%
              Over $19,800, but not over $20,300  60%
              Over $20,300, but not over $20,800  55% 
              Over $20,800, but not over $21,300  50%
              Over $21,300, but not over $21,800  45%
              Over $21,800, but not over $22,300  40%
              Over $22,300, but not over $25,000  35%
              Over $25,000, but not over $25,500  30%
              Over $25,500, but not over $26,000  25%
              Over $26,000, but not over $26,500  20%
              Over $26,500, but not over $31,300  15%
              Over $31,300, but not over $31,800  14%
              Over $31,800, but not over $32,300  13%
              Over $32,300, but not over $32,800  12%
              Over $32,800, but not over $33,300  11%
              Over $33,300, but not over $60,000  10%
              Over $60,000, but not over $60,500  9%
              Over $60,500, but not over $61,000  8%
              Over $61,000, but not over $61,500  7%
              Over $61,500, but not over $62,000  6%
              Over $62,000, but not over $62,500  5%
              Over $62,500, but not over $63,000  4%
              Over $63,000, but not over $63,500  3%
              Over $63,500, but not over $64,000  2%
              Over $64,000, but not over $64,500  1%
              Over $64,500                        0%
              
              Married Filing Seperately
              Adjusted Gross Income               Amount of Credit
              Over $12,000, but not over $15,000  75%
              Over $15,800, but not over $15,500  70%
              Over $15,500, but not over $16,000  65%
              Over $16,000, but not over $16,500  60%
              Over $16,500, but not over $17,000  55% 
              Over $17,000, but not over $17,500  50%
              Over $17,500, but not over $18,000  45%
              Over $18,000, but not over $18,500  40%
              Over $18,500, but not over $20,000  35%
              Over $20,000, but not over $20,500  30%
              Over $20,500, but not over $21,000  25%
              Over $21,000, but not over $21,500  20%
              Over $21,500, but not over $25,000  15%
              Over $25,000, but not over $25,500  14%
              Over $25,500, but not over $26,000  13%
              Over $26,000, but not over $26,500  12%
              Over $26,500, but not over $27,000  11%
              Over $27,000, but not over $48,000  10%
              Over $48,000, but not over $48,500  9%
              Over $48,500, but not over $49,000  8%
              Over $49,000, but not over $49,500  7%
              Over $49,500, but not over $50,000  6%
              Over $50,000, but not over $50,500  5%
              Over $50,500, but not over $51,000  4%
              Over $51,000, but not over $51,500  3%
              Over $51,500, but not over $52,000  2%
              Over $52,000, but not over $52,500  1%
              Over $52,500                        0%
              
              Head of Household
              Adjusted Gross Income               Amount of Credit
              Over $19,000, but not over $24,000  75%
              Over $24,000, but not over $24,500  70%
              Over $24,500, but not over $25,000  65%
              Over $25,000, but not over $25,500  60%
              Over $25,500, but not over $26,000  55% 
              Over $26,000, but not over $26,500  50%
              Over $26,500, but not over $27,000  45%
              Over $27,000, but not over $27,500  40%
              Over $27,500, but not over $34,000  35%
              Over $34,000, but not over $34,500  30%
              Over $34,500, but not over $35,000  25%
              Over $35,000, but not over $35,500  20%
              Over $35,500, but not over $44,000  15%
              Over $44,000, but not over $44,500  14%
              Over $44,500, but not over $45,000  13%
              Over $45,000, but not over $45,500  12%
              Over $45,500, but not over $46,000  11%
              Over $46,000, but not over $74,000  10%
              Over $74,000, but not over $74,500  9%
              Over $74,500, but not over $75,000  8%
              Over $75,000, but not over $75,500  7%
              Over $75,500, but not over $76,000  6%
              Over $76,000, but not over $76,500  5%
              Over $76,500, but not over $77,000  4%
              Over $77,000, but not over $77,500  3%
              Over $78,500, but not over $78,000  2%
              Over $78,000, but not over $78,500  1%
              Over $78,500                        0%
              
              Married Filing Jointly
              Adjusted Gross Income                 Amount of Credit
              Over $24,000, but not over $30,000    75%
              Over $30,000, but not over $30,500    70%
              Over $30,500, but not over $31,000    65%
              Over $31,000, but not over $31,500    60%
              Over $31,500, but not over $32,000    55% 
              Over $32,000, but not over $32,500    50%
              Over $32,500, but not over $33,000    45%
              Over $33,000, but not over $33,500    40%
              Over $33,500, but not over $40,000    35%
              Over $40,000, but not over $40,500    30%
              Over $40,500, but not over $41,000    25%
              Over $41,000, but not over $41,500    20%
              Over $41,500, but not over $50,000    15%
              Over $50,000, but not over $50,500    14%
              Over $50,500, but not over $51,000    13%
              Over $51,000, but not over $51,500    12%
              Over $51,500, but not over $52,000    11%
              Over $52,000, but not over $96,000    10%
              Over $96,000, but not over $96,500    9%
              Over $96,500, but not over $97,000    8%
              Over $97,000, but not over $97,500    7%
              Over $97,500, but not over $98,000    6%
              Over $98,000, but not over $98,500    5%
              Over $98,500, but not over $99,000    4%
              Over $99,000, but not over $99,500    3%
              Over $99,500, but not over $100,000   2%
              Over $100,000, but not over $100,500  1%
              Over $100,500                         0%
    '''

doc_capital_gains = '''
    Capital Gains Taxes
    Sources - https://portal.ct.gov/DRS/Publications/TSSNs/TSSN-29#:~:text=An%20individual's%20net%20capital%20gains,portion%20of%20Social%20Security%20benefits.
    Summary - Net capital gains are taxed at a rate of 7%

    Dividend and Interest Taxes
    Sources - https://portal.ct.gov/DRS/Publications/TSSNs/TSSN-29#:~:text=An%20individual's%20net%20capital%20gains,portion%20of%20Social%20Security%20benefits.
    Summary - Dividends and interest income are treated as ordinary income
    '''

doc_local = '''
    Local Income Taxes
    Sources - https://portal.ct.gov/DRS/Individuals/Resident-Income-Tax/Tax-Information
    Summary - No local jurisdictions impose additional income taxes
    '''

@add_doc(doc_income+doc_capital_gains)
def total(filings_status="single", capital_gains_short=0, capital_gains_long=0, credits_state=0, state_agi=0, income=0):
    return 1


@add_doc(filings_status="single", credits_state=0, state_agi=0, income=0)
def income():
    return 2
    

@add_doc(doc_capital_gains)
def capital_gains(capital_gains_short=0, capital_gains_long=0):
    return 3

@add_doc(doc_local)
def local():
    return 4
