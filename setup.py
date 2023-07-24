from setuptools import setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name='google_spreadsheets_exporter',
    version='1.0.2',
    packages=['google_spreadsheets_exporter'],
    install_requires=[
        'google-api-python-client',
        'google-auth-httplib2',
        'google-auth-oauthlib',
    ],
    exclude_package_data={'google_spreadsheets_exporter': ['creds.json', 'test.py']},
    long_description=long_description,
    long_description_content_type="text/markdown",
)