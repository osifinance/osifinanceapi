![PyPI Latest Release](https://badge.fury.io/py/osifinanceAPI.svg)
[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)


# osifinanceAPI: Python API for OSI Finance REST API
osifinanceAPI is a Python package for accessing OSI Finance's financial calculators. The library enables developers to programmatically calculate taxes, social security, and other tax-related values.


## Installation
You can install osifinanceAPI with pip:

```
pip install osifinanceAPI
```
Additional information can be found at https://pypi.org/project/osifinanceAPI/0.1.1/


## Documentation
Full documentation is available [here](https://osifinance.com/docs/osifinanceAPI).


## Quickstart
Getting started with osifinanceAPI is easy.

Like most API clients, osifinanceAPI uses a parent class that provides access to nearly the entirety of the API: Osifinance.

The first thing to do is instantiate a new Osifinance object by providing your Osifinance instance’s root API URL and a valid API key. Additionally, you can include constant financial data such as your filing status or salary.

```ruby
# Import the Osifinance class
from osifinanceAPI import Osifinance

# OSI Finance API key
API_KEY = "p@$$w0rd"

# Initialize a new Osifinance object
osi = Osifinance(API_KEY)

# You can now use osi to begin making API calls.

# Working with Osifinance Objects
# osifinanceAPI converts the JSON responses from the host website into Pandas dataframes

# Get income taxes
df_income_taxes = osi.income_taxes(filing_status='single', agi=100000)

# Access the total taxes
df_income_taxes.taxes.total

# State tax information can be found using the StateTaxes Class
from osifinanceAPI import StateTaxes

# Initialize a new StateTaxes object
state_taxes = StateTaxes(API_KEY)

alabama_taxes = state_taxes.alabama(agi=100000)

# Alternatively, you can access a sources dict by passing in sources=True
alabama_taxes = state_taxes.alabama(agi=100000, sources=True)
alabama_taxes['sources']

# To access the dataframe in this case, you must access the data key first
alabama_taxes['data'] 
```


## Contact Us
Need help? Have an idea? Feel free to check out our [Discussions board](https://osifinance.canny.io).


## Disclaimer
I undestand that OSI Finance reads my financial information when performing calculations and does not store any of my information. For more information, please visit our [Legal Disclaimer](https://osifinance.com/legal-disclaimer).
