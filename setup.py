from setuptools import setup

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='osifinanceAPI',
    version='0.1.0',
    packages=['osifinanceAPI'],
    description='Python toolkit for interacting with the OSI Finance API',
    long_description=long_description,
    long_description_content_type='text/markdown',
    python_requires='>=3.7',
    install_requires=['pandas>=1.3.5']
)
