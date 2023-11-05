import http.client 
import json
from pandas import DataFrame

class Osifinance:
    '''
    The Osifinance class is the main class that provides default variables and functions to query the OSI Finance API. You need to specify a valid API Key and can then begin using its functions.
    '''

    def __init__(self, api_key=None, filing_status=None, federal_agi=None, state_agi=None, credits_federal=None, credits_state=None, capital_gains_long=None, capital_gains_short=None, state_residence=None, state_occupation=None, county_residence=None, county_occupation=None, pay_periods=None, income=None, birth_year=None, dependents=None, filers_over_65=None, traditional_esp_contributions=None, traditional_ira_contributions=None, roth_ira_contributions=None, pmi=None, election_age=None, election_month=None, years_retirement=None, year_retirement=None, traditional_4_value=None, traditional_ira_value=None, roth_ira_value=None, sep_ira_value=None, employer_salary_percentage_1=None, employer_match_rate_1=None, employer_salary_percentage_2=None, employer_match_rate_2=None, employer_salary_percentage_3=None, employer_match_rate_3=None, employer_salary_percentage_4=None, employer_match_rate_4=None, employer_salary_percentage_5=None, employer_match_rate_5=None):
        '''
        Initialize the Osifinance class that provides default variables and functions to query the OSI Finance API. You need to specify a valid
        API key in one of 3 ways: pass the string via api_key, or set api_key_file to a file with the api key in the
        first line, or set the environment variable 'OSI_API_KEY' to the value of your api key. You can sign up for a
        free api key on the OSI Finance website at https://osifinance.com/signup/.
        
        Parameters:
        api_key : str, optional
            Your OSI Finance API key. If not specified, the value of the environment variable 'OSI_API_KEY' will be used.
        filing_status : str, optional
            Filing status for taxes. Options are 'single', 'married', 'married_seperately', 'head_of_household', 'widow'. Default is 'single'. Source - https://www.irs.gov/newsroom/taxpayers-should-use-the-correct-filing-status-for-accuracy-and-to-avoid-
        federal_agi : int, optional
            Adjusted Gross Income (AGI) for federal taxes. Default is 0. Source -  https://www.irs.gov/e-file-providers/definition-of-adjusted-gross-income, https://www.irs.gov/newsroom/taxpayers-should-know-the-difference-between-standard-and-itemized-deductions
        state_agi : int, optional
            Adjusted Gross Income (AGI) for state taxes. Default is 0.
        credits_federal : int, optional
            Credits for federal taxes. Default is 0. Source - https://www.irs.gov/credits-deductions-for-individuals
        credits_state : int, optional
            Credits for state taxes. Default is 0.
        capital_gains_long : int, optional
            Net long term capital gains. Default is 0.
        capital_gains_short : int, optional
            Net short term capital gains. Default is 0.
        state_residence : str, optional
            State of residence. Default is None, in which case, only Federal taxes will be calculated in the respective functions.
        state_occupation : str, optional
            State of occupation. Default is None, in which case, only Federal taxes will be calculated in the respective functions.
        county_residence : str, optional
            County of residence. Default is None, in which case, only State taxes will be calculated in the respective functions.
        county_occupation : str, optional
            County of occupation. Default is None, in which case, only State taxes will be calculated in the respective functions.
        pay_periods : int, optional
            Number of pay periods. Options are 13, 24, 26, 52. Default is 24.
        income : int, optional
            Gross income. Default is 0.
        birth_year : int, optional
            Year of birth. Options are 1923-2005. Default is 1990.
        dependents : int, optional
            Number of dependents. Default is 0. Source - https://www.irs.gov/faqs/filing-requirements-status-dependents/dependents/dependents-2
        filers_over_65 : int, optional
            Number of filers over 65. Options are 0, 1, 2. Default is 0. 
        traditional_esp_contributions : int, optional
            Traditional employer sponsored plan (401k, 403(b), and 457(b)) contributions. For 401(k)s, the max is 22,500 with an additional 7,500 those 50 or older. Default is 0. Source - https://www.irs.gov/newsroom/401k-limit-increases-to-22500-for-2023-ira-limit-rises-to-6500
        traditional_ira_contributions : int, optional
            Traditional IRA contributions. Max is 6,500 with an additional 1,000 for those 50 or older. Default is 0. Source - https://www.irs.gov/newsroom/401k-limit-increases-to-22500-for-2023-ira-limit-rises-to-6500
        pmi : int, optional
            Monthly Social Security benefits or Primary Monthly Insurance (PMI). Max is 4,555. Default is 0. Source - https://faq.ssa.gov/en-us/Topic/article/KA-01897
        salary: int, optional
            Salary from employer ie. W2. Default is 0.
        
        Additional parameters used in retirement plan optimization function
        apy : float, optional
            Inflation-adjusted Annual percentage yield (APY) of investments. Range from 1-2. Default is 1.04.
        years_retirement : int, optional
            Number of years in retirement. Must be between 0-100. Default is 25.
        year_retirement : int, optional
            Year of retirement. Must be between 2023-2100. Default is 2040.
        retirement_expenses: int, optional
            Retirement expenses. Default is 30,000.
        current_expenses: int, optional
            Current expenses. Default is 40,000.
        traditional_4_value : int, optional
            Value of traditional 401k, 403(b), and 457(b) accounts. Default is 0. Source - https://www.irs.gov/retirement-plans/plan-sponsor/types-of-retirement-plans
        traditional_ira_value : int, optional
            Value of traditional IRA accounts. Default is 0. Source - https://www.irs.gov/retirement-plans/traditional-iras
        roth_ira_value : int, optional
            Value of Roth IRA accounts. Default is 0. Source - https://www.irs.gov/retirement-plans/roth-iras
        employer_salary_percentage (1-5) : float, optional
            Percentage of salary matched by employer. Typically ranges from 1-10%. Range is 0-1. Default is 0. Source - https://www.irs.gov/retirement-plans/plan-participant-employee/401k-resource-guide-plan-
        employer_match_rate (1-5) : float, optional
            Rate at which employer matches contributions. Typically ranges from 25-100%. Range is 0-2. Default is 0. Source - https://www.irs.gov/retirement-plans/plan-participant-employee/401k-resource-guide-plan-
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
                    website at https://osifinance.com/signup/'''))
        

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
        if birth_year:
            self.birth_year = dependents
        if dependents:
            self.dependents = dependents
        if filers_over_65:
            self.filers_over_65 = filers_over_65
        if traditional_esp_contributions:
            self.traditional_esp_contributions = traditional_esp_contributions
        if traditional_ira_contributions:
            self.traditional_ira_contributions = traditional_ira_contributions
        if roth_ira_contributions:
            self.roth_ira_contributions = roth_ira_contributions
        if pmi:
            self.pmi = pmi
        if election_age:
            self.election_age = election_age
        if election_month:
            self.election_month = election_month


    def __fetch__(self, body, path):
        conn = http.client.HTTPSConnection("osifinance.com")

        headers = {'Content-Type': 'application/json'}
        body.update({'api_key': self.api_key, 'python_api': 1})
        payload = json.dumps(body)

        conn.request("POST", f"/api/v1/{path}", body=payload, headers=headers)

        res = conn.getresponse()
        if res.status != 200:
            raise ValueError(f"Error: {res.status} {res.reason}")
        
        data = res.read()
        
        r = json.loads(data.decode("utf-8"))
        
        return DataFrame(r['data']).iloc[:, ::-1]
    

    def all_taxes(self, filing_status='single', federal_agi=0, credits_federal=0, credits_state=0, capital_gains_long=0, capital_gains_short=0, state_residence="Florida", state_occupation="Florida", county_residence="Other", county_occupation="Other", pay_periods=24, income=0, birth_year=1990, dependents=0, filers_over_65=0, traditional_esp_contributions=0, traditional_ira_contributions=0, pmi=0):
        """Income, FICA, capital gains, and state taxes

        Parameters:
        filing_status : str, optional
            Filing status for taxes. Options are 'single', 'married', 'married_seperately', 'head_of_household', 'widow'. Default is 'single'. Source - https://www.irs.gov/newsroom/taxpayers-should-use-the-correct-filing-status-for-accuracy-and-to-avoid-
        federal_agi : int, optional
            Adjusted Gross Income (AGI) for federal taxes. Default is 0. Source -  https://www.irs.gov/e-file-providers/definition-of-adjusted-gross-income, https://www.irs.gov/newsroom/taxpayers-should-know-the-difference-between-standard-and-itemized-deductions
        state_agi : int, optional
            Adjusted Gross Income (AGI) for state taxes. Default is 0.
        credits_federal : int, optional
            Credits for federal taxes. Default is 0. Source - https://www.irs.gov/credits-deductions-for-individuals
        credits_state : int, optional
            Credits for state taxes. Default is 0.
        capital_gains_long : int, optional
            Net long term capital gains. Default is 0.
        capital_gains_short : int, optional
            Net short term capital gains. Default is 0.
        state_residence : str, optional
            State of residence. Default is None.
        state_occupation : str, optional
            State of residence. Default is None.
        county_residence : str, optional
            State of residence. Default is None.
        county_occupation : str, optional
            State of occupation. Default is None.
        pay_periods : int, optional
            Number of pay periods. Options are 13, 24, 26, 52. Default is 24.
        income : int, optional
            Gross income. Default is 0.
        birth_year : int, optional
            Year of birth. Options are 1923-2005. Default is 1990.
        dependents : int, optional
            Number of dependents. Default is 0. Source - https://www.irs.gov/faqs/filing-requirements-status-dependents/dependents/dependents-2
        filers_over_65 : int, optional
            Number of filers over 65. Options are 0, 1, 2. Default is 0. 
        traditional_esp_contributions : int, optional
            Traditional employer sponsored plan (401k, 403(b), and 457(b)) contributions. For 401(k)s, the max is 22,500 with an additional 7,500 those 50 or older. Default is 0. Source - https://www.irs.gov/newsroom/401k-limit-increases-to-22500-for-2023-ira-limit-rises-to-6500
        roth_esp_contributions : int, optional
            Roth employer sponsored plan (401k, 403(b), and 457(b)) contributions. For 401(k)s, the max is 22,500 with an additional 7,500 those 50 or older. Default is 0. Source - https://www.irs.gov/newsroom/401k-limit-increases-to-22500-for-2023-ira-limit-rises-to-6500
        traditional_ira_contributions : int, optional
            Traditional IRA contributions. Max is 6,500 with an additional 1,000 for those 50 or older. Default is 0. Source - https://www.irs.gov/newsroom/401k-limit-increases-to-22500-for-2023-ira-limit-rises-to-6500
        roth_ira_contributions : int, optional
            Roth IRA contributions. Max is 6,500 with an additional 1,000 for those 50 or older. Default is 0. Source - https://www.irs.gov/newsroom/401k-limit-increases-to-22500-for-2023-ira-limit-rises-to-6500
        pmi : int, optional
            Monthly Social Security benefits or Primary Monthly Insurance (PMI). Max is 4,555. Default is 0. Source - https://faq.ssa.gov/en-us/Topic/article/KA-01897
        
        Returns:
        pandas.DataFrame: A DataFrame containing the detailed tax breakdown.

        Note:
        The function fetches the latest tax details from external sources to perform the calculation.
        
        Sources:
        Sources can be found in their respective functions."""

        # Check if the parameters are set upstream in the instance
        data_init = {
                "filing_status": self.filing_status if hasattr(self, 'filing_status') else filing_status,
                "capital_gains_long": self.capital_gains_long if hasattr(self, 'capital_gains_long') else capital_gains_long,
                "capital_gains_short": self.capital_gains_short if hasattr(self, 'capital_gains_short') else capital_gains_short,
                "credits_federal": self.credits_federal if hasattr(self, 'credits_federal') else credits_federal,
                "credits_state": self.credits_state if hasattr(self, 'credits_state') else credits_state,
                "state_residence": self.state_residence if hasattr(self, 'state_residence') else state_residence,
                "state_occupation": self.state_occupation if hasattr(self, 'state_occupation') else state_occupation,
                "county_residence": self.county_residence if hasattr(self, 'county_residence') else county_residence,
                "county_occupation": self.county_occupation if hasattr(self, 'county_occupation') else county_occupation,
                "pay_periods": self.pay_periods if hasattr(self, 'pay_periods') else pay_periods
                }


        # Adjusted Gross Income (federal_agi) = gross income - deductions
        if hasattr(self, 'federal_agi') or federal_agi:
            federal_agi = self.federal_agi if hasattr(self, 'federal_agi') else federal_agi
            data = {"federal_agi": federal_agi}
            data.update(data_init)
        
        # Calculates federal_agi for you by determining deductions
        else:
            data = {
                    "income": self.income if hasattr(self, 'income') else income,
                    "birth_year": self.birth_year if hasattr(self, 'birth_year') else birth_year,
                    "dependents": self.dependents if hasattr(self, 'dependents') else dependents,
                    "filers_over_65": self.filers_over_65 if hasattr(self, 'filers_over_65') else filers_over_65,
                    "traditional_esp_contributions": self.traditional_esp_contributions if hasattr(self, 'traditional_esp_contributions') else traditional_esp_contributions,
                    "traditional_ira_contributions": self.traditional_ira_contributions if hasattr(self, 'traditional_ira_contributions') else traditional_ira_contributions,
                    "pmi": self.pmi if hasattr(self, 'pmi') else pmi
                    }
            data.update(data_init)
            
        return self.__fetch__(data, "all-taxes")


    def income_taxes(self, filing_status='single', federal_agi=0, credits_federal=0, credits_state=0, capital_gains_short=0, state_residence=None, state_occupation=None, county_residence=None, county_occupation=None, pay_periods=24, income=0, dependents=0, birth_year=1990,filers_over_65=0, traditional_esp_contributions=0, traditional_ira_contributions=0, pmi=0):
        """Income Taxes

        Parameters:
        filing_status : str, optional
            Filing status for taxes. Options are 'single', 'married', 'married_seperately', 'head_of_household', 'widow'. Default is 'single'. Source - https://www.irs.gov/newsroom/taxpayers-should-use-the-correct-filing-status-for-accuracy-and-to-avoid-
        federal_agi : int, optional
            Adjusted Gross Income (AGI) for federal taxes. Default is 0. Source -  https://www.irs.gov/e-file-providers/definition-of-adjusted-gross-income, https://www.irs.gov/newsroom/taxpayers-should-know-the-difference-between-standard-and-itemized-deductions
        state_agi : int, optional
            Adjusted Gross Income (AGI) for state taxes. Default is 0.
        credits_federal : int, optional
            Credits for federal taxes. Default is 0. Source - https://www.irs.gov/credits-deductions-for-individuals
        credits_state : int, optional
            Credits for state taxes. Default is 0.
        capital_gains_short : int, optional
            Net short term capital gains. Default is 0.
        state_occupation : str, optional
            State of residence. Default is None.
        county_residence : str, optional
            State of residence. Default is None.
        county_occupation : str, optional
            State of occupation. Default is None.
        pay_periods : int, optional
            Number of pay periods. Options are 13, 24, 26, 52. Default is 24.
        income : int, optional
            Gross income. Default is 0.
        birth_year : int, optional
            Year of birth. Options are 1923-2005. Default is 1990.
        dependents : int, optional
            Number of dependents. Default is 0. Source - https://www.irs.gov/faqs/filing-requirements-status-dependents/dependents/dependents-2
        filers_over_65 : int, optional
            Number of filers over 65. Options are 0, 1, 2. Default is 0. 
        traditional_esp_contributions : int, optional
            Traditional employer sponsored plan (401k, 403(b), and 457(b)) contributions. For 401(k)s, the max is 22,500 with an additional 7,500 those 50 or older. Default is 0. Source - https://www.irs.gov/newsroom/401k-limit-increases-to-22500-for-2023-ira-limit-rises-to-6500
        traditional_ira_contributions : int, optional
            Traditional IRA contributions. Max is 6,500 with an additional 1,000 for those 50 or older. Default is 0. Source - https://www.irs.gov/newsroom/401k-limit-increases-to-22500-for-2023-ira-limit-rises-to-6500
        pmi : int, optional
            Monthly Social Security benefits or Primary Monthly Insurance (PMI). Max is 4,555. Default is 0. Source - https://faq.ssa.gov/en-us/Topic/article/KA-01897

        Returns:
        pandas.DataFrame: A DataFrame containing the detailed tax breakdown.

        Note:
        The function fetches the latest tax details from external sources to perform the calculation.
        
        Sources:
        https://www.irs.gov/newsroom/irs-provides-tax-inflation-adjustments-for-tax-year-2023
        """

        json_init = {
                "filing_status": self.filing_status if hasattr(self, 'filing_status') else filing_status,
                "capital_gains_short": self.capital_gains_short if hasattr(self, 'capital_gains_short') else capital_gains_short,
                "credits_federal": self.credits_federal if hasattr(self, 'credits_federal') else credits_federal,
                "credits_state": self.credits_state if hasattr(self, 'credits_state') else credits_state,
                "state_residence": self.state_residence if hasattr(self, 'state_residence ') else state_residence,
                "state_occupation": self.state_occupation if hasattr(self, 'state_occupation') else state_occupation,
                "county_residence": self.county_residence if hasattr(self, 'county_residence') else county_residence,
                "county_occupation": self.county_occupation if hasattr(self, 'county_occupation') else county_occupation,
                "pay_periods": self.pay_periods if hasattr(self, 'pay_periods') else pay_periods
                }

        # Adjusted Gross Income (federal_agi) = gross income - deductions
        federal_agi = self.federal_agi if hasattr(self, 'federal_agi') else federal_agi
        if federal_agi:
            json = dict(json_init, **{"federal_agi": federal_agi})
        
        # Calculates federal_agi for you by determining deductions
        else:
            json = dict(json_init, **{
                    "income": self.income if hasattr(self, 'income') else income,
                    "birth_year": self.birth_year if hasattr(self, 'birth_year') else birth_year,
                    "dependents": self.dependents if hasattr(self, 'dependents') else dependents,
                    "filers_over_65": self.filers_over_65 if hasattr(self, 'filers_over_65') else filers_over_65,
                    "traditional_esp_contributions": self.traditional_esp_contributions if hasattr(self, 'traditional_esp_contributions') else traditional_esp_contributions,
                    "traditional_ira_contributions": self.traditional_ira_contributions if hasattr(self, 'traditional_ira_contributions') else traditional_ira_contributions,
                    "pmi": self.pmi if hasattr(self, 'pmi') else pmi
                    })
            
        self.fetch(json, "income-taxes")


    def capital_gains_taxes(self, capital_gains_long=0, capital_gains_short=0, only_federal=False, only_state=False, filing_status='single', state_residence=None, county_residence=None, federal_agi=0, state_agi=0, income=0, birth_year=1990, dependents=0, filers_over_65=0, traditional_esp_contributions=0, traditional_ira_contributions=0, pmi=0):
        """Federal Capital Gains Taxes (See respective state functions for state capital gains taxes)

        Parameters:
        capital_gains_long : int, optional
            Net long term capital gains. Default is 0.
        capital_gains_short: int, optional
            Net short term capital gains. Default is 0.
        only_federal : bool, optional
            Whether or not to only calculate federal capital gains taxes. Default is False.
        only_state : bool, optional
            Whether or not to only calculate state capital gains taxes. Default is False.
        filing_status : str, optional
            Filing status for taxes. Options are 'single', 'married', 'married_seperately', 'head_of_household', 'widow'. Default is 'single'. Source - https://www.irs.gov/newsroom/taxpayers-should-use-the-correct-filing-status-for-accuracy-and-to-avoid-
        state_residence : str, optional
            State of residence. Default is None.
        county_residence : str, optional
            County of residence. Default is None.
        credits_federal : int, optional
            Credits for federal taxes. Default is 0. Source - https://www.irs.gov/credits-deductions-for-individuals
        credits_state : int, optional
            Credits for state taxes. Default is 0.
        federal_agi : int, optional
            Adjusted Gross Income (AGI) for federal taxes. Default is 0. Source -  https://www.irs.gov/e-file-providers/definition-of-adjusted-gross-income, https://www.irs.gov/newsroom/taxpayers-should-know-the-difference-between-standard-and-itemized-deductions
        state_agi : int, optional
            Adjusted Gross Income (AGI) for state taxes. Default is 0.
        income : int, optional
            Gross income. Default is 0.
        birth_year : int, optional
            Year of birth. Options are 1923-2005. Default is 1990.
        dependents : int, optional
            Number of dependents. Default is 0. Source - https://www.irs.gov/faqs/filing-requirements-status-dependents/dependents/dependents-2
        filers_over_65 : int, optional
            Number of filers over 65. Options are 0, 1, 2. Default is 0. 
        traditional_esp_contributions : int, optional
            Traditional employer sponsored plan (401k, 403(b), and 457(b)) contributions. For 401(k)s, the max is 22,500 with an additional 7,500 those 50 or older. Default is 0. Source - https://www.irs.gov/newsroom/401k-limit-increases-to-22500-for-2023-ira-limit-rises-to-6500
        traditional_ira_contributions : int, optional
            Traditional IRA contributions. Max is 6,500 with an additional 1,000 for those 50 or older. Default is 0. Source - https://www.irs.gov/newsroom/401k-limit-increases-to-22500-for-2023-ira-limit-rises-to-6500
        pmi : int, optional
            Monthly Social Security benefits or Primary Monthly Insurance (PMI). Max is 4,555. Default is 0. Source - https://faq.ssa.gov/en-us/Topic/article/KA-01897

        Returns:
        pandas.DataFrame: A DataFrame containing the detailed tax breakdown.

        Note:
        The function fetches the latest tax details from external sources to perform the calculation.
        
        Sources:
        https://www.irs.gov/taxtopics/tc409
        https://www.irs.gov/taxtopics/tc559
        """
        
        if only_state and only_federal:
            raise ValueError("You can't have both only_state and only_federal set to True")
        
        json_init = {
                "filing_status": self.filing_status if hasattr(self, 'filing_status') else filing_status,
                "capital_gains_long": self.capital_gains_long if self.capital_gains_long else capital_gains_long,
                "capital_gains_short": self.capital_gains_short if hasattr(self, 'capital_gains_short') else capital_gains_short,
                "state_residence": self.state_residence if hasattr(self, 'state_residence ') else state_residence,
                "county_residence": self.county_residence if hasattr(self, 'county_residence') else county_residence
                }

        # Adjusted Gross Income (AGI) = gross income - deductions
        federal_agi = self.federal_agi if hasattr(self, 'federal_agi') else federal_agi
        if federal_agi:
            json = dict(json_init, **{"federal_agi": federal_agi})
        
        state_agi = self.state_agi if hasattr(self, 'state_agi') else state_agi
        if state_agi:
            json = dict(json_init, **{"state_agi": state_agi})

        # Calculates federal or state AGI for you by determining deductions
        if not federal_agi or not state_agi:
            json = dict(json_init, **{
                        "income": self.income if hasattr(self, 'income') else income,
                        "birth_year": self.birth_year if hasattr(self, 'birth_year') else birth_year,
                        "dependents": self.dependents if hasattr(self, 'dependents') else dependents,
                        "filers_over_65": self.filers_over_65 if hasattr(self, 'filers_over_65') else filers_over_65,
                        "traditional_esp_contributions": self.traditional_esp_contributions if hasattr(self, 'traditional_esp_contributions') else traditional_esp_contributions,
                        "traditional_ira_contributions": self.traditional_ira_contributions if hasattr(self, 'traditional_ira_contributions') else traditional_ira_contributions,
                        "pmi": self.pmi if hasattr(self, 'pmi') else pmi
                    })

        return self.__fetch__(json, 'capital-gains-taxes')
    
    def federal_capital_gains_taxes(self, capital_gains_long=0, capital_gains_short=0, only_federal=False, only_state=False, filing_status='single', state_residence=None, county_residence=None, federal_agi=0, state_agi=0, income=0, birth_year=1990, dependents=0, filers_over_65=0, traditional_esp_contributions=0, traditional_ira_contributions=0, pmi=0):
        """Federal Capital Gains Taxes (See respective state functions for state capital gains taxes)

        Parameters:
        capital_gains_long : int, optional
            Net long term capital gains. Default is 0.
        capital_gains_short: int, optional
            Net short term capital gains. Default is 0.
        filing_status : str, optional
            Filing status for taxes. Options are 'single', 'married', 'married_seperately', 'head_of_household', 'widow'. Default is 'single'. Source - https://www.irs.gov/newsroom/taxpayers-should-use-the-correct-filing-status-for-accuracy-and-to-avoid-
        credits_federal : int, optional
            Credits for federal taxes. Default is 0. Source - https://www.irs.gov/credits-deductions-for-individuals
        credits_state : int, optional
            Credits for state taxes. Default is 0.
        federal_agi : int, optional
            Adjusted Gross Income (AGI) for federal taxes. Default is 0. Source -  https://www.irs.gov/e-file-providers/definition-of-adjusted-gross-income, https://www.irs.gov/newsroom/taxpayers-should-know-the-difference-between-standard-and-itemized-deductions
        income : int, optional
            Gross income. Default is 0.
        birth_year : int, optional
            Year of birth. Options are 1923-2005. Default is 1990.
        dependents : int, optional
            Number of dependents. Default is 0. Source - https://www.irs.gov/faqs/filing-requirements-status-dependents/dependents/dependents-2
        filers_over_65 : int, optional
            Number of filers over 65. Options are 0, 1, 2. Default is 0. 
        traditional_esp_contributions : int, optional
            Traditional employer sponsored plan (401k, 403(b), and 457(b)) contributions. For 401(k)s, the max is 22,500 with an additional 7,500 those 50 or older. Default is 0. Source - https://www.irs.gov/newsroom/401k-limit-increases-to-22500-for-2023-ira-limit-rises-to-6500
        traditional_ira_contributions : int, optional
            Traditional IRA contributions. Max is 6,500 with an additional 1,000 for those 50 or older. Default is 0. Source - https://www.irs.gov/newsroom/401k-limit-increases-to-22500-for-2023-ira-limit-rises-to-6500
        pmi : int, optional
            Monthly Social Security benefits or Primary Monthly Insurance (PMI). Max is 4,555. Default is 0. Source - https://faq.ssa.gov/en-us/Topic/article/KA-01897

        Returns:
        pandas.DataFrame: A DataFrame containing the detailed tax breakdown.

        Note:
        The function fetches the latest tax details from external sources to perform the calculation.
        
        Sources:
        https://www.irs.gov/taxtopics/tc409
        https://www.irs.gov/taxtopics/tc559
        """
        
        if only_state and only_federal:
            raise ValueError("You can't have both only_state and only_federal set to True")
        
        json_init = {
                "filing_status": self.filing_status if hasattr(self, 'filing_status') else filing_status,
                "capital_gains_long": self.capital_gains_long if self.capital_gains_long else capital_gains_long,
                "capital_gains_short": self.capital_gains_short if hasattr(self, 'capital_gains_short') else capital_gains_short,
                }

    
        # Adjusted Gross Income (AGI) = gross income - deductions
        federal_agi = self.federal_agi if hasattr(self, 'federal_agi') else federal_agi
        if federal_agi:
                json = dict(json_init, **{"federal_agi": federal_agi})

        # Calculates federal or state AGI for you by determining deductions
        if not federal_agi:
            json = dict(json_init, **{
                        "income": self.income if hasattr(self, 'income') else income,
                        "birth_year": self.birth_year if hasattr(self, 'birth_year') else birth_year,
                        "dependents": self.dependents if hasattr(self, 'dependents') else dependents,
                        "filers_over_65": self.filers_over_65 if hasattr(self, 'filers_over_65') else filers_over_65,
                        "traditional_esp_contributions": self.traditional_esp_contributions if hasattr(self, 'traditional_esp_contributions') else traditional_esp_contributions,
                        "traditional_ira_contributions": self.traditional_ira_contributions if hasattr(self, 'traditional_ira_contributions') else traditional_ira_contributions,
                        "pmi": self.pmi if hasattr(self, 'pmi') else pmi
                    })
    
        return self.__fetch__(json, 'capital-gains-taxes')


    def fica_taxes(self, filing_status='single', salary=0):
        """Federal Insurance Contributions Act (FICA)

        Parameters:
        filing_status : str, optional
            Filing status for taxes. Options are 'single', 'married', 'married_seperately', 'head_of_household', 'widow'. Default is 'single'. Source - https://www.irs.gov/newsroom/taxpayers-should-use-the-correct-filing-status-for-accuracy-and-to-avoid-
        salary : int, optional
            Salary. Default is 100000.

        Returns:
        pandas.DataFrame: A DataFrame containing the detailed tax breakdown.

        Note:
        The function fetches the latest tax details from external sources to perform the calculation.
        
        Sources:
        https://www.ssa.gov/oact/cola/cbb.html
        https://www.irs.gov/taxtopics/tc560#:~:text=A%200.9%25%20Additional%20Medicare%20Tax,%24200%2C000%20for%20all%20other%20taxpayers
        """
        json = {
            "income": self.salary if hasattr(self, 'salary') else salary,
            "filing_status": self.filing_status if hasattr(self, 'filing_status') else filing_status
        }

        return self.__fetch__(json, "fica-taxes")


    def savers_tax_credit(self, filing_status='single', traditional_esp_contributions=0, traditional_ira_contributions=0, roth_ira_contributions=0, federal_agi=0, income=0, capital_gains_short=0, birth_year=1990, dependents=0, filers_over_65=0, pmi=0):
        """Saver's Credit

        Parameters:
        filing_status : str, optional
            Filing status for taxes. Options are 'single', 'married', 'married_seperately', 'head_of_household', 'widow'. Default is 'single'. Source - https://www.irs.gov/newsroom/taxpayers-should-use-the-correct-filing-status-for-accuracy-and-to-avoid-
        traditional_esp_contributions : int, optional
            Traditional employer sponsored plan (401k, 403(b), and 457(b)) contributions. For 401(k)s, the max is 22,500 with an additional 7,500 those 50 or older. Default is 0. Source - https://www.irs.gov/newsroom/401k-limit-increases-to-22500-for-2023-ira-limit-rises-to-6500
        traditional_ira_contributions : int, optional
            Traditional IRA contributions. Max is 6,500 with an additional 1,000 for those 50 or older. Default is 0. Source - https://www.irs.gov/newsroom/401k-limit-increases-to-22500-for-2023-ira-limit-rises-to-6500
        roth_ira_contributions : int, optional
            Roth IRA contributions. Max is 6,500 with an additional 1,000 for those 50 or older. Default is 0. Source - https://www.irs.gov/newsroom/401k-limit-increases-to-22500-for-2023-ira-limit-rises-to-6500
        federal_agi : int, optional
            Adjusted Gross Income (AGI) for federal taxes. Default is 0. Source -  https://www.irs.gov/e-file-providers/definition-of-adjusted-gross-income, https://www.irs.gov/newsroom/taxpayers-should-know-the-difference-between-standard-and-itemized-deductions
        income : int, optional
            Gross income. Default is 0.
        capital_gains_short : int, optional
            Net short-term capital gains. Default is 0.
        birth_year : int, optional
            Year of birth. Options are 1923-2005. Default is 1990.
        dependents : int, optional
            Number of dependents. Default is 0. Source - https://www.irs.gov/faqs/filing-requirements-status-dependents/dependents/dependents-2
        filers_over_65 : int, optional
            Number of filers over 65. Options are 0, 1, 2. Default is 0. 
        pmi : int, optional
            Monthly Social Security benefits or Primary Monthly Insurance (PMI). Max is 4,555. Default is 0. Source - https://faq.ssa.gov/en-us/Topic/article/KA-01897
        
        Returns:
        pandas.DataFrame: A DataFrame containing the detailed tax breakdown.

        Note:
        The function fetches the latest tax details from external sources to perform the calculation.
        
        Sources:
        https://www.irs.gov/retirement-plans/plan-participant-employee/retirement-savings-contributions-savers-credit
        """
        
        traditional_esp_contributions = self.traditional_esp_contributions if hasattr(self, 'traditional_esp_contributions') else traditional_esp_contributions
        traditional_ira_contributions = self.traditional_ira_contributions if hasattr(self, 'traditional_ira_contributions') else traditional_ira_contributions
        roth_ira_contributions = self.roth_ira_contributions if hasattr(self, 'roth_ira_contributions') else roth_ira_contributions
        
        json_init = {
                "filing_status": self.filing_status if hasattr(self, 'filing_status') else filing_status,
                "contributions": traditional_esp_contributions + traditional_ira_contributions + roth_ira_contributions
                }
        
        # Adjusted Gross Income (federal_agi) = gross income - deductions
        federal_agi = self.federal_agi if hasattr(self, 'federal_agi') else federal_agi
        if federal_agi:
            json = dict(json_init, **{"federal_agi": federal_agi})

        # Calculates federal_agi for you by determining deductions
        else:
            json = dict(json_init, **{
                    "income": self.income if hasattr(self, 'income') else income,
                    "capital_gains_short": self.capital_gains_short if hasattr(self, 'capital_gains_short') else capital_gains_short,
                    "birth_year": self.birth_year if hasattr(self, 'birth_year') else birth_year,
                    "dependents": self.dependents if hasattr(self, 'dependents') else dependents,
                    "filers_over_65": self.filers_over_65 if hasattr(self, 'filers_over_65') else filers_over_65,
                    "pmi": self.pmi if hasattr(self, 'pmi') else pmi
                    })

        return self.__fetch__(json, "savers-tax-credit")


    def eic_tax_credit(self, filing_status='single', residence_state="", federal_agi=0, income=0, capital_gains_short=0, birth_year=1990, dependents=0, filers_over_65=0, traditional_esp_contributions=0, traditional_ira_contributions=0, pmi=0): 
        """Earned Income Tax Credit (EIC)

        Parameters:
        filing_status : str, optional
            Filing status for taxes. Options are 'single', 'married', 'married_seperately', 'head_of_household', 'widow'. Default is 'single'. Source - https://www.irs.gov/newsroom/taxpayers-should-use-the-correct-filing-status-for-accuracy-and-to-avoid-
        state_residence : str, optional
            State of residence. Default is None.
        federal_agi : int, optional
            Adjusted Gross Income (AGI) for federal taxes. Default is 0. Source -  https://www.irs.gov/e-file-providers/definition-of-adjusted-gross-income, https://www.irs.gov/newsroom/taxpayers-should-know-the-difference-between-standard-and-itemized-deductions
        income : int, optional
            Gross income. Default is 0.
        capital_gains_short : int, optional
            Net short-term capital gains. Default is 0.
        birth_year : int, optional
            Year of birth. Options are 1923-2005. Default is 1990.
        dependents : int, optional
            Number of dependents. Default is 0. Source - https://www.irs.gov/faqs/filing-requirements-status-dependents/dependents/dependents-2
        filers_over_65 : int, optional
            Number of filers over 65. Options are 0, 1, 2. Default is 0. 
        traditional_esp_contributions : int, optional
            Traditional employer sponsored plan (401k, 403(b), and 457(b)) contributions. For 401(k)s, the max is 22,500 with an additional 7,500 those 50 or older. Default is 0. Source - https://www.irs.gov/newsroom/401k-limit-increases-to-22500-for-2023-ira-limit-rises-to-6500
        traditional_ira_contributions : int, optional
            Traditional IRA contributions. Max is 6,500 with an additional 1,000 for those 50 or older. Default is 0. Source - https://www.irs.gov/newsroom/401k-limit-increases-to-22500-for-2023-ira-limit-rises-to-6500
        pmi : int, optional
            Monthly Social Security benefits or Primary Monthly Insurance (PMI). Max is 4,555. Default is 0. Source - https://faq.ssa.gov/en-us/Topic/article/KA-01897
        
        Returns:
        pandas.DataFrame: A DataFrame containing the detailed tax breakdown.

        Note:
        The function fetches the latest tax details from external sources to perform the calculation.
        
        Sources:
        https://www.irs.gov/credits-deductions/individuals/earned-income-tax-credit/earned-income-and-earned-income-tax-credit-eitc-tables
        """

        # Adjusted Gross Income (federal_agi) = gross income - deductions
        json_init = {
                "filing_status": self.filing_status if hasattr(self, 'filing_status') else filing_status,
                "residence_state": residence_state
                }
        
        federal_agi = self.federal_agi if hasattr(self, 'federal_agi') else federal_agi
        if federal_agi:
            json = dict(json_init, **{"federal_agi": federal_agi})

        # Calculates federal_agi for you by determining deductions
        else:
            json = dict(json_init, **{
                    "income": self.income if hasattr(self, 'income') else income,
                    "capital_gains_short": self.capital_gains_short if hasattr(self, 'capital_gains_short') else capital_gains_short,
                    "birth_year": self.birth_year if hasattr(self, 'birth_year') else birth_year,
                    "dependents": self.dependents if hasattr(self, 'dependents') else dependents,
                    "filers_over_65": self.filers_over_65 if hasattr(self, 'filers_over_65') else filers_over_65,
                    "traditional_esp_contributions": self.traditional_esp_contributions if hasattr(self, 'traditional_esp_contributions') else traditional_esp_contributions,
                    "traditional_ira_contributions": self.traditional_ira_contributions if hasattr(self, 'traditional_ira_contributions') else traditional_ira_contributions,
                    "pmi": self.pmi if hasattr(self, 'pmi') else pmi
                    })
            
        return self.__fetch__(json, "eic-tax-credt")

    def social_security_taxes(self, pmi=0, filing_status='single', federal_agi=0, state_residence=None, county_residence="Other", pay_periods=24, income=0, capital_gains_short=0, birth_year=1990, dependents=0, filers_over_65=0, traditional_esp_contributions=0, traditional_ira_contributions=0):
        '''
        This function calculates the amount of benefits subject to income
        taxes and subsequently the amount of taxes paid on those benefits.
        See social_security_portion_taxable and income for more information. 

        Parameters:
        pmi : int, optional
            Monthly Social Security benefits or Primary Monthly Insurance (PMI). Max is 4,555. Default is 0. Source - https://faq.ssa.gov/en-us/Topic/article/KA-01897
        filing_status : str, optional
            Filing status for taxes. Options are 'single', 'married', 'married_seperately', 'head_of_household', 'widow'. Default is 'single'. Source - https://www.irs.gov/newsroom/taxpayers-should-use-the-correct-filing-status-for-accuracy-and-to-avoid-
        federal_agi : int, optional
            Adjusted Gross Income (AGI) for federal taxes. Default is 0. Source -  https://www.irs.gov/e-file-providers/definition-of-adjusted-gross-income, https://www.irs.gov/newsroom/taxpayers-should-know-the-difference-between-standard-and-itemized-deductions
        state_agi : int, optional
            Adjusted Gross Income (AGI) for state taxes. Default is 0.
        credits_federal : int, optional
            Credits for federal taxes. Default is 0. Source - https://www.irs.gov/credits-deductions-for-individuals
        credits_state : int, optional
            Credits for state taxes. Default is 0.
        capital_gains_long : int, optional
            Net long term capital gains. Default is 0.
        capital_gains_short : int, optional
            Net short term capital gains. Default is 0.
        state_residence : str, optional
            State of residence. Default is None.
        state_occupation : str, optional
            State of residence. Default is None.
        county_residence : str, optional
            State of residence. Default is None.
        county_occupation : str, optional
            State of occupation. Default is None.
        pay_periods : int, optional
            Number of pay periods. Options are 13, 24, 26, 52. Default is 24.
        income : int, optional
            Gross income. Default is 0.
        birth_year : int, optional
            Year of birth. Options are 1923-2005. Default is 1990.
        dependents : int, optional
            Number of dependents. Default is 0. Source - https://www.irs.gov/faqs/filing-requirements-status-dependents/dependents/dependents-2
        filers_over_65 : int, optional
            Number of filers over 65. Options are 0, 1, 2. Default is 0. 
        traditional_esp_contributions : int, optional
            Traditional employer sponsored plan (401k, 403(b), and 457(b)) contributions. For 401(k)s, the max is 22,500 with an additional 7,500 those 50 or older. Default is 0. Source - https://www.irs.gov/newsroom/401k-limit-increases-to-22500-for-2023-ira-limit-rises-to-6500
        traditional_ira_contributions : int, optional
            Traditional IRA contributions. Max is 6,500 with an additional 1,000 for those 50 or older. Default is 0. Source - https://www.irs.gov/newsroom/401k-limit-increases-to-22500-for-2023-ira-limit-rises-to-6500

        Returns:
        pandas.DataFrame: A DataFrame containing the detailed tax breakdown.

        Note:
        The function fetches the latest tax details from external sources to perform the calculation.
        
        Sources:
        https://www.irs.gov/pub/irs-pdf/p915.pdf
        '''
        json_init = {
                "pmi": self.pmi if hasattr(self, 'pmi') else pmi,
                "filing_status": self.filing_status if hasattr(self, 'filing_status') else filing_status,
                "capital_gains_short": self.capital_gains_short if hasattr(self, 'capital_gains_short') else capital_gains_short,
                "state_residence": self.state_residence if hasattr(self, 'state_residence ') else state_residence,
                "county_residence": self.county_residence if hasattr(self, 'county_residence') else county_residence,
                "pay_periods": self.pay_periods if hasattr(self, 'pay_periods') else pay_periods
                }

        # Adjusted Gross Income (federal_agi) = gross income - deductions
        federal_agi = self.federal_agi if hasattr(self, 'federal_agi') else federal_agi
        if federal_agi:
            json = dict(json_init, **{"federal_agi": federal_agi})

        # Calculates federal_agi for you by determining deductions
        else:
            json = dict(json_init, **{
                    "income": self.income if hasattr(self, 'income') else income,
                    "birth_year": self.birth_year if hasattr(self, 'birth_year') else birth_year,
                    "dependents": self.dependents if hasattr(self, 'dependents') else dependents,
                    "filers_over_65": self.filers_over_65 if hasattr(self, 'filers_over_65') else filers_over_65,
                    "traditional_esp_contributions": self.traditional_esp_contributions if hasattr(self, 'traditional_esp_contributions') else traditional_esp_contributions,
                    "traditional_ira_contributions": self.traditional_ira_contributions if hasattr(self, 'traditional_ira_contributions') else traditional_ira_contributions
                    })

        return self.__fetch__(json, "social-security-taxes")


    def social_security_benefits_factor(self, election_age=62, election_month='January'):
        """Social Security PMI factor for early or delayed retirement

        Parameters:
        election_age : int, optional
            Age in years at Social Security benefits election. Default is the minimum, or 62. Max is 70.
        election_month : int, optional
            Month of Social Security benefits election. Default is January. Options are January, February, March, April, May, June, July, August, September, October, November, December.
            
        Returns:
        pandas.DataFrame: A DataFrame containing the social security factor.

        Note:
        The function fetches the latest tax details from external sources to perform the calculation.
        
        Sources:
        https://www.ssa.gov/oact/ProgData/ar_drc.html
        """

        json = {
                "api_key": self.api_key,
                "election_age": self.election_age if self.election_age else election_age,
                "election_month": self.election_month if self.election_month else election_month
                }
    
        return self.__fetch__(json, "social-security-benefits-factor")

    def social_security_benefits(self, salary=0, salary_array=False):
        """Social Security Benefitseic

        Parameters:
        salary : int, optional
            Salary. Default is 100000.
        salary_array : list, optional
            DataFrame, CSV, XLS, or XLSX of 35 highest salaries in the formate year,salary. Default is False.
        
        Returns:
        pandas.DataFrame: A DataFrame containing the social security benefits projcetion at ages 62, 67, and 70.
        
        Note:
        The function fetches the latest tax details from external sources to perform the calculation.
        
        Sources:
        https://www.ssa.gov/oact/cola/awiseries.html
        https://www.ssa.gov/oact/cola/cbb.html
        https://www.ssa.gov/oact/COLA/piaformula.html
        """
        
        json = {"api_key": self.api_key}
        if salary:
            json["salary"] =  self.salary if self.salary else salary
        else:
            json["salary_array"] = self.salary_array if self.salary_array else salary_array
            
        return self.__fetch__(json, "social-security-benefits")


    def social_security_portion_taxable(self, pmi=0, filing_status="single", state_residence=None, county_residence="Other", federal_agi=0, income=0, capital_gains_short=0, dependents=0, filers_over_65=0, traditional_esp_contributions=0, traditional_ira_contributions=0):
        """Portion of Social Security benefits subject to taxation

        Parameters:
        pmi : int, optional
            Monthly Social Security benefits or Primary Monthly Insurance (PMI). Max is 4,555. Default is 0. Source - https://faq.ssa.gov/en-us/Topic/article/KA-01897
        filing_status : str, optional
            Filing status for taxes. Options are 'single', 'married', 'married_seperately', 'head_of_household', 'widow'. Default is 'single'. Source - https://www.irs.gov/newsroom/taxpayers-should-use-the-correct-filing-status-for-accuracy-and-to-avoid-
        federal_agi : int, optional
            Adjusted Gross Income (AGI) for federal taxes. Default is 0. Source -  https://www.irs.gov/e-file-providers/definition-of-adjusted-gross-income, https://www.irs.gov/newsroom/taxpayers-should-know-the-difference-between-standard-and-itemized-deductions
        state_agi : int, optional
            Adjusted Gross Income (AGI) for state taxes. Default is 0.
        credits_federal : int, optional
            Credits for federal taxes. Default is 0. Source - https://www.irs.gov/credits-deductions-for-individuals
        credits_state : int, optional
            Credits for state taxes. Default is 0.
        capital_gains_long : int, optional
            Net long term capital gains. Default is 0.
        capital_gains_short : int, optional
            Net short term capital gains. Default is 0.
        state_residence : str, optional
            State of residence. Default is None.
        state_occupation : str, optional
            State of residence. Default is None.
        county_residence : str, optional
            State of residence. Default is None.
        county_occupation : str, optional
            State of occupation. Default is None.
        pay_periods : int, optional
            Number of pay periods. Options are 12, 24, 26, 52. Default is 24.
        income : int, optional
            Gross income. Default is 100000.
        birth_year : int, optional
            Year of birth. Options are 1923-2005. Default is 1990.
        dependents : int, optional
            Number of dependents. Default is 0. Source - https://www.irs.gov/faqs/filing-requirements-status-dependents/dependents/dependents-2
        filers_over_65 : int, optional
            Number of filers over 65. Options are 0, 1, 2. Default is 0.  
        traditional_esp_contributions : int, optional
            Traditional employer sponsored plan (401k, 403(b), and 457(b)) contributions. For 401(k)s, the max is 22,500 with an additional 7,500 those 50 or older. Default is 0. Source - https://www.irs.gov/newsroom/401k-limit-increases-to-22500-for-2023-ira-limit-rises-to-6500
        traditional_ira_contributions : int, optional
            Traditional IRA contributions. Max is 6,500 with an additional 1,000 for those 50 or older. Default is 0. Source - https://www.irs.gov/newsroom/401k-limit-increases-to-22500-for-2023-ira-limit-rises-to-6500

        Returns:
        pandas.DataFrame: A DataFrame containing the detailed taxable breakdown.

        Note:
        The function fetches the latest tax details from external sources to perform the calculation.
        
        Sources:
        https://www.irs.gov/pub/irs-pdf/p915.pdf
        """
            
        json_init = {
                "pmi": self.pmi if hasattr(self, 'pmi') else pmi,
                "filing_status": self.filing_status if hasattr(self, 'filing_status') else filing_status,
                "state_residence": self.state_residence if hasattr(self, 'state_residence ') else state_residence,
                "county_residence": self.county_residence if hasattr(self, 'county_residence') else county_residence,
                }
        
        federal_agi = self.federal_agi if hasattr(self, 'federal_agi') else federal_agi
        if federal_agi:
            json = dict(json_init, **{
                    "federal_agi": federal_agi
                    })
        else:
            json = dict(json_init, **{
                    "income": self.income if hasattr(self, 'income') else income,
                    "capital_gains_short": self.capital_gains_short if hasattr(self, 'capital_gains_short') else capital_gains_short,
                    "dependents": self.dependents if hasattr(self, 'dependents') else dependents,
                    "filers_over_65": self.filers_over_65 if hasattr(self, 'filers_over_65') else filers_over_65,
                    
                    "traditional_esp_contributions": self.traditional_esp_contributions if hasattr(self, 'traditional_esp_contributions') else traditional_esp_contributions,
                    "traditional_ira_contributions": self.traditional_ira_contributions if hasattr(self, 'traditional_ira_contributions') else traditional_ira_contributions,
                    })
            
        return self.__fetch__(json, "social-security-portion-of-benefits-taxable")
    
    def roth_ira_contribution_limit(self, age_over_50=False, federal_agi=0, filing_status='single', income=0, capital_gains_short=0, birth_year=1990, dependents=0, filers_over_65=0, traditional_esp_contributions=0, roth_ira_contributions=0, traditional_ira_contributions=0, pmi=0):
        """Roth IRA contribution limit

        Parameters:
        age_over_50 : bool, optional
            Whether or not the filer is over 50. Default is False. Limit can increase by 1,000 if True.
        federal_agi : int, optional
            Adjusted Gross Income (AGI) for federal taxes. Default is 0. Source -  https://www.irs.gov/e-file-providers/definition-of-adjusted-gross-income, https://www.irs.gov/newsroom/taxpayers-should-know-the-difference-between-standard-and-itemized-deductions
        filing_status : str, optional
            Filing status for taxes. Options are 'single', 'married', 'married_seperately', 'head_of_household', 'widow'. Default is 'single'. Source - https://www.irs.gov/newsroom/taxpayers-should-use-the-correct-filing-status-for-accuracy-and-to-avoid-
        income : int, optional
            Gross income. Default is 0.
        capital_gains_short : int, optional
            Net short-term capital gains. Default is 0.
        birth_year : int, optional
            Year of birth. Options are 1923-2005. Default is 1990.
        dependents : int, optional
            Number of dependents. Default is 0. Source - https://www.irs.gov/faqs/filing-requirements-status-dependents/dependents/dependents-2
        filers_over_65 : int, optional
            Number of filers over 65. Options are 0, 1, 2. Default is 0.
        traditional_esp_contributions : int, optional
            Traditional employer sponsored plan (401k, 403(b), and 457(b)) contributions. For 401(k)s, the max is 22,500 with an additional 7,500 those 50 or older. Default is 0. Source - https://www.irs.gov/newsroom/401k-limit-increases-to-22500-for-2023-ira-limit-rises-to-6500
        roth_ira_contributions : int, optional
            ROTH IRA contributions. Max is 6,500 with an additional 1,000 for those 50 or older. Default is 0. Source - https://www.irs.gov/newsroom/401k-limit-increases-to-22500-for-2023-ira-limit-rises-to-6500
        pmi : int, optional
            Monthly Social Security benefits or Primary Monthly Insurance (PMI). Max is 4,555. Default is 0. Source - https://faq.ssa.gov/en-us/Topic/article/KA-01897
        
        Returns:
        pandas.DataFrame: A DataFrame containing a breakdown of the limit.

        Note:
        The function fetches the latest tax details from external sources to perform the calculation.

        Sources:
        https://www.irs.gov/retirement-plans/amount-of-roth-ira-contributions-that-you-can-make-for-2023
        """
        
        json_init = {
                "filing_status": self.filing_status if hasattr(self, 'filing_status') else filing_status,
                "age_over_50": self.age_over_50 if hasattr(self, 'age_over_50 ') else age_over_50,
                "roth_ira_contributions": self.roth_ira_contributions if hasattr(self, 'roth_ira_contributions') else roth_ira_contributions
                }

        # Adjusted Gross Income (federal_agi) = gross income - deductions
        federal_agi = self.federal_agi if hasattr(self, 'federal_agi') else federal_agi
        if federal_agi:
            json = dict(json_init, **{
                    "federal_agi": federal_agi
                    })
        else:
            json = dict(json_init, **{
                    "income": self.income if hasattr(self, 'income') else income,
                    "capital_gains_short": self.capital_gains_short if hasattr(self, 'capital_gains_short') else capital_gains_short,
                    "dependents": self.dependents if hasattr(self, 'dependents') else dependents,
                    "filers_over_65": self.filers_over_65 if hasattr(self, 'filers_over_65') else filers_over_65,
                    "traditional_esp_contributions": self.traditional_esp_contributions if hasattr(self, 'traditional_esp_contributions') else traditional_esp_contributions,
                    "traditional_ira_contributions": self.traditional_ira_contributions if hasattr(self, 'traditional_ira_contributions') else traditional_ira_contributions,
                    "pmi": self.pmi if hasattr(self, 'pmi') else pmi
                    })


        return self.__fetch__(json, "roth-ira-contribution-limit")
    
    def traditional_ira_tax_deductible_amount(self, age_over_50=False, federal_agi=0, filing_status='single', income=0, capital_gains_short=0, dependents=0, filers_over_65=0, traditional_esp_contributions=0, roth_ira_contributions=0, pmi=0):
        """Traditional IRA contribution limit

        Parameters:
        age_over_50 : bool, optional
            Whether or not the filer is over 50. Default is False. Limit can increase by 1,000 if True.
        federal_agi : int, optional
            Adjusted Gross Income (AGI) for federal taxes. Default is 0. Source -  https://www.irs.gov/e-file-providers/definition-of-adjusted-gross-income, https://www.irs.gov/newsroom/taxpayers-should-know-the-difference-between-standard-and-itemized-deductions
        filing_status : str, optional
            Filing status for taxes. Options are 'single', 'married', 'married_seperately', 'head_of_household', 'widow'. Default is 'single'. Source - https://www.irs.gov/newsroom/taxpayers-should-use-the-correct-filing-status-for-accuracy-and-to-avoid-
        income : int, optional
            Gross income. Default is 0.
        dependents : int, optional
            Number of dependents. Default is 0. Source - https://www.irs.gov/faqs/filing-requirements-status-dependents/dependents/dependents-2
        filers_over_65 : int, optional
            Number of filers over 65. Options are 0, 1, 2. Default is 0. 
        traditional_esp_contributions : int, optional
            Traditional employer sponsored plan (401k, 403(b), and 457(b)) contributions. For 401(k)s, the max is 22,500 with an additional 7,500 those 50 or older. Default is 0. Source - https://www.irs.gov/newsroom/401k-limit-increases-to-22500-for-2023-ira-limit-rises-to-6500
        traditional_ira_contributions : int, optional
            Traditional IRA contributions. Max is 6,500 with an additional 1,000 for those 50 or older. Default is 0. Source - https://www.irs.gov/newsroom/401k-limit-increases-to-22500-for-2023-ira-limit-rises-to-6500
        pmi : int, optional
            Monthly Social Security benefits or Primary Monthly Insurance (PMI). Max is 4,555. Default is 0. Source - https://faq.ssa.gov/en-us/Topic/article/KA-01897
        
        Returns:
        pandas.DataFrame: A DataFrame containing a breakdown of the limit.

        Note:
        The function fetches the latest tax details from external sources to perform the calculation.

        Sources:
        https://www.irs.gov/retirement-plans/2023-ira-deduction-limits-effect-of-modified-agi-on-deduction-if-you-are-covered-by-a-retirement-plan-at-work
        """

        json_init = {
            "filing_status": self.filing_status if hasattr(self, 'filing_status') else filing_status,
            "age_over_50": self.age_over_50 if hasattr(self, 'age_over_50 ') else age_over_50,
            "roth_ira_contributions": self.roth_ira_contributions if hasattr(self, 'roth_ira_contributions') else roth_ira_contributions
        }

        # Adjusted Gross Income (federal_agi) = gross income - deductions
        federal_agi = self.federal_agi if hasattr(self, 'federal_agi') else federal_agi
        if federal_agi:
            json = dict(json_init, **{
                    "federal_agi": federal_agi
                    })
        else:
            json = dict(json_init, **{
                    "income": self.income if hasattr(self, 'income') else income,
                    "capital_gains_short": self.capital_gains_short if hasattr(self, 'capital_gains_short') else capital_gains_short,
                    "dependents": self.dependents if hasattr(self, 'dependents') else dependents,
                    "filers_over_65": self.filers_over_65 if hasattr(self, 'filers_over_65') else filers_over_65,
                    
                    "traditional_esp_contributions": self.traditional_esp_contributions if hasattr(self, 'traditional_esp_contributions') else traditional_esp_contributions,
                    "pmi": self.pmi if hasattr(self, 'pmi') else pmi
                    })
        
        return self.__fetch__(json, "traditional-ira-tax-deductible-amount")
    
    def federal_adjusted_gross_income(self, filing_status='single', income=0, capital_gains_short=0, dependents=0, filers_over_65=0, traditional_esp_contributions=0, traditional_ira_contributions=0, pmi=0):
        """Federal Adjusted Gross Income (AGI)

        parameters:
        filing_status : str, optional
            Filing status for taxes. Options are 'single', 'married', 'married_seperately', 'head_of_household', 'widow'. Default is 'single'. Source - https://www.irs.gov/newsroom/taxpayers-should-use-the-correct-filing-status-for-accuracy-and-to-avoid-
        income : int, optional
            Gross income. Default is 0.
        dependents : int, optional
            Number of dependents. Default is 0. Source - https://www.irs.gov/faqs/filing-requirements-status-dependents/dependents/dependents-2
        filers_over_65 : int, optional
            Number of filers over 65. Options are 0, 1, 2. Default is 0. 

        traditional_esp_contributions : int, optional
            Traditional employer sponsored plan (401k, 403(b), and 457(b)) contributions. For 401(k)s, the max is 22,500 with an additional 7,500 those 50 or older. Default is 0. Source - https://www.irs.gov/newsroom/401k-limit-increases-to-22500-for-2023-ira-limit-rises-to-6500
        traditional_ira_contributions : int, optional
            Traditional IRA contributions. Max is 6,500 with an additional 1,000 for those 50 or older. Default is 0. Source - https://www.irs.gov/newsroom/401k-limit-increases-to-22500-for-2023-ira-limit-rises-to-6500
        pmi : int, optional
            Monthly Social Security benefits or Primary Monthly Insurance (PMI). Max is 4,555. Default is 0. Source - https://faq.ssa.gov/en-us/Topic/article/KA-01897
        
        Returns:
        pandas.DataFrame: A DataFrame containing a breakdown of the AGI.

        Notes:
        The function fetches the latest tax details from external sources to perform the calculation.

        Sources: 
        https://www.irs.gov/e-file-providers/definition-of-adjusted-gross-incomehttps://www.irs.gov/newsroom/taxpayers-should-know-the-difference-between-standard-and-itemized-deductions
        """

        json = {
                "filing_status": self.filing_status if hasattr(self, 'filing_status') else filing_status,
                "income": self.income if hasattr(self, 'income') else income,
                "capital_gains_short": self.capital_gains_short if hasattr(self, 'capital_gains_short') else capital_gains_short,
                "dependents": self.dependents if hasattr(self, 'dependents') else dependents,
                "filers_over_65": self.filers_over_65 if hasattr(self, 'filers_over_65') else filers_over_65,
                "traditional_esp_contributions": self.traditional_esp_contributions if hasattr(self, 'traditional_esp_contributions') else traditional_esp_contributions,
                "pmi": self.pmi if hasattr(self, 'pmi') else pmi
                }
        return self.__fetch__(json, "federal-adjusted-gross-income-(agi)")

