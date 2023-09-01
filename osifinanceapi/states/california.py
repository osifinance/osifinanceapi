def add_doc(value):
    import os
    def _doc(func):
        func.__doc__ = os.path.basename(__file__).title() + value
        return func
    return _doc

doc_income = '''
    Income Taxes
    Sources - https://www.ftb.ca.gov/forms/2022/2022-540-tax-rate-schedules.pdf
    Summary - Single or Married Filing Separately
              Taxable Income
              Is over      But not over     Taxes                Of the amount over
              $0           $10,099          1.00%                $0
              $10,099      $23,942          $100.99    + 2.0%    $10,099
              $23,942      $37,788          $377.85    + 4.0%    $23,942
              $37,788      $52,455          $931.69    + 6.0%    $37,788
              $52,455      $66,295          $1,811.71  + 8.0%    $52,455
              $66,295      $338,639         $2,918.91  + 9.3%    $66,295
              $338,639     $406,364         $28,246.9  + 10.3%   $338,639
              $406,364     $677,275         $35,222.58 + 11.3%   $406,364
              $677,275                      $65,835.52 + 12.3%   $677,275
                                                                                  
              Married Filing Jointly or Qualifying Surviving Spouse                                                                                                                                     
              Taxable Income
              Is over      But not over     Taxes                 Of the amount over
              $0           $20,198          1.00%                 $0
              $20,198      $47,884          $201.98     + 2.0%    $20,198
              $47,884      $75,576          $755.7      + 4.0%    $47,884
              $75,576      $104,910         $1,863.38   + 6.0%    $75,576
              $104,910     $132,590         $3,623.42   + 8.0%    $104,910
              $132,590     $677,278         $5,837.82   + 9.3%    $132,590
              $677,278     $812,728         $56,493.8   + 10.3%   $677,278 
              $812,728     $1,354,550       $35,222.58  + 11.3%   $812,728
              $1,354,550                    $131,671.04 + 12.3%   $1,354,550     
                                                                                  
              Head of Househodld
              Taxable Income
              Is over      But not over     Taxes                Of the amount over
              $0           $20,212          1.00%                $0
              $20,212      $47,887          $202.12    + 2.0%    $20,212
              $47,887      $61,730          $755.62    + 4.0%    $47,887
              $61,730      $76,397          $1,309.34  + 6.0%    $61,730
              $76,397      $90,240          $2,189.36  + 8.0%    $76,397
              $90,240      $460,547         $3,296.8   + 9.3%    $90,240
              $460,547     $552,658         $37,735.35 + 10.3%   $460,547
              $552,658     $921,095         $47,222.78 + 11.3%   $552,658
              $921,095                      $88,856.16 + 12.3%   $677,275                                                                

    Deductions
    Sources - https://www.ftb.ca.gov/file/personal/deductions/index.html
    Summary - Single or Married Filing Separately: $5,202
            - Married Filing Jointly, Head of Househodld, or Qualifying Surviving Spouse: $10,404

    Earned Income Tax Credit
    Sources - https://www.ftb.ca.gov/about-ftb/newsroom/caleitc/eligibility-and-credit-information.html
    Summary - 2022 CalEITC
              qualifying children	California maximum income	CalEITC(up to)	YCTC (up to)	FYTC (up to)   Federal EITC (up to)
              None	                $30,000	                    $275	        $0	            $1,083	       $560
              1	                    $30,000	                    $1,843	        $1,083	        $1,083	       $3,733
              2	                    $30,000	                    $3,037	        $1,083	        $1,083	       $6,164
              3 or more	            $30,000	                    $3,417	        $1,083	        $1,083	       $6,935
        '''

doc_capital_gains = '''
    Capital Gains Taxes
    Sources - https://www.ftb.ca.gov/file/personal/income-types/capital-gains-and-losses.html#:~:text=California%20does%20not%20have%20a,are%20taxed%20as%20ordinary%20income.
    Summary - Net short-term and long-term capital gains are taxed as ordinary income.
    '''

doc_local = '''
    Local Income Taxes
    Sources - https://www.ftb.ca.gov/file/personal/
    Summary - No jurisditions impose local income taxes on employees or individuals
    '''


@add_doc(doc_income+doc_capital_gains+doc_local)
def total(filing_status="single", capital_gains_short=0, capital_gains_long=0, credits_state=0, state_agi=0, income=0):
    return 1

@add_doc(doc_income)
def income(filing_status="single", capital_gains_short=0, capital_gains_long=0, credits_state=0, state_agi=0, income=0):
    return 2
    
@add_doc(doc_capital_gains)
def capital_gains(filing_status="single", capital_gains_short=0, capital_gains_long=0, credits_state=0, state_agi=0, income=0, dependents=0, filers_over_65=0):
    return 3

@add_doc(doc_local)
def local():
    return 4