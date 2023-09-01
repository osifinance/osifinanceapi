def add_doc(value):
    import os
    def _doc(func):
        func.__doc__ = os.path.basename(__file__).title() + value
        return func
    return _doc

doc_income = '''
    Income Taxes
    Sources - https://www.tax.ny.gov/forms/html-instructions/2022/it/it201i-2022.htm#nys-tax-rate-schedule
    Summary -   Married filing jointly or qualifying surviving spouse
                over	    but not over            The tax is 
                $0	        $17,150			        4%
                $17,150	    $23,600	                $686       plus 4.5%  of the excess over $17,150
                $23,600	    $27,900	                $976       plus 5.25% of the excess over $23,600
                $27,900	    $161,550	            $1,202     plus 5.85% of the excess over $27,900
                $161,550	$323,200	            $9,021	   plus 6.25% of the excess over $161,550
                $323,200	$2,155,350	            $19,124	   plus 6.85% of the excess over $323,200
                $2,155,350	$5,000,000	            $144,626   plus 9.65% of the excess over $2,155,350
                $5,000,000	$425,000,000	        $419,135   plus 10.3% of the excess over $5,000,000
                $25,000,000		                    $2,479,135 plus 10.9% of the excess over $25,000,000
 
                Single or married filing separately
                over	    but not over            The tax is:
                $0	        $8,500			        4%
                $8,500	    $11,700	                $340	   plus	4.5%  of the excess over $8,500
                $11,700	    $13,900	                $484	   plus	5.25% of the excess over $11,700
                $13,900	    $80,650	                $600	   plus	5.85% of the excess over $13,900
                $80,650	    $215,400	            $4,504	   plus	6.25% of the excess over $80,650
                $215,400	$1,077,550	            $12,926	   plus	6.85% of the excess over $215, 400
                $1,077,550	$5,000,000	            $71,984	   plus	9.65% of the excess over $1,077,550
                $5,000,000	$25,000,000	            $450,500   plus	10.3% of the excess over $5,000,000
                $25,000,000	            	        $2,510,500 plus	10.9% of the excess over $25,000,000

                Head of household
                over	    but not over            The tax is:
                $0	        $12,800			        4%
                $12,800	    $17,650	                $512	   plus	4.5%  of the excess over $12,800
                $17,650	    $20,900	                $730       plus	5.25% of the excess over $17,650
                $20,900	    $107,650	            $901	   plus	5.85% of the excess over $20,900
                $107,650	$269,300                $5,976	   plus	6.25% of the excess over $107,650
                $269,300	$1,616,450	            $16,079	   plus	6.85% of the excess over $269,300
                $1,616,450	$5,000,000	            $108,359   plus	9.65% of the excess over $1,616,450
                $5,000,000	$25,000,000	            $434,871   plus	10.3% of the excess over $5,000,000
                $25,000,000		                    $2,494,871 plus	10.9% of the excess over $25,000,000

    Standard Deduction
    Sources - https://www.tax.ny.gov/forms/html-instructions/2022/it/it201i-2022.htm#nys-tax-rate-schedule
    Summary - Single and dependent	                        $3,100
              Single and independent	                    $8,000
              Married filing joint return	                $16,050
              Married filing separate return	            $8,000
              Head of household (with qualifying person)	$11,200
              Qualifying surviving spouse 	                $16,050

    Dependent Exemption
    Sources - https://www.tax.ny.gov/forms/html-instructions/2022/it/it201i-2022.htm#nys-tax-rate-schedule
    Summary - $1,000 PER Dependent
    '''

doc_capital_gains = '''
    Capital Gains Taxes
    Sources - https://www.tax.ny.gov/pit/
    Summary - Net short-term and long-term capital gains are taxed as ordinary income.
    '''

doc_local = '''
    Local Income Taxes
    Sources - https://www.tax.ny.gov/pit/file/nonresident-faqs.htm
    Summary - Only for residents, not workers

              Yonkers
              https://www.tax.ny.gov/forms/html-instructions/2022/it/it201i-2022.htm#yonkers-tax-rate-schedule
              16.75% OF STATE INCOME TAX
      
              New York City
              https://www.tax.ny.gov/forms/html-instructions/2022/it/it201i-2022.htm#nyc-tax-rate-schedule
      
              Married filing jointly and qualifying surviving spouse
              over	        but not over    the tax is
              $0	        $21,600			3.078%
              $21,600	    $45,000	        $665 + 3.762% of the excess over $21,600
              $45,000	    $90,000	        $1,545 + 3.819%	of the excess over $45,000
              $90,000	                    $3,264 + 3.876%	of the excess over $90,000
      
              Single and married filing separately
              over	       but not over    the tax is
              $0	        $12,000			3.078%
              $12,000	    25,000	        $369 + 3.762% of the excess over $12,000
              $25,000	    $50,000	        $858 + 3.819% of the excess over $25,000
              $50,000		                $1,813 + 3.876%	of the excess over $50,000
      
              Head of household
              over	        but not over    the tax is:
              $0	        $14,400			3.078%	of line 47	
              $14,400     	$30,000	        $443 + 3.762% of the excess over $14,400
              $30,000	    $60,000	        $1,030 + 3.819%	of the excess over $30,000
              $60,000	                    $2,176 + 3.876%	of the excess over $60,000
    '''

@add_doc(doc_income+doc_capital_gains+doc_local)
def total(filing_status="single", county_residence="", capital_gains_short=0, capital_gains_long=0, credits_state=0, state_agi=0, income=0, dependents=0):
    return 1


@add_doc(doc_income)
def income(filing_status="single", county_residence="", capital_gains_short=0, capital_gains_long=0, credits_state=0, state_agi=0, income=0, dependents=0):
    return 2
    

@add_doc(doc_capital_gains)
def capital_gains(filing_status="single", county_residence="", capital_gains_short=0, capital_gains_long=0, credits_state=0, state_agi=0, income=0, dependents=0):
    return 3


@add_doc(doc_local)
def local(filing_status="single", county_residence="", capital_gains_short=0, capital_gains_long=0, credits_state=0, state_agi=0, income=0, dependents=0):
    return 4

