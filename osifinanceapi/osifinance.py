import http.client
import json
from pandas import DataFrame

class Osifinance:
    '''
    The Osifinance class is the main class that provides default variables and functions to query the OSI Finance API. You need to specify a valid API Key and can then begin using its functions.
    '''

    def __init__(self, api_key, sources=None, filing_status=None, salary=None, federal_agi=None, federal_deductions=None, state_agi=None, state_deductions=None, credits_federal=None, credits_state=None, capital_gains_long=None, capital_gains_short=None, state_residence=None, state_occupation=None, county_residence=None, county_occupation=None, pay_periods=None, income=None, birth_year=None, dependents=None, filers_over_65=None, filer_over_50=None, traditional_esp_contributions=None, traditional_ira_contributions=None, roth_ira_contributions=None, contributions=None, pmi=None, election_age=None, election_month=None):
        '''
        Initialize the Osifinance class that provides default variables and functions to query the OSI Finance API. You need to specify a valid
        API key by passing it as a string via api_key. You can sign up for a free api key on the OSI Finance website at https://osifinance.com/signup/.
        
        Parameters:
        api_key : str, required
            Your OSI Finance API key. You can find yours at https://osifinance.com/profile?mode=api.
        sources : bool, optional
            Whether or not to return the sources of the data. Default is False.
        filing_status : str, optional
            Filing status for taxes. Options are 'single', 'married_jointly', 'married_separately', 'head_of_household', 'widow(er)'. Default is 'single'. Source - https://www.irs.gov/newsroom/taxpayers-should-use-the-correct-filing-status-for-accuracy-and-to-avoid-
        salary: int, optional
            Salary from employer or self-employment (ie. W2). Default is 100000.
        federal_agi : int, optional
            Adjusted Gross Income (AGI) for federal taxes. Default is 75000. Source -  https://www.irs.gov/e-file-providers/definition-of-adjusted-gross-income, https://www.irs.gov/newsroom/taxpayers-should-know-the-difference-between-standard-and-itemized-deductions
        state_agi : int, optional
            Adjusted Gross Income (AGI) for state taxes. Default is 75000.
        credits_federal : int, optional
            Credits for federal taxes. Default is 0. Source - https://www.irs.gov/credits-deductions-for-individuals
        credits_state : int, optional
            Credits for state taxes. Default is 0.
        capital_gains_long : int, optional
            Net long term capital gains. Default is 0.
        capital_gains_short : int, optional
            Net short term capital gains. Default is 0.
        state_residence : str, optional
            State of residence. Default is 'Florida', in which case, only Federal taxes will be calculated in the respective functions.
        state_occupation : str, optional
            State of occupation. Default is 'Florida', in which case, only Federal taxes will be calculated in the respective functions.
        county_residence : str, optional
            County of residence. Default is 'Other', in which case, only State taxes will be calculated in the respective functions.
        county_occupation : str, optional
            County of occupation. Default is 'Other', in which case, only State taxes will be calculated in the respective functions.
        pay_periods : int, optional
            Number of pay periods. Options are 12, 24, 26, 52. Default is 24.
        income : int, optional
            Gross income. Default is 100000.
        birth_year : int, optional
            Year of birth. Options are 1923-2005. Default is 1990.
        dependents : int, optional
            Number of dependents (max 10). Default is 0. Source - https://www.irs.gov/faqs/filing-requirements-status-dependents/dependents/dependents-2
        filers_over_65 : int, optional
            Number of filers over 65. Options are 0, 1, 2. Default is 0. 
        filer_over_50 : bool, optional
            Whether or not the filer is over 50. Default is False.
        traditional_esp_contributions : int, optional
            Traditional employer sponsored plan (401k, 403(b), and 457(b)) contributions. For 401(k)s, the max is 22,500 with an additional 7,500 those 50 or older. Default is 0. Source - https://www.irs.gov/newsroom/401k-limit-increases-to-22500-for-2023-ira-limit-rises-to-6500
        traditional_ira_contributions : int, optional
            Traditional IRA contributions. Max is 6,500 with an additional 1,000 for those 50 or older. Default is 0. Source - https://www.irs.gov/newsroom/401k-limit-increases-to-22500-for-2023-ira-limit-rises-to-6500
        contributions : int, optional
            Contributions to retirement accounts. Default is 0.
        pmi : int, optional
            Monthly Social Security benefits or Primary Monthly Insurance (PMI). Max is 4,555. Default is 0. Source - https://faq.ssa.gov/en-us/Topic/article/KA-01897
        '''
    
        if api_key is None:
            raise ValueError('You need to set a valid API key by passing the string with api_key. You can sign up for a free api key on the OSI Finance website at https://osifinance.com/signup/')
        
        self.api_key = api_key
        if sources is not None:
            self.sources = sources
        if filing_status is not None:
            self.filing_status = filing_status
        if federal_agi is not None:
            self.federal_agi = federal_agi
        if federal_deductions is not None:
            self.federal_deductions = federal_deductions
        if state_agi is not None:
            self.state_agi = state_agi
        if state_deductions is not None:
            self.state_deductions = state_deductions
        if credits_federal is not None:
            self.credits_federal = credits_federal
        if credits_state is not None:
            self.credits_state = credits_state
        if capital_gains_long is not None:
            self.capital_gains_long = capital_gains_long
        if capital_gains_short is not None:
            self.capital_gains_short = capital_gains_short
        if state_residence is not None:
            self.state_residence = state_residence
        if state_occupation is not None:
            self.state_occupation = state_occupation
        if county_residence is not None:
            self.county_residence = county_residence
        if county_occupation is not None:
            self.county_occupation = county_occupation
        if pay_periods is not None:
            self.pay_periods = pay_periods
        if income is not None:
            self.income = income
        if birth_year is not None:
            self.birth_year = dependents
        if dependents is not None:
            self.dependents = dependents
        if filers_over_65 is not None:
            self.filers_over_65 = filers_over_65
        if filer_over_50:
            self.filer_over_50 = filer_over_50
        if traditional_esp_contributions is not None:
            self.traditional_esp_contributions = traditional_esp_contributions
        if traditional_ira_contributions is not None:
            self.traditional_ira_contributions = traditional_ira_contributions
        if roth_ira_contributions is not None:
            self.roth_ira_contributions = roth_ira_contributions
        if contributions is not None:
            self.contributions = contributions
        if pmi is not None:
            self.pmi = pmi
        if election_age is not None:
            self.election_age = election_age
        if election_month is not None:
            self.election_month = election_month
        if salary is not None:
            self.salary = salary


    def __fetch__(self, body, path):
        conn = http.client.HTTPSConnection('osifinance.com')

        headers = {'Content-Type': 'application/json'}
        body.update({'api_key': self.api_key, 'python_api': 1})
        payload = json.dumps(body)

        conn.request('POST', f'/api/v1/{path}', body=payload, headers=headers)

        res = conn.getresponse()
        if res.status != 200:
            raise ValueError(f'Error: {res.status} {res.reason}')
        
        data = res.read()
        r = json.loads(data.decode('utf-8'))
        
        if path in ['all-taxes', 'federal-income-taxes', 'fica-taxes', 'federal-capital-gains-taxes', 'state-taxes']:
            df = DataFrame(r['data']).iloc[:, ::-1]
        
        else:
            df = DataFrame(r['data'], index=[0])
        
        if body.get('sources'):
            return {'data': df, 'sources': r['sources']}
        
        return df
    

    def all_taxes(self, sources=False, filing_status='single', income=100000, salary=100000, capital_gains_long=0, capital_gains_short=0, federal_deductions=0, federal_agi=75000, state_agi=0, credits_federal=0, credits_state=0, state_residence='Florida', state_occupation='Florida', county_residence='Other', county_occupation='Other', pay_periods=24, birth_year=1990, dependents=0, filers_over_65=0, traditional_esp_contributions=0, traditional_ira_contributions=0, pmi=0):
        '''Income, FICA, capital gains, and state taxes

        Parameters:
        sources : bool, optional
            Whether or not to return the sources of the data. Default is False.
        filing_status : str, optional
            Filing status for taxes. Options are 'single', 'married_jointly', 'married_separately', 'head_of_household', 'widow(er)'. Default is 'single'. Source - https://www.irs.gov/newsroom/taxpayers-should-use-the-correct-filing-status-for-accuracy-and-to-avoid-
        income : int, optional
            Gross income. Default is 1000000.
        salary: int, optional
            Salary from employer or self-employment (ie. W2). Default is 100000.
        capital_gains_long : int, optional
            Net long term capital gains. Default is 0.
        capital_gains_short : int, optional
            Net short term capital gains. Default is 0.
        federal_deductions : int, optional
            Federal deductions for determining federal AGI. Default is 0. Source -  https://www.irs.gov/e-file-providers/definition-of-adjusted-gross-income, https://www.irs.gov/newsroom/taxpayers-should-know-the-difference-between-standard-and-itemized-deductions
        federal_agi : int, optional
            Adjusted Gross Income (AGI) for federal taxes. Default is 75000. Source -  https://www.irs.gov/e-file-providers/definition-of-adjusted-gross-income, https://www.irs.gov/newsroom/taxpayers-should-know-the-difference-between-standard-and-itemized-deductions
        state_agi : int, optional
            Adjusted Gross Income (AGI) for state taxes. Default is 75000.
        credits_federal : int, optional
            Credits for federal taxes. Default is 0. Source - https://www.irs.gov/credits-deductions-for-individuals
        credits_state : int, optional
            Credits for state taxes. Default is 0.
        state_residence : str, optional
            State of residence. Default is 'Florida'.
        state_occupation : str, optional
            State of residence. Default is 'Florida'.
        county_residence : str, optional
            County of residence. Default is 'Other'.
        county_occupation : str, optional
            County of occupation. Default is 'Other'.
        pay_periods : int, optional
            Number of pay periods. Options are 12, 24, 26, 52. Default is 24.
        birth_year : int, optional
            Year of birth. Options are 1923-2005. Default is 1990.
        dependents : int, optional
            Number of dependents (max 10). Default is 0. Source - https://www.irs.gov/faqs/filing-requirements-status-dependents/dependents/dependents-2
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
        or
        dict: where 'data' contains the DataFrame and 'sources' contains a dict of the sources.

        Note:
        The function fetches the latest tax details from external sources to perform the calculation.
        
        Sources:
        Sources can be found in their respective functions.'''

        # Check if the parameters are set upstream in the instance
        data = {
                'sources': self.sources if hasattr(self, 'sources') else sources,
                'filing_status': self.filing_status if hasattr(self, 'filing_status') else filing_status,
                'income': self.income if hasattr(self, 'income') else income,
                'salary': self.salary if hasattr(self, 'salary') else salary,
                'capital_gains_long': self.capital_gains_long if hasattr(self, 'capital_gains_long') else capital_gains_long,
                'capital_gains_short': self.capital_gains_short if hasattr(self, 'capital_gains_short') else capital_gains_short,
                'federal_deductions': self.federal_deductions if hasattr(self, 'federal_deductions') else federal_deductions,
                'federal_agi': self.federal_agi if hasattr(self, 'federal_agi') else federal_agi,
                'state_agi': self.state_agi if hasattr(self, 'state_agi') else state_agi,
                'credits_federal': self.credits_federal if hasattr(self, 'credits_federal') else credits_federal,
                'credits_state': self.credits_state if hasattr(self, 'credits_state') else credits_state,
                'state_residence': self.state_residence if hasattr(self, 'state_residence') else state_residence,
                'state_occupation': self.state_occupation if hasattr(self, 'state_occupation') else state_occupation,
                'county_residence': self.county_residence if hasattr(self, 'county_residence') else county_residence,
                'county_occupation': self.county_occupation if hasattr(self, 'county_occupation') else county_occupation,
                'pay_periods': self.pay_periods if hasattr(self, 'pay_periods') else pay_periods,
                'birth_year': self.birth_year if hasattr(self, 'birth_year') else birth_year,
                'dependents': self.dependents if hasattr(self, 'dependents') else dependents,
                'filers_over_65': self.filers_over_65 if hasattr(self, 'filers_over_65') else filers_over_65,
                'traditional_esp_contributions': self.traditional_esp_contributions if hasattr(self, 'traditional_esp_contributions') else traditional_esp_contributions,
                'traditional_ira_contributions': self.traditional_ira_contributions if hasattr(self, 'traditional_ira_contributions') else traditional_ira_contributions,
                'pmi': self.pmi if hasattr(self, 'pmi') else pmi                
                }
        
        return self.__fetch__(data, 'all-taxes')


    def federal_income_taxes(self, filing_status='single', income=100000, federal_deductions=0, credits_federal=0, credits_state=0, capital_gains_long=0, capital_gains_short=0, state_residence='Florida', state_occupation='Florida', county_residence='Other', county_occupation='Other', pay_periods=24, dependents=0, birth_year=1990,filers_over_65=0, traditional_esp_contributions=0, traditional_ira_contributions=0, pmi=0, sources=False):
        '''Federal Income Taxes

        Parameters:
        sources : bool, optional
            Whether or not to return the sources of the data. Default is False.
        filing_status : str, optional
            Filing status for taxes. Options are 'single', 'married_jointly', 'married_separately', 'head_of_household', 'widow(er)'. Default is 'single'. Source - https://www.irs.gov/newsroom/taxpayers-should-use-the-correct-filing-status-for-accuracy-and-to-avoid-
        income : int, optional
            Gross income. Default is 100000.
        federal_deductions : int, optional
            Deductions for federal taxes. Default is 0. Source -  https://www.irs.gov/e-file-providers/definition-of-adjusted-gross-income, https://www.irs.gov/newsroom/taxpayers-should-know-the-difference-between-standard-and-itemized-deductions
        state_agi : int, optional
            Adjusted Gross Income (AGI) for state taxes. Default is 75000.
        credits_federal : int, optional
            Credits for federal taxes. Default is 0. Source - https://www.irs.gov/credits-deductions-for-individuals
        credits_state : int, optional
            Credits for state taxes. Default is 0.
        capital_gains_short : int, optional
            Net short term capital gains. Default is 0.
        state_occupation : str, optional
            State of residence. Default is 'Florida'.
        county_residence : str, optional
            County of residence. Default is 'Other'.
        county_occupation : str, optional
            County of occupation. Default is 'Other'.
        pay_periods : int, optional
            Number of pay periods. Options are 12, 24, 26, 52. Default is 24.
        dependents : int, optional
            Number of dependents (max 10). Default is 0. Source - https://www.irs.gov/faqs/filing-requirements-status-dependents/dependents/dependents-2
        birth_year : int, optional
            Year of birth. Options are 1923-2005. Default is 1990.
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
        or
        dict: where 'data' contains the DataFrame and 'sources' contains a dict of the sources.

        Note:
        The function fetches the latest tax details from external sources to perform the calculation.
        
        Sources:
        https://www.irs.gov/newsroom/irs-provides-tax-inflation-adjustments-for-tax-year-2023
        '''

        data = {
                'sources': self.sources if hasattr(self, 'sources') else sources,
                'filing_status': self.filing_status if hasattr(self, 'filing_status') else filing_status,
                'capital_gains_short': self.capital_gains_short if hasattr(self, 'capital_gains_short') else capital_gains_short,
                'capital_gains_long': self.capital_gains_long if hasattr(self, 'capital_gains_long') else capital_gains_long,
                'credits_federal': self.credits_federal if hasattr(self, 'credits_federal') else credits_federal,
                'credits_state': self.credits_state if hasattr(self, 'credits_state') else credits_state,
                'state_residence': self.state_residence if hasattr(self, 'state_residence ') else state_residence,
                'state_occupation': self.state_occupation if hasattr(self, 'state_occupation') else state_occupation,
                'county_residence': self.county_residence if hasattr(self, 'county_residence') else county_residence,
                'county_occupation': self.county_occupation if hasattr(self, 'county_occupation') else county_occupation,
                'pay_periods': self.pay_periods if hasattr(self, 'pay_periods') else pay_periods,
                'income': self.income if hasattr(self, 'income') else income,
                'federal_deductions': self.federal_deductions if hasattr(self, 'federal_deductions') else federal_deductions,
                'dependents': self.dependents if hasattr(self, 'dependents') else dependents,
                'birth_year': self.birth_year if hasattr(self, 'birth_year') else birth_year,
                'filers_over_65': self.filers_over_65 if hasattr(self, 'filers_over_65') else filers_over_65,
                'traditional_esp_contributions': self.traditional_esp_contributions if hasattr(self, 'traditional_esp_contributions') else traditional_esp_contributions,
                'traditional_ira_contributions': self.traditional_ira_contributions if hasattr(self, 'traditional_ira_contributions') else traditional_ira_contributions,
                'pmi': self.pmi if hasattr(self, 'pmi') else pmi
                }
        
        self.__fetch__(data, 'federal-income-taxes')


    def federal_capital_gains_taxes(self, sources=False, filing_status='single', capital_gains_long=0, capital_gains_short=0, income=100000, federal_agi=75000, birth_year=1990, dependents=0, filers_over_65=0, traditional_esp_contributions=0, traditional_ira_contributions=0, pmi=0):
        '''Federal Capital Gains Taxes (See respective state functions for state capital gains taxes)

        Parameters:
        filing_status : str, optional
            Filing status for taxes. Options are 'single', 'married_jointly', 'married_separately', 'head_of_household', 'widow(er)'. Default is 'single'. Source - https://www.irs.gov/newsroom/taxpayers-should-use-the-correct-filing-status-for-accuracy-and-to-avoid-
        capital_gains_long : int, optional
            Net long term capital gains. Default is 0.
        capital_gains_short: int, optional
            Net short term capital gains. Default is 0.
        income : int, optional
            Gross income. Default is 100000.
        federal_agi : int, optional
            Adjusted Gross Income (AGI) for federal taxes. Default is 75000. Source -  https://www.irs.gov/e-file-providers/definition-of-adjusted-gross-income, https://www.irs.gov/newsroom/taxpayers-should-know-the-difference-between-standard-and-itemized-deductions
        dependents : int, optional
            Number of dependents (max 10). Default is 0. Source - https://www.irs.gov/faqs/filing-requirements-status-dependents/dependents/dependents-2
        birth_year : int, optional
            Year of birth. Options are 1923-2005. Default is 1990.
        filers_over_65 : int, optional
            Number of filers over 65. Options are 0, 1, 2. Default is 0. 
        traditional_esp_contributions : int, optional
            Traditional employer sponsored plan (401k, 403(b), and 457(b)) contributions. For 401(k)s, the max is 22,500 with an additional 7,500 those 50 or older. Default is 0. Source - https://www.irs.gov/newsroom/401k-limit-increases-to-22500-for-2023-ira-limit-rises-to-6500
        traditional_ira_contributions : int, optional
            Traditional IRA contributions. Max is 6,500 with an additional 1,000 for those 50 or older. Default is 0. Source - https://www.irs.gov/newsroom/401k-limit-increases-to-22500-for-2023-ira-limit-rises-to-6500
        pmi : int, optional
            Monthly Social Security benefits or Primary Monthly Insurance (PMI). Max is 4,555. Default is 0. Source - https://faq.ssa.gov/en-us/Topic/article/KA-01897
        sources : bool, optional
            Whether or not to return the sources of the data. Default is False.
        
        Returns:
        pandas.DataFrame: A DataFrame containing the detailed tax breakdown.
        or
        dict: where 'data' contains the DataFrame and 'sources' contains a dict of the sources.

        Note:
        The function fetches the latest tax details from external sources to perform the calculation.
        
        Sources:
        https://www.irs.gov/taxtopics/tc409
        https://www.irs.gov/taxtopics/tc559
        '''
        
        data = {
                'sources': self.sources if hasattr(self, 'sources') else sources,
                'filing_status': self.filing_status if hasattr(self, 'filing_status') else filing_status,
                'capital_gains_long': self.capital_gains_long if hasattr(self, 'capital_gains_long') else capital_gains_long,
                'capital_gains_short': self.capital_gains_short if hasattr(self, 'capital_gains_short') else capital_gains_short,
                'income': self.income if hasattr(self, 'income') else income,
                'federal_agi': self.federal_agi if hasattr(self, 'federal_agi') else federal_agi,
                'dependents': self.dependents if hasattr(self, 'dependents') else dependents,
                'birth_year': self.birth_year if hasattr(self, 'birth_year') else birth_year,
                'filers_over_65': self.filers_over_65 if hasattr(self, 'filers_over_65') else filers_over_65,
                'traditional_esp_contributions': self.traditional_esp_contributions if hasattr(self, 'traditional_esp_contributions') else traditional_esp_contributions,
                'traditional_ira_contributions': self.traditional_ira_contributions if hasattr(self, 'traditional_ira_contributions') else traditional_ira_contributions,
                'pmi': self.pmi if hasattr(self, 'pmi') else pmi
                }

        return self.__fetch__(data, 'federal-capital-gains-taxes')
    

    def fica_taxes(self, sources=False, filing_status='single', salary=100000):
        '''Federal Insurance Contributions Act (FICA)

        Parameters:
        sources : bool, optional
            Whether or not to return the sources of the data. Default is False.
        filing_status : str, optional
            Filing status for taxes. Options are 'single', 'married_jointly', 'married_separately', 'head_of_household', 'widow(er)'. Default is 'single'. Source - https://www.irs.gov/newsroom/taxpayers-should-use-the-correct-filing-status-for-accuracy-and-to-avoid-
        salary : int, optional
            Salary from employer or self-employment (ie. W2). Default is 100000.
       
        Returns:
        pandas.DataFrame: A DataFrame containing the detailed tax breakdown.
        or
        dict: where 'data' contains the DataFrame and 'sources' contains a dict of the sources.

        Note:
        The function fetches the latest tax details from external sources to perform the calculation.
        
        Sources:
        https://www.ssa.gov/oact/cola/cbb.html
        https://www.irs.gov/taxtopics/tc560#:~:text=A%200.9%25%20Additional%20Medicare%20Tax,%24200%2C000%20for%20all%20other%20taxpayers
        '''
        data = {
            'sources': self.sources if hasattr(self, 'sources') else sources,
            'filing_status': self.filing_status if hasattr(self, 'filing_status') else filing_status,
            'salary': self.salary if hasattr(self, 'salary') else salary
        }

        return self.__fetch__(data, 'fica-taxes')
    

    def social_security_taxes(self, sources=False, filing_status='single', pmi=0, income=100000, federal_deductions=0, federal_agi=75000, state_agi=0, credits_federal=0, credits_state=0, state_residence='Florida', county_residence='Other', state_occupation='Florida', county_occupation='Other', capital_gains_short=0, birth_year=1990, dependents=0, filers_over_65=0, traditional_esp_contributions=0, traditional_ira_contributions=0):
        '''
        This function calculates the amount of benefits subject to income
        taxes and subsequently the amount of taxes paid on those benefits.
        See social_security_portion_taxable and income for more information. 

        Parameters:
        sources : bool, optional
            Whether or not to return the sources of the data. Default is False.
        filing_status : str, optional
            Filing status for taxes. Options are 'single', 'married_jointly', 'married_separately', 'head_of_household', 'widow(er)'. Default is 'single'. Source - https://www.irs.gov/newsroom/taxpayers-should-use-the-correct-filing-status-for-accuracy-and-to-avoid-
        pmi : int, optional
            Monthly Social Security benefits or Primary Monthly Insurance (PMI). Max is 4,555. Default is 0. Source - https://faq.ssa.gov/en-us/Topic/article/KA-01897
        income : int, optional
            Gross income. Default is 100000.
        federal_deductions : int, optional
            Federal deductions for determining federal AGI. Default is 0. Source -  https://www.irs.gov/e-file-providers/definition-of-adjusted-gross-income, https://www.irs.gov/newsroom/taxpayers-should-know-the-difference-between-standard-and-itemized-deductions
        federal_agi : int, optional
            Adjusted Gross Income (AGI) for federal taxes. Default is 75000. Source -  https://www.irs.gov/e-file-providers/definition-of-adjusted-gross-income, https://www.irs.gov/newsroom/taxpayers-should-know-the-difference-between-standard-and-itemized-deductions
        state_agi : int, optional
            Adjusted Gross Income (AGI) for state taxes. Default is 75000.
        credits_federal : int, optional
            Credits for federal taxes. Default is 0. Source - https://www.irs.gov/credits-deductions-for-individuals
        credits_state : int, optional
            Credits for state taxes. Default is 0.
        capital_gains_short : int, optional
            Net short term capital gains. Default is 0.
        state_residence : str, optional
            State of residence. Default is 'Florida'.
        state_occupation : str, optional
            State of residence. Default is 'Florida'.
        county_residence : str, optional
            County of residence. Default is 'Other'.
        county_occupation : str, optional
            County of occupation. Default is 'Other'.
        dependents : int, optional
            Number of dependents (max 10). Default is 0. Source - https://www.irs.gov/faqs/filing-requirements-status-dependents/dependents/dependents-2
        birth_year : int, optional
            Year of birth. Options are 1923-2005. Default is 1990.
        filers_over_65 : int, optional
            Number of filers over 65. Options are 0, 1, 2. Default is 0. 
        traditional_esp_contributions : int, optional
            Traditional employer sponsored plan (401k, 403(b), and 457(b)) contributions. For 401(k)s, the max is 22,500 with an additional 7,500 those 50 or older. Default is 0. Source - https://www.irs.gov/newsroom/401k-limit-increases-to-22500-for-2023-ira-limit-rises-to-6500
        traditional_ira_contributions : int, optional
            Traditional IRA contributions. Max is 6,500 with an additional 1,000 for those 50 or older. Default is 0. Source - https://www.irs.gov/newsroom/401k-limit-increases-to-22500-for-2023-ira-limit-rises-to-6500
        
        Returns:
        pandas.DataFrame: A DataFrame containing the detailed tax breakdown.
        or
        dict: where 'data' contains the DataFrame and 'sources' contains a dict of the sources.

        Note:
        The function fetches the latest tax details from external sources to perform the calculation.
        
        Sources:
        https://www.irs.gov/pub/irs-pdf/p915.pdf
        '''

        data = {
                'sources': self.sources if hasattr(self, 'sources') else sources,
                'filing_status': self.filing_status if hasattr(self, 'filing_status') else filing_status,
                'pmi': self.pmi if hasattr(self, 'pmi') else pmi,
                'income': self.income if hasattr(self, 'income') else income,
                'federal_deductions': self.federal_deductions if hasattr(self, 'federal_deductions') else federal_deductions,
                'federal_agi': self.federal_agi if hasattr(self, 'federal_agi') else federal_agi,
                'state_agi': self.state_agi if hasattr(self, 'state_agi') else state_agi,
                'credits_federal': self.credits_federal if hasattr(self, 'credits_federal') else credits_federal,
                'credits_state': self.credits_state if hasattr(self, 'credits_state') else credits_state,
                'capital_gains_short': self.capital_gains_short if hasattr(self, 'capital_gains_short') else capital_gains_short,
                'state_residence': self.state_residence if hasattr(self, 'state_residence ') else state_residence,
                'county_residence': self.county_residence if hasattr(self, 'county_residence') else county_residence,
                'state_occupation': self.state_occupation if hasattr(self, 'state_occupation') else state_occupation,
                'county_occupation': self.county_occupation if hasattr(self, 'county_occupation') else county_occupation,
                'dependents': self.dependents if hasattr(self, 'dependents') else dependents,
                'birth_year': self.birth_year if hasattr(self, 'birth_year') else birth_year,
                'filers_over_65': self.filers_over_65 if hasattr(self, 'filers_over_65') else filers_over_65,
                'traditional_esp_contributions': self.traditional_esp_contributions if hasattr(self, 'traditional_esp_contributions') else traditional_esp_contributions,
                'traditional_ira_contributions': self.traditional_ira_contributions if hasattr(self, 'traditional_ira_contributions') else traditional_ira_contributions
                }

        return self.__fetch__(data, 'social-security-taxes')
    

    def social_security_taxable_amount(self, sources=False, filing_status='single', pmi=0, federal_agi=75000, income=100000, capital_gains_short=0, birth_year=1990, dependents=0, filers_over_65=0, traditional_esp_contributions=0, traditional_ira_contributions=0):
        '''Portion of Social Security benefits subject to taxation

        Parameters:
        sources : bool, optional
            Whether or not to return the sources of the data. Default is False.
        filing_status : str, optional
            Filing status for taxes. Options are 'single', 'married_jointly', 'married_separately', 'head_of_household', 'widow(er)'. Default is 'single'. Source - https://www.irs.gov/newsroom/taxpayers-should-use-the-correct-filing-status-for-accuracy-and-to-avoid-
        pmi : int, optional
            Monthly Social Security benefits or Primary Monthly Insurance (PMI). Max is 4,555. Default is 0. Source - https://faq.ssa.gov/en-us/Topic/article/KA-01897
        federal_agi : int, optional
            Adjusted Gross Income (AGI) for federal taxes. Default is 75000. Source -  https://www.irs.gov/e-file-providers/definition-of-adjusted-gross-income, https://www.irs.gov/newsroom/taxpayers-should-know-the-difference-between-standard-and-itemized-deductions
        income : int, optional
            Gross income. Default is 100000.
        capital_gains_short : int, optional
            Net short term capital gains. Default is 0.
        dependents : int, optional
            Number of dependents (max 10). Default is 0. Source - https://www.irs.gov/faqs/filing-requirements-status-dependents/dependents/dependents-2
        birth_year : int, optional
            Year of birth. Options are 1923-2005. Default is 1990.
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
        '''
            
        data = {
                'sources': self.sources if hasattr(self, 'sources') else sources,
                'filing_status': self.filing_status if hasattr(self, 'filing_status') else filing_status,
                'pmi': self.pmi if hasattr(self, 'pmi') else pmi,
                'federal_agi': self.federal_agi if hasattr(self, 'federal_agi') else federal_agi,
                'income': self.income if hasattr(self, 'income') else income,
                'capital_gains_short': self.capital_gains_short if hasattr(self, 'capital_gains_short') else capital_gains_short,
                'dependents': self.dependents if hasattr(self, 'dependents') else dependents,
                'birth_year': self.birth_year if hasattr(self, 'birth_year') else birth_year,
                'filers_over_65': self.filers_over_65 if hasattr(self, 'filers_over_65') else filers_over_65,
                'traditional_esp_contributions': self.traditional_esp_contributions if hasattr(self, 'traditional_esp_contributions') else traditional_esp_contributions,
                'traditional_ira_contributions': self.traditional_ira_contributions if hasattr(self, 'traditional_ira_contributions') else traditional_ira_contributions,
                }
            
        return self.__fetch__(data, 'social-security-taxable-amount')


    def social_security_benefits_factor(self, sources=False, election_age=62, election_month=0):
        '''Social Security PMI factor for early or delayed retirement

        Parameters:
        election_age : int, optional
            Age in years at Social Security benefits election. Default is the minimum, or 62. Max is 70.
        election_month : int, optional
            Month of Social Security benefits election. Default is 0 (January).
            
        Returns:
        pandas.DataFrame: A DataFrame containing the social security factor.

        Note:
        The function fetches the latest tax details from external sources to perform the calculation.
        
        Sources:
        https://www.ssa.gov/oact/ProgData/ar_drc.html
        '''

        data = {
                'sources': self.sources if hasattr(self, 'sources') else sources,
                'election_age': self.election_age if hasattr(self, 'election_age') else election_age,
                'election_month': self.election_month if hasattr(self, 'election_month') else election_month
                }
    
        return self.__fetch__(data, 'social-security-benefits-factor')


    def social_security_benefits(self, salary=100000, sources=False):
        '''Social Security Benefitseic

        Parameters:
        salary : int, optional
            Salary from employer or self-employment (ie. W2). Default is 100000.
        
        Returns:
        pandas.DataFrame: A DataFrame containing the social security benefits projcetion at ages 62, 67, and 70.
        
        Note:
        The function fetches the latest tax details from external sources to perform the calculation.
        
        Sources:
        https://www.ssa.gov/oact/cola/awiseries.html
        https://www.ssa.gov/oact/cola/cbb.html
        https://www.ssa.gov/oact/COLA/piaformula.html
        '''
        
        data = {
                'sources': self.sources if hasattr(self, 'sources') else sources,
                'salary': self.salary if hasattr(self, 'salary') else salary
                }
        
        return self.__fetch__(data, 'social-security-benefits')
    
    
    def federal_adjusted_gross_income(self, sources=False, filing_status='single', income=100000, capital_gains_short=0, dependents=0, birth_year=1990, filers_over_65=0, traditional_esp_contributions=0, traditional_ira_contributions=0, pmi=0):
        '''Federal Adjusted Gross Income (AGI)

        parameters:
        sources : bool, optional
            Whether or not to return the sources of the data. Default is False.
        filing_status : str, optional
            Filing status for taxes. Options are 'single', 'married_jointly', 'married_separately', 'head_of_household', 'widow(er)'. Default is 'single'. Source - https://www.irs.gov/newsroom/taxpayers-should-use-the-correct-filing-status-for-accuracy-and-to-avoid-
        income : int, optional
            Gross income. Default is 100000.
        capital_gains_short : int, optional
            Net short term capital gains. Default is 0.
        dependents : int, optional
            Number of dependents (max 10). Default is 0. Source - https://www.irs.gov/faqs/filing-requirements-status-dependents/dependents/dependents-2
        birth_year : int, optional
            Year of birth. Options are 1923-2005. Default is 1990.
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
        or
        dict: where 'data' contains the DataFrame and 'sources' contains a dict of the sources.

        Notes:
        The function fetches the latest tax details from external sources to perform the calculation.

        Sources: 
        https://www.irs.gov/e-file-providers/definition-of-adjusted-gross-incomehttps://www.irs.gov/newsroom/taxpayers-should-know-the-difference-between-standard-and-itemized-deductions
        '''

        data = {
                'sources': self.sources if hasattr(self, 'sources') else sources,
                'filing_status': self.filing_status if hasattr(self, 'filing_status') else filing_status,
                'income': self.income if hasattr(self, 'income') else income,
                'capital_gains_short': self.capital_gains_short if hasattr(self, 'capital_gains_short') else capital_gains_short,
                'dependents': self.dependents if hasattr(self, 'dependents') else dependents,
                'birth_year': self.birth_year if hasattr(self, 'birth_year') else birth_year,
                'filers_over_65': self.filers_over_65 if hasattr(self, 'filers_over_65') else filers_over_65,
                'traditional_esp_contributions': self.traditional_esp_contributions if hasattr(self, 'traditional_esp_contributions') else traditional_esp_contributions,
                'traditional_ira_contributions': self.traditional_ira_contributions if hasattr(self, 'traditional_ira_contributions') else traditional_ira_contributions,
                'pmi': self.pmi if hasattr(self, 'pmi') else pmi
                }
        return self.__fetch__(data, 'federal-adjusted-gross-income-(agi)')
    

    def traditional_ira_tax_deductible_amount(self, sources=False, filing_status='single', federal_agi=75000, filer_over_50=None, birth_year=1990, roth_ira_contributions=0):
        '''Traditional IRA contribution limit

        Parameters:
        sources : bool, optional
            Whether or not to return the sources of the data. Default is False.
        filing_status : str, optional
            Filing status for taxes. Options are 'single', 'married_jointly', 'married_separately', 'head_of_household', 'widow(er)'. Default is 'single'. Source - https://www.irs.gov/newsroom/taxpayers-should-use-the-correct-filing-status-for-accuracy-and-to-avoid-
        federal_agi : int, optional
            Adjusted Gross Income (AGI) for federal taxes. Default is 75000. Source -  https://www.irs.gov/e-file-providers/definition-of-adjusted-gross-income, https://www.irs.gov/newsroom/taxpayers-should-know-the-difference-between-standard-and-itemized-deductions
        filer_over_50 : bool, optional
            Whether or not the filer is over 50. Default is None. Limit can increase by 1,000 if True.
        birth_year : int, optional
            Year of birth in the event filer_over_50 is not used. Options are 1923-2005. Default is 1990.
        roth_ira_contributions : int, optional
            Traditional IRA contributions. Max is $6,500 with an additional $1,000 for those 50 or older. Default is 0. Source - https://www.irs.gov/newsroom/401k-limit-increases-to-22500-for-2023-ira-limit-rises-to-6500

        Returns:
        pandas.DataFrame: A DataFrame containing a breakdown of the limit.
        or
        dict: where 'data' contains the DataFrame and 'sources' contains a dict of the sources.

        Note:
        The function fetches the latest tax details from external sources to perform the calculation.

        Sources:
        https://www.irs.gov/retirement-plans/2023-ira-deduction-limits-effect-of-modified-agi-on-deduction-if-you-are-covered-by-a-retirement-plan-at-work
        '''

        data = {
            'sources': self.sources if hasattr(self, 'sources') else sources,
            'filing_status': self.filing_status if hasattr(self, 'filing_status') else filing_status,
            'federal_agi': self.federal_agi if hasattr(self, 'federal_agi') else federal_agi,
            'filer_over_50': self.filer_over_50 if hasattr(self, 'filer_over_50 ') else filer_over_50,
            'birth_year': self.birth_year if hasattr(self, 'birth_year') else birth_year,
            'roth_ira_contributions': self.roth_ira_contributions if hasattr(self, 'roth_ira_contributions') else roth_ira_contributions,
        }

        return self.__fetch__(data, 'traditional-ira-tax-deductible-amount')
    

    def roth_ira_contribution_limit(self, sources=False, filing_status='single', federal_agi=75000, filer_over_50=False, birth_year=1990, traditional_ira_contributions=0):
        '''Roth IRA contribution limit

        Parameters:
        sources : bool, optional
            Whether or not to return the sources of the data. Default is False.
        filing_status : str, optional
            Filing status for taxes. Options are 'single', 'married_jointly', 'married_separately', 'head_of_household', 'widow(er)'. Default is 'single'. Source - https://www.irs.gov/newsroom/taxpayers-should-use-the-correct-filing-status-for-accuracy-and-to-avoid-
        federal_agi : int, optional
            Adjusted Gross Income (AGI) for federal taxes. Default is 75000. Source -  https://www.irs.gov/e-file-providers/definition-of-adjusted-gross-income, https://www.irs.gov/newsroom/taxpayers-should-know-the-difference-between-standard-and-itemized-deductions
        filer_over_50 : bool, optional
            Whether or not the filer is over 50. Default is False. Limit can increase by 1,000 if True.
        birth_year : int, optional
            Year of birth in the event filer_over_50 is not used. Options are 1923-2005. Default is 1990.
        traditional_ira_contributions : int, optional
            Traditional IRA contributions. Max is $6,500 with an additional $1,000 for those 50 or older. Default is 0. Source - https://www.irs.gov/newsroom/401k-limit-increases-to-22500-for-2023-ira-limit-rises-to-6500
            
        Returns:
        pandas.DataFrame: A DataFrame containing a breakdown of the limit.
        or
        dict: where 'data' contains the DataFrame and 'sources' contains a dict of the sources.

        Note:
        The function fetches the latest tax details from external sources to perform the calculation.

        Sources:
        https://www.irs.gov/retirement-plans/amount-of-roth-ira-contributions-that-you-can-make-for-2023
        '''
        
        data = {
                'sources': self.sources if hasattr(self, 'sources') else sources,
                'filing_status': self.filing_status if hasattr(self, 'filing_status') else filing_status,
                'federal_agi': self.federal_agi if hasattr(self, 'federal_agi') else federal_agi,
                'filer_over_50': self.filer_over_50 if hasattr(self, 'filer_over_50 ') else filer_over_50,
                'birth_year': self.birth_year if hasattr(self, 'birth_year') else birth_year,
                'traditional_ira_contributions': self.traditional_ira_contributions if hasattr(self, 'traditional_ira_contributions') else traditional_ira_contributions
                }

        return self.__fetch__(data, 'roth-ira-contribution-limit')


    def savers_tax_credit(self, sources=False, filing_status='single', federal_agi=75000, contributions=0):
        '''Saver's Credit

        Parameters:
        sources : bool, optional
            Whether or not to return the sources of the data. Default is False.
        filing_status : str, optional
            Filing status for taxes. Options are 'single', 'married_jointly', 'married_separately', 'head_of_household', 'widow(er)'. Default is 'single'. Source - https://www.irs.gov/newsroom/taxpayers-should-use-the-correct-filing-status-for-accuracy-and-to-avoid-
        federal_agi : int, optional
            Adjusted Gross Income (AGI) for federal taxes. Default is 75000. Source -  https://www.irs.gov/e-file-providers/definition-of-adjusted-gross-income, https://www.irs.gov/newsroom/taxpayers-should-know-the-difference-between-standard-and-itemized-deductions
        contributions : int, optional
            Contributions to retirement accounts. Default is 0.
        
        Returns:
        pandas.DataFrame: A DataFrame containing the detailed tax breakdown.
        or
        dict: where 'data' contains the DataFrame and 'sources' contains a dict of the sources.

        Note:
        The function fetches the latest tax details from external sources to perform the calculation.
        
        Sources:
        https://www.irs.gov/retirement-plans/plan-participant-employee/retirement-savings-contributions-savers-credit
        '''
        
        data = {
                'sources': self.sources if hasattr(self, 'sources') else sources,
                'filing_status': self.filing_status if hasattr(self, 'filing_status') else filing_status,
                'federal_agi': self.federal_agi if hasattr(self, 'federal_agi') else federal_agi,
                'contributions': self.contributions if hasattr(self, 'contributions') else contributions
                }

        return self.__fetch__(data, 'savers-tax-credit')


    def earned_income_tax_credit(self, sources=False, filing_status='single', federal_agi=75000, dependents=0): 
        '''Earned Income Tax Credit (EIC)

        Parameters:
        sources : bool, optional
            Whether or not to return the sources of the data. Default is False.
        filing_status : str, optional
            Filing status for taxes. Options are 'single', 'married_jointly', 'married_separately', 'head_of_household', 'widow(er)'. Default is 'single'. Source - https://www.irs.gov/newsroom/taxpayers-should-use-the-correct-filing-status-for-accuracy-and-to-avoid-
        federal_agi : int, optional
            Adjusted Gross Income (AGI) for federal taxes. Default is 75000. Source -  https://www.irs.gov/e-file-providers/definition-of-adjusted-gross-income, https://www.irs.gov/newsroom/taxpayers-should-know-the-difference-between-standard-and-itemized-deductions
        dependents : int, optional
            Number of dependents (max 10). Default is 0. Source - https://www.irs.gov/faqs/filing-requirements-status-dependents/dependents/dependents-2
        
        Returns:
        pandas.DataFrame: A DataFrame containing the detailed tax breakdown.
        or
        dict: where 'data' contains the DataFrame and 'sources' contains a dict of the sources.

        Note:
        The function fetches the latest tax details from external sources to perform the calculation.
        
        Sources:
        https://www.irs.gov/credits-deductions/individuals/earned-income-tax-credit/earned-income-and-earned-income-tax-credit-eitc-tables
        '''

        data = {
                'sources': self.sources if hasattr(self, 'sources') else sources,
                'filing_status': self.filing_status if hasattr(self, 'filing_status') else filing_status,
                'federal_agi': self.federal_agi if hasattr(self, 'federal_agi') else federal_agi,
                'dependents': self.dependents if hasattr(self, 'dependents') else dependents
                }
        
        return self.__fetch__(data, 'earned-income-tax-credit')
