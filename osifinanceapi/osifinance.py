import requests


class Osifinance(object):
    def __init__(self, api_key=None, filing_status=None, federal_agi=None, state_agi=None, credits_federal=None, credits_state=None, capital_gains_long=None, capital_gains_short=None, state_residence=None, state_occupation=None, county_residence=None, county_occupation=None, pay_periods=None, income=None, dependents=None, filers_over_65=None, age_over_65=None, age_over_67=None, traditional_401k_contributions=None, traditional_ira_contributions=None, monthly_benefits=None):
        '''
        Initialize the Osifinance class that provides default variables and functions to query the OSI Finance API. You need to specify a valid
        API key in one of 3 ways: pass the string via api_key, or set api_key_file to a file with the api key in the
        first line, or set the environment variable 'OSI_API_KEY' to the value of your api key. You can sign up for a
        free api key on the OSI Finance website at https://osifinance.com/getstarted/
        '''
        if api_key is not None:
            self.api_key = api_key
      
        if self.api_key is None:
            import textwrap
            raise ValueError(textwrap.dedent('''
                    You need to set a valid API key. You can set it in 3 ways:
                    pass the string with api_key, or set api_key_file to a
                    file with the api key in the first line, or set the
                    environment variable 'OSI_API_KEY' to the value of your
                    api key. You can sign up for a free api key on the OSI Finance
                    website at https://osifinance.com/getstarted/'''))
        
        if filing_status:
            self.filing_status = filing_status
        if federal_agi:
            self.federal_agi = federal_agi
        if state_agi:
            self.state_agi = state_agi
        if credits_federal:
            self.credits_federal = credits_federal
        if credits_state:
            self.credits_state = credits_state
        if capital_gains_long:
            self.capital_gains_long = capital_gains_long
        if capital_gains_short:
            self.capital_gains_short = capital_gains_short
        if state_residence:
            self.state_residence = state_residence
        if state_occupation:
            self.state_occupation = state_occupation
        if county_residence:
            self.county_residence = county_residence
        if county_occupation:
            self.county_occupation = county_occupation
        if pay_periods:
            self.pay_periods = pay_periods
        if income:
            self.income = income
        if dependents:
            self.dependents = dependents
        if filers_over_65:
            self.filers_over_65 = filers_over_65
        if age_over_65:
            self.age_over_65 = age_over_65
        if age_over_67:
            self.age_over_67 = age_over_67
        if traditional_401k_contributions:
            self.traditional_401k_contributions = traditional_401k_contributions
        if traditional_ira_contributions:
            self.traditional_ira_contributions = traditional_ira_contributions
        if monthly_benefits:
            self.monthly_benefits = monthly_benefits
        
        
    def fetch(self, json, path):
        url = f'https://osifinance.com/api/v1/{path}&api_key={self.api_key}'
        r = requests.post(url, json=json)
        return r.json()
    

    def add_doc(state, value):
        def _doc(func):
            func.__doc__ = f'{state} {value}'
            return func
        return _doc
    

    def taxes(self, filing_status='single', federal_agi=0, credits_federal=0, credits_state=0, capital_gains_long=0, capital_gains_short=0, state_residence="", state_occupation="", county_residence="", county_occupation="", pay_periods=None, income=0, dependents=0, filers_over_65=0, age_over_65=False, traditional_401k_contributions=0, traditional_ira_contributions=0):
        '''
        Includes income, FICA, capital gains, and state taxes\n
        Sources can be found in their respective functions.
        ''' 
        json = {
                "filing_status": self.filing_status if self.filing_status else filing_status,
                "capital_gains_long": self.capital_gains_long if self.capital_gains_long else capital_gains_long,
                "capital_gains_short": self.capital_gains_short if self.capital_gains_short else capital_gains_short,
                "credits_federal": self.credits_federal if self.credits_federal else credits_federal,
                "credits_state": self.credits_state if self.credits_state else credits_state,
                "state_residence": self.state_residence if self.state_residence else state_residence,
                "state_occupation": self.state_occupation if self.state_occupation else state_occupation,
                "county_residence": self.county_residence if self.county_residence else county_residence,
                "county_occupation": self.county_occupation if self.county_occupation else county_occupation,
                "pay_periods": self.pay_periods if self.pay_periods else pay_periods,
                }

        # Adjusted Gross Income (federal_agi) = gross income - deductions
        if federal_agi:
            json = dict(json, **{"federal_agi": federal_agi})
        
        # Calculates federal_agi for you by determining deductions
        else:
            json = dict(json, **{
                    "income": self.income if self.income else income,
                    "dependents": self.dependents if self.dependents else dependents,
                    "filers_over_65": self.filers_over_65 if self.filers_over_65 else filers_over_65,
                    "age_over_65": self.age_over_65 if self.age_over_65 else age_over_65,
                    "traditional_401k_contributions": self.traditional_401k_contributions if self.traditional_401k_contributions else traditional_401k_contributions,
                    "traditional_ira_contributions": self.traditional_ira_contributions if self.traditional_ira_contributions else traditional_ira_contributions
                    })
            
        return self.fetch(json, "taxes/total")


    def taxes_income(self, filing_status='single', federal_agi=0, credits_federal=0, credits_state=0, capital_gains_short=0, state_residence="", state_occupation="", county_residence="", county_occupation="", pay_periods=None, income=0, dependents=0, filers_over_65=0, age_over_65=False, traditional_401k_contributions=0, traditional_ira_contributions=0):
        '''
        Income Taxes
        Sources - https://www.irs.gov/newsroom/irs-provides-tax-inflation-adjustments-for-tax-year-2023
        Summary - For tax year 2023, the top tax rate remains 37% for individual single taxpayers with incomes greater than $578,125 ($693,750 for married couples filing jointly).
                The other rates are:
                35% for incomes over $231,250 ($462,500 for married couples filing jointly);
                32% for incomes over $182,100 ($364,200 for married couples filing jointly);
                24% for incomes over $95,375 ($190,750 for married couples filing jointly);
                22% for incomes over $44,725 ($89,450 for married couples filing jointly);
                12% for incomes over $11,000 ($22,000 for married couples filing jointly).
                The lowest rate is 10% for incomes of single individuals with incomes of $11,000 or less ($22,000 for married couples filing jointly)
        
        Standard Deduction
        Sources - https://www.irs.gov/newsroom/irs-provides-tax-inflation-adjustments-for-tax-year-2023
                https://www.irs.gov/taxtopics/tc551 (Table 7)
        Summary - Under Age 65
                Married Filing Jointly: $27,700
                Head of Household: $20,800
                Single or Married Filing Seperately: $13,850

                Age 65 or Older
                Married Filing Jointly: $30,700
                Head of Household: $23,650
                Single: $15,700
                Married Filing Seperately: $15,350
        '''
        
        json = {
                "filing_status": self.filing_status if self.filing_status else filing_status,
                "capital_gains_short": self.capital_gains_short if self.capital_gains_short else capital_gains_short,
                "credits_federal": self.credits_federal if self.credits_federal else credits_federal,
                "credits_state": self.credits_state if self.credits_state else credits_state,
                "state_residence": self.state_residence if self.state_residence else state_residence,
                "state_occupation": self.state_occupation if self.state_occupation else state_occupation,
                "county_residence": self.county_residence if self.county_residence else county_residence,
                "county_occupation": self.county_occupation if self.county_occupation else county_occupation,
                "pay_periods": self.pay_periods if self.pay_periods else pay_periods,
                }

        # Adjusted Gross Income (federal_agi) = gross income - deductions
        if federal_agi:
            json = dict(json, **{"federal_agi": federal_agi})
        
        # Calculates federal_agi for you by determining deductions
        else:
            json = dict(json, **{
                    "income": self.income if self.income else income,
                    "pay_periods": self.pay_periods if self.pay_periods else pay_periods,
                    "dependents": self.dependents if self.dependents else dependents,
                    "filers_over_65": self.filers_over_65 if self.filers_over_65 else filers_over_65,
                    "age_over_65": self.age_over_65 if self.age_over_65 else age_over_65,
                    "traditional_401k_contributions": self.traditional_401k_contributions if self.traditional_401k_contributions else traditional_401k_contributions,
                    "traditional_ira_contributions": self.traditional_ira_contributions if self.traditional_ira_contributions else traditional_ira_contributions
                    })
            
        self.fetch(json, "taxes/income")


    def taxes_capital_gains(self, filing_status='single', capital_gains_long=0, capital_gains_short=0, state_residence="", county_residence="", federal_agi=0, state_agi=0, income=0, dependents=0, filers_over_65=0, age_over_65=False, traditional_401k_contributions=0, traditional_ira_contributions=0, only_federal=False, only_state=False):
        '''
        Federal Capital Gains Taxes (See respective state functions for state capital gains taxes)
        Sources - https://www.irs.gov/taxtopics/tc409
        Summary - Rate      Married Filing Jointly    Single                    Head of Household 
                0%        Up to $83,350             Up to $41,675             Up to $55,800
                15%       $83,350 - $517,200        $41,675 - $459,750        $55,800 - $488,500
                20%       In excess of $517,200     In excess of $459,750     In excess of $488,500

        Net Investment Income Tax (NIIT)
        Sources - https://www.irs.gov/taxtopics/tc559
        Summary - 3.8% additional tax on net investment income for taxpayers with modified adjusted gross income (Mfederal_agi) above the following thresholds:
                Married Filing Jointly     Single or Head of Household     Married Filing Separately
                Thresholds:   $250,000                        $200,000                      $125,000
        '''
        
        if only_state and only_federal:
            raise ValueError("You can't have both only_state and only_federal set to True")
        
        json = {
                "filing_status": self.filing_status if self.filing_status else filing_status,
                "capital_gains_long": self.capital_gains_long if self.capital_gains_long else capital_gains_long,
                "capital_gains_short": self.capital_gains_short if self.capital_gains_short else capital_gains_short,
                }

        if not only_federal:
            json = dict(json, **{
                    "state_residence": self.state_residence if self.state_residence else state_residence,
                    "county_residence": self.county_residence if self.county_residence else county_residence,
                    })
            
            if state_agi:
                json = dict(json, **{"state_agi": federal_agi})
        
        elif not only_state:
            # Adjusted Gross Income (AGI) = gross income - deductions
            if federal_agi:
                json = dict(json, **{"federal_agi": federal_agi})

        # Calculates federal or state AGI for you by determining deductions
        if not federal_agi and not state_agi:
            json = dict(json, **{
                    "income": self.income if self.income else income,
                    "dependents": self.dependents if self.dependents else dependents,
                    "filers_over_65": self.filers_over_65 if self.filers_over_65 else filers_over_65,
                    "age_over_65": self.age_over_65 if self.age_over_65 else age_over_65,
                    "traditional_401k_contributions": self.traditional_401k_contributions if self.traditional_401k_contributions else traditional_401k_contributions,
                    "traditional_ira_contributions": self.traditional_ira_contributions if self.traditional_ira_contributions else traditional_ira_contributions
                    })
        
        url = "taxes/capital_gains"
        
        if only_state:
            url += f"/{state_residence}"

        elif only_federal:
            url += "/federal"
    
        return self.fetch(json, url)


    def taxes_fica(self, filing_status='single', salary=0):
        '''
        Federal Insurance Contributions Act (FICA)
        Sources - https://www.ssa.gov/oact/cola/cbb.html
        Summary - Social Security: 6.2% of gross salary up to $160,200
                Medicare - 1.45% of gross salary

        Additional 0.9% Medicare Tax
        Sources - https://www.irs.gov/taxtopics/tc560#:~:text=A%200.9%25%20Additional%20Medicare%20Tax,%24200%2C000%20for%20all%20other%20taxpayers.
        Summary - Income over the following thresholds
                Married Filing Jointly: $250,000
                Married Filing Seperatly: $125,000
                All Others: $200,000
        '''
        json = {
            "income": salary,
            "filing_status": filing_status
        }

        return self.fetch(json, "taxes/fica")

    def taxes_social_security(self, monthly_benefits=0, filing_status='single', federal_agi=0, state_residence="", county_residence="", pay_periods=None, income=0, capital_gains_short=0, dependents=0, filers_over_65=0, age_over_65=False, traditional_401k_contributions=0, traditional_ira_contributions=0):
        '''
        See social_secrity.portion_taxable and .income for more information.
        This function calculate the amount of benefits subject to income taxes
        and subsequently the amount of taxes paid on those benefits.
        '''
        json = {"pmi": self.monthly_benefits if self.monthly_benefits else monthly_benefits,
                "filing_status": self.filing_status if self.filing_status else filing_status,
                "capital_gains_short": self.capital_gains_short if self.capital_gains_short else capital_gains_short,
                "state_residence": self.state_residence if self.state_residence else state_residence,
                "county_residence": self.county_residence if self.county_residence else county_residence,
                }

        # Adjusted Gross Income (federal_agi) = gross income - deductions
        if federal_agi:
            json = dict(json, **{"federal_agi": federal_agi})
        
        # Calculates federal_agi for you by determining deductions
        else:
            json = dict(json, **{
                    "income": self.income if self.income else income,
                    "pay_periods": self.pay_periods if self.pay_periods else pay_periods,
                    "dependents": self.dependents if self.dependents else dependents,
                    "filers_over_65": self.filers_over_65 if self.filers_over_65 else filers_over_65,
                    "age_over_65": self.age_over_65 if self.age_over_65 else age_over_65,
                    "traditional_401k_contributions": self.traditional_401k_contributions if self.traditional_401k_contributions else traditional_401k_contributions,
                    "traditional_ira_contributions": self.traditional_ira_contributions if self.traditional_ira_contributions else traditional_ira_contributions
                    })

        return "taxes/social_security"


    def credit_savers(self, filing_status='single', contributions=0, federal_agi=0, income=0, capital_gains_short=0, dependents=0, filers_over_65=0, age_over_65=False, traditional_401k_contributions=0, traditional_ira_contributions=0):
        '''
        Saver's Credit
        Sources - https://www.irs.gov/retirement-plans/plan-participant-employee/retirement-savings-contributions-savers-credit
        Summary - You're eligible for the credit if you're:
                1.) Age 18 or older,
                2.) Not claimed as a dependent on another person's return, and
                3.) Not a student.

                The maximum contribution amount that may qualify for the credit is $2,000 ($4,000 if married filing jointly), making the maximum credit $1,000 ($2,000 if married filing jointly).

                Credit Rate	                Married Filing Jointly	    Head of Household	        All Other Filers*
                50% of your contribution	    federal_agi not more than $43,500	federal_agi not more than $32,625	federal_agi not more than $21,750
                20% of your contribution	    $43,501- $47,500	        $32,626 - $35,625	        $21,751 - $23,750
                10% of your contribution	    $47,501 - $73,000	        $35,626 - $54,750	        $23,751 - $36,500
                0% of your contribution	    more than $73,000	        more than $54,750	        more than $36,500
        '''
        json = {
                "filing_status": self.filing_status if self.filing_status else filing_status,
                "contributions": contributions
                }
        
        # Adjusted Gross Income (federal_agi) = gross income - deductions
        if federal_agi:
            json = dict(json, **{"federal_agi": federal_agi})

        # Calculates federal_agi for you by determining deductions
        else:
            json = dict(json, **{
                    "income": self.income if self.income else income,
                    "capital_gains_short": self.capital_gains_short if self.capital_gains_short else capital_gains_short,
                    "dependents": self.dependents if self.dependents else dependents,
                    "filers_over_65": self.filers_over_65 if self.filers_over_65 else filers_over_65,
                    "age_over_65": self.age_over_65 if self.age_over_65 else age_over_65,
                    "traditional_401k_contributions": self.traditional_401k_contributions if self.traditional_401k_contributions else traditional_401k_contributions,
                    "traditional_ira_contributions": self.traditional_ira_contributions if self.traditional_ira_contributions else traditional_ira_contributions
                    })

        return self.fetch(json, "taxes/savers")


    def credit_eic(self, filing_status='single', residence_state="", federal_agi=0, income=0, capital_gains_short=0, dependents=0, filers_over_65=0, age_over_65=False, traditional_401k_contributions=0, traditional_ira_contributions=0): 
        '''
        Earned Income Tax Credit (EIC)
        Sources - https://www.irs.gov/credits-deductions/individuals/earned-income-tax-credit/earned-income-and-earned-income-tax-credit-eitc-tables
                https://sgp.fas.org/crs/misc/R43805.pdf (Graph of credits with the corresponding rates)
                https://www.irs.gov/pub/irs-pdf/p596.pdf (Additional Publications)
                https://www.irs.gov/pub/irs-drop/rp-21-45.pdf (Table with key 2022 values)
        Summary - Find the maximum federal_agi, investment income and credit amounts for tax year 2023.
                Children or               Filing as Single, Head of 
                Relatives Claimed         Household, or Widowed           Filing as Married Filing Jointly
                Zero	                  $17,640                         $24,210
                One	                      $46,560                         $53,120
                Two	                      $52,918                         $59,478
                Three	                  $56,838                         $63,698
                
                Investment income limit: $11,000 or less
                Maximum Credit Amounts
                The maximum amount of credit:
                No qualifying children: $600
                1 qualifying child: $3,995
                2 qualifying children: $6,604
                3 or more qualifying children: $7,430
                
                                    Number of Qualifying Children
                Item                        One         Two         Three+       None 
                Earned Income Amount        $10,980     $15,410     $15,410      $7,320
                Maximum Amount of Credit    $3,733      $6,164      $6,935       $560
                
                (Single,  Surviving Spouse, or  Head of Household)
                Threshold Phaseout Amount   $20,130     $20,130     $20,130       $9,160
                Completed Phaseout  Amount  $43,492     $49,399     $53,057       $16,480
                
                (Married Filing  Jointly)
                Threshold Phaseout  Amount  $26,260     $26,260     $26,260       $15,290
                Completed Phaseout  Amount  $49,622     $55,529     $59,187       $22,610
        '''

        # Adjusted Gross Income (federal_agi) = gross income - deductions
        json = {
                "filing_status": self.filing_status if self.filing_status else filing_status,
                "residence_state": residence_state
                }
        
        if federal_agi:
            json = dict(json, **{"federal_agi": federal_agi})

        # Calculates federal_agi for you by determining deductions
        else:
            json = dict(json, **{
                    "income": self.income if self.income else income,
                    "capital_gains_short": self.capital_gains_short if self.capital_gains_short else capital_gains_short,
                    "dependents": self.dependents if self.dependents else dependents,
                    "filers_over_65": self.filers_over_65 if self.filers_over_65 else filers_over_65,
                    "age_over_65": self.age_over_65 if self.age_over_65 else age_over_65,
                    "traditional_401k_contributions": self.traditional_401k_contributions if self.traditional_401k_contributions else traditional_401k_contributions,
                    "traditional_ira_contributions": self.traditional_ira_contributions if self.traditional_ira_contributions else traditional_ira_contributions
                    })
            
        return self.fetch(json, "taxes/eic")

    def social_security_taxes(self, monthly_benefits=0, filing_status='single', federal_agi=0, state_residence="", county_residence="", pay_periods=None, income=0, capital_gains_short=0, dependents=0, filers_over_65=0, age_over_65=False, traditional_401k_contributions=0, traditional_ira_contributions=0):
        '''
        See social_secrity.portion_taxable and .income for more information.
        This function calculate the amount of benefits subject to income taxes
        and subsequently the amount of taxes paid on those benefits.
        '''
        json = {"pmi": self.monthly_benefits if self.monthly_benefits else monthly_benefits,
                "filing_status": self.filing_status if self.filing_status else filing_status,
                "capital_gains_short": self.capital_gains_short if self.capital_gains_short else capital_gains_short,
                "state_residence": self.state_residence if self.state_residence else state_residence,
                "county_residence": self.county_residence if self.county_residence else county_residence,
                }

        # Adjusted Gross Income (federal_agi) = gross income - deductions
        if federal_agi:
            json = dict(json, **{"federal_agi": federal_agi})
        
        # Calculates federal_agi for you by determining deductions
        else:
            json = dict(json, **{
                    "income": self.income if self.income else income,
                    "pay_periods": self.pay_periods if self.pay_periods else pay_periods,
                    "dependents": self.dependents if self.dependents else dependents,
                    "filers_over_65": self.filers_over_65 if self.filers_over_65 else filers_over_65,
                    "age_over_65": self.age_over_65 if self.age_over_65 else age_over_65,
                    "traditional_401k_contributions": self.traditional_401k_contributions if self.traditional_401k_contributions else traditional_401k_contributions,
                    "traditional_ira_contributions": self.traditional_ira_contributions if self.traditional_ira_contributions else traditional_ira_contributions
                    })

        return "taxes/social_security"


    def social_security_factor(self, age=62, month=0):
        '''
        Benefit factor for early or delayed retirement
        Sources - https://www.ssa.gov/oact/ProgData/ar_drc.html
        Summary - Percentage changes monthly based on birth year
                Minimum Age 62: 70%
                Normal (Full) Retirement Age 67: 100%
                Maximimum Age 70: 124%       
        '''
        json = {
                "age": age,
                "month": month
                }
    
        return self.fetch(json, "social_security/factor")

    def social_security_benefits(self, salary=0, salary_array=False):
        '''
        Average Wage Indexing (AWI) Series
        Sources - https://www.ssa.gov/oact/cola/awiseries.html
                https://www.ssa.gov/oact/cola/cbb.html
                https://www.ssa.gov/oact/COLA/piaformula.html
        Summary - Highest 35 wage-adjusted salaries are used to calculate one's
                Primary Montly Insurance (PMI). The PMI is bent such that higher
                earners receive proportionately less benefits.
        '''
        if salary:
            json = {
                    "salary": salary,
                    }
        else:
            json = {
                    "salary_array": salary_array,
                    }
            
        return self.fetch(json, "social_security/benefits")


    def social_security_poriton_taxable(self, monthly_benefits=0, filing_status="single", state_residence="", county_residence="", federal_agi=0, income=0, capital_gains_short=0, dependents=0, filers_over_65=0, age_over_65=False, traditional_401k_contributions=0, traditional_ira_contributions=0):
        '''
        Portion of Social Security benefits subject to taxation
        Sources - https://www.irs.gov/pub/irs-pdf/p915.pdf
        Summary - Ranges from 0% for those with low Adjusted Gross Income (federal_agi) and 
                Primary Monthly Insurance (PMI) up to a maximum of 85%.
        '''
        json = {
                "monthly_benefits": self.monthly_benefits if self.monthly_benefits else monthly_benefits,
                "filing_status": self.filing_status if self.filing_status else filing_status,
                "state_residence": self.state_residence if self.state_residence else state_residence,
                "county_residence": self.county_residence if self.county_residence else county_residence,
                }
        
        if federal_agi:
            json = dict(json, **{
                    "federal_agi": federal_agi
                    })
        else:
            json = dict(json, **{
                    "income": self.income if self.income else income,
                    "capital_gains_short": self.capital_gains_short if self.capital_gains_short else capital_gains_short,
                    "dependents": self.dependents if self.dependents else dependents,
                    "filers_over_65": self.filers_over_65 if self.filers_over_65 else filers_over_65,
                    "age_over_65": self.age_over_65 if self.age_over_65 else age_over_65,
                    "traditional_401k_contributions": self.traditional_401k_contributions if self.traditional_401k_contributions else traditional_401k_contributions,
                    "traditional_ira_contributions": self.traditional_ira_contributions if self.traditional_ira_contributions else traditional_ira_contributions,
                    })
            
        return self.fetch(json, "social_security/portion_taxable")