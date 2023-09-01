def add_doc(value):
    import os
    def _doc(func):
        func.__doc__ = os.path.basename(__file__).title() + value
        return func
    return _doc

doc_income = '''
    Income Taxes
    Sources - https://www.revenue.state.mn.us/minnesota-income-tax-rates-and-brackets
    Summary -  2023     Married Filing Jointly      	        Married Filing Seperate​Ly
               Rate     More Than​	     But not more than​	      More than​	    But not more than​
               5.35%	$0	            $43,950	                $0	             $21,975
               6.80%	$43,950	        $174,610	​            $21,975    	  $87,305
               7.85%	$174,610	    $304,970 ​	             $87,305	      $152,485
               9.85%	$304,970	 	                        $152,485	 


              ​	         Head of Household​	        	          Single	
              Rate      More Than​	    But not more than​        More than​	But not more than​
              5.35%​	 $0	            $37,010	                 $0	          $30,070
              6.80%	    $37,010	       $148,730	                $30,070	     $98,760
              7.85%	    $148,730       $243,720	                $98,760	     $183,340
              9.85%	    $243,720	                            $183,340

    Dependent Deductions
    Sources - https://www.revenue.state.mn.us/child-and-dependent-care-credit
              https://www.revenue.state.mn.us/dependent-exemptions
    Summary - $4,950 deduction per dependent


    Standard Deduction
    Sources - https://www.revenue.state.mn.us/minnesota-standard-deduction
    Summary - Single or Married Filing Seperately: $12,900
              Married Filing Jointly or Qualifying Surviving Spouse: $25,800
              Head of Household: $19,400

    Reciprocal Agreements
    Sources - https://mn.gov/mmb/assets/mwr_form_tcm1059-128581.pdf
    Summary - North Dakota and Michigan
    '''

doc_capital_gains = '''
    Capital Gains Taxes
    Sources - https://www.revenue.state.mn.us/individual-income-tax
    Summary - Net short-term and long-term capital gains are taxed as ordinary income.
    '''

doc_local = '''
    Local Income Taxes
    Sources - https://www.revenue.state.mn.us/individual-income-tax
    Summary - No local jurisdictions impose additional income taxes
    '''


@add_doc(doc_income+doc_capital_gains+doc_local)
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