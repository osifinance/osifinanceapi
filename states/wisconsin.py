def add_doc(value):
    import os
    def _doc(func):
        func.__doc__ = os.path.basename(__file__).title() + value
        return func
    return _doc

doc_income = '''
    Income Taxes
    Sources - https://www.revenue.wi.gov/TaxForms2023/2023-Form1-ES-Inst.pdf
    Summary - For single, head of household, estates, and trusts with taxable income:
                over	    but not over	2022 tax is 	    of the amount over
                $0	        $13,810	        3.54%	            $0
                $13,810     $27,630	        $451.70 + 4.65%	    $13,810
                $27,630	    $304,170	    $1,045.04 + 5.3%	$27,630
                $304,170                  	$14,582.83 + 7.65%	$304,170

                For married taxpayers filing a joint return with taxable income:
                over	    but not over	2022 tax is	        of the amount over
                $0	        $18,420         3.54%	            $0
                $18,420     $36,840         $602.15 + 4.65%	    $18,420
                $36,840     $405,550        $1,393.58 + 5.3%	$36,840
                $405,550                    $19,443.79 + 7.65%	$405,550

                For married taxpayers filing separate returns with taxable income:
                over	    but not over	2022 tax is	        of the amount over
                $0	        $9,210          3.54%	            $0      
                $9,210      $18,420         $301.25 + 4.65% 	$9,210
                $18,420     $187,300	    $696.50 + 5.3%	    $18,420
                $202,780                    $9,721.87 + 7.65%	$202,780

    Standard Deduction
    Sources - https://www.revenue.wi.gov/TaxForms2023/2023-Form1-ES-Inst.pdf
    Summary - Single
              over        but not over    deduction
              $0          $18,399 	      $12,760
              $18,399     $124,733 	      $12,760 - 12% of the amount over $18,400
              $124,733                    $0
  
              Head of Household
              over        but not over    deduction
              $0          $18,399 	      $16,840
              $18,399     $53,778 	      $16,840 - 22.515% of the amount over $18,400
              $53,778     $124,733 	      $12,760 - 12% of the amount over $18,400
              $124,733                    $0
  
              Married Filing Jointly
              over        but not over    deduction
              $0          $26,549 	      $23,620
              $26,549     $124,733 	      $23,620 - 19.778% of the amount over $26,550
              $145,976                    $0
  
              Married Filing Separately
              over        but not over    deduction
              $0          $12,599 	      $11,220
              $12,599     $69,330 	      $11,220 - 19.778% of the amount over $12,600
              $69,330                     $0

    Exemptions
    Sources - https://www.revenue.wi.gov/TaxForms2023/2023-Form1-ES-Inst.pdf
    Summary - $700 for yourself, $700 for your spouse if filing a joint return, and $700 for each dependent.
              Add $250 to the total if you are 65 years of age or over and, if filing a joint return, add
              $250 if your spouse is 65 years of age or over. Exemptions must also be prorated using the
              same ratio as standard deductions.

    Reciprocal Agreements
    Sources - https://www.revenue.wi.gov/Pages/FAQS/pcs-work.aspx
    Summary - Illinois, Indiana, Kentucky, and Michigan
    '''

doc_capital_gains = '''
    Capital Gains Taxes 
    Sources - https://www.revenue.wi.gov/Dor%20Publications/pb103.pdf (P. 4)
    Summary - 30% of long term gains are deducted, but all gains are treated as ordinary income
    '''

doc_local = '''
    Local Income Taxes
    Sources - https://www.revenue.wi.gov/Pages/FAQS/pcs-work.aspx
    Summary - No local jurisdictions impose additional income taxes
    '''

@add_doc(doc_income+doc_capital_gains)
def total(filing_status="single", capital_gains_short=0, capital_gains_long=0, credits_state=0, state_agi=0, income=0, dependents=0):
    return 1


@add_doc(doc_income)
def income(filing_status="single", capital_gains_short=0, capital_gains_long=0, credits_state=0, state_agi=0, income=0, dependents=0):
    return 2


@add_doc(doc_capital_gains)
def capital_gains(filing_status="single", capital_gains_short=0, capital_gains_long=0, credits_state=0, state_agi=0, income=0, dependents=0):
    return 3


@add_doc(doc_local)
def local():
    return 4
