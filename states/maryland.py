def add_doc(value):
    import os
    def _doc(func):
        func.__doc__ = os.path.basename(__file__).title() + value
        return func
    return _doc

doc_income = '''
    Income Taxes (2022)
    Sources - https://www.marylandtaxes.gov/individual/income/tax-info/tax-rates.php
    Summary - Taxpayers Filing as Single, Married Filing Separately, Dependent Taxpayers or Fiduciaries	  
              Taxable Net Income	            Maryland Tax	                                              
              $0 - $1,000	                    2.00%	                                                      
              $1,000 - $2,000	                $20 plus 3.00% of the excess over $1,000	                  
              $2,000 - $3,000	                $50 plus 4.00% of the excess over $2,000	                  
              $3,000 - $100,000	                $90 plus 4.75% of the excess over $3,000	                 
              $100,000 - $125,000	            $4,697.50 plus 5.00% of the excess over $100,000	         
              $125,000 - $150,000	            $5,947.50 plus 5.25% of the excess over $125,000	          
              $150,000 - $250,000	            $7,260.00 plus 5.50% of the excess over $150,000	          
              Over $250,000	                    $12,760.00 plus 5.75% of the excess of $250,000	              
  
              Taxpayers Filing Joint Returns, Head of Household, or Qualifying Widows/Widowers	 	 
              Taxable Net Income	           Maryland Tax
              $0 - $1,000	                   2.00%
              $1,000 - $2,000	               $20 plus 3.00% of the excess over $1,000
              $2,000 - $3,000	               $50 plus 4.00% of the excess over $2,000
              $3,000 - $150,000	               $90 plus 4.75% of the excess over $3,000
              $150,000 - $175,000	           $7,072.50 plus 5.00% of the excess over $150,000
              $175,000 - $225,000	           $8,322.50 plus 5.25% of the excess over $175,000
              $225,000 - $300,000	           $10,947.50 plus 5.50% of the excess over $225,000
              Over $300,000	                   $15,072.50 plus 5.75% of the excess over $300,000

    Standard Deduction
    Sources - https://www.marylandtaxes.gov/forms/22_forms/Resident_Booklet.pdf (P. 33, Line 4)
    Summary - 15% of AGI
              Minumums:
                $1,600 for single, married filing separately
                $3,200 for married filing jointly, head of household
              Maximums:
                $2,400 for single, married filing separately
                $4,850 for married filing jointly, head of household

    Reciprocal Agreements
    Sources - https://www.marylandtaxes.gov/forms/Tax_Publications/Administrative_Releases/Income_and_Estate_Tax_Releases/ar_it37.pdf VI.
    Summary - District of Columbia, Virginia, Pennsylvania, and West Virginia
    '''

doc_capital_gains = '''
    Capital Gains Taxes
    Sources - https://www.marylandtaxes.gov/individual/index.php
    Summary - Net short-term and long-term capital gains are taxed as ordinary income.
    '''
doc_local = '''
    Local Income Taxes
    Sources - https://www.marylandtaxes.gov/individual/income/tax-info/tax-rates.php
    Summary - Your local income tax is based on where you live - not where you work
              Local Tax Area	        2023
      
              Allegany County		    .0303
              Anne Arundel County       .0281*
              Baltimore City	    	.0320
              Baltimore County	    	.0320
              Calvert County	    	.0300
              Caroline County	        .0320
              Carroll County	        .0303
              Cecil County	            .0280
              Charles County	        .0303
              Dorchester County	        .0320
              Frederick County	      	.0296**
              Garrett County	        .0265
              Harford County	        .0306
              Howard County	            .0320
              Kent County	            .0320
              Montgomery County	    	.0320
              Prince George's County	.0320
              Queen Anne's County	    .0320
              St. Mary's County	        .0300
              Somerset County	        .0320
              Talbot County	            .0240
              Washington County         .0295
              Wicomico County	        .0320
              Worcester County    	    .0225
              Other       	    	    .0225
      
              * Anne Arundel Co. The local tax rates for taxable year 2023 are as follows:
              (1) .0270 of an individual’s Maryland taxable income of $1 through $50,000; and
              (2) .0281 of an individual’s Maryland taxable income in excess of $50,000.
      
              ** Frederick Co. The local tax rates for taxable year 2023 are as follows:
              (1) .0275 for taxpayers with Maryland taxable income of $100,000 or less and a filing status of married filing joint, head of household, and qualifying widow(er) with dependent child;
              (2) .0275 for taxpayers with Maryland taxable income of $50,000 or less and a filing status of single, married filing separately, and dependent; and
              (3) .0296 for all other taxpayers.'''

@add_doc(doc_income+doc_local)
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