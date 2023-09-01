# OSI Finance API

The OSI Finance API is a Python library for accessing OSI Finanance's financial calculators. The library enables developers to programmatically calculate taxes, social security, and other financial topics.

## Installation
You can install the OSI Finance API with pip:

pip install osifinance api

## Documentation
Full documentation is available at Read the Docs.

## Contributing
Want to help us improve the OSI Finance API? Check out our Contributing Guide to learn about running CanvasAPI as a developer, picking issues to work on, submitting bug reports, contributing patches, and more.

Quickstart
Getting started with the OSI Finance API is easy.

Like most API clients, the OSI Finance API exposes a single class that provides access to the rest of the API: Osifinance.

The first thing to do is instantiate a new Osifinance object by providing your Osifinance instance’s root API URL and a valid API key. Additionally, you can include constant financial data such as your filing status or salary.

'''
# Import the Osifinance class
from osifinanceapi import Osifinance
from osifinanceapi import states

# OSI Finance API key
API_KEY = "p@$$w0rd"

# Initialize a new Osifinance object
osi = Osifinance(API_KEY)

You can now use osi to begin making API calls.

Working with Osifinance Objects
The OSI Finance API converts the JSON responses from the host website into Pandas dataframes.

# Get income taxes
>>> df_income_taxes = osi.taxes_income(filing_status='single', agi=100000)

# Access the total taxes
>>> df_income_taxes.taxes.total

# State tax information can be found in the respective state files
>>> help(osi.states.alabama)
>>> help(osi.states.alabama.income)
'''

## Contact Us
Need help? Have an idea? Feel free to check out our Discussions board. Just want to say hi or get extended spport? Come join us on the UCF Open Slack Channel and join the #cosifinanceapi channel!
