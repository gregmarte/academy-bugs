# Create a virtual environment named 'venv'
python -m venv .venv

# Activate the virtual environment (mac)
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Update dependencies to the latest version
pip install pip-tools
pip-compile requirements.in

# Install the browser binaries
playwright install

# Action: 
# Open srp.tests.py in VSCode, 
# bottom right, switch the python interpreter to the .venv.


# Sites to potentially test
# https://ultimateqa.com/dummy-automation-websites/
# https://suitecrm.com/demo/
# https://practicesoftwaretesting.com/
# https://practice.expandtesting.com/
# https://github.com/christianbaumann/personal-knowledge-base/blob/master/links/testautomation.md#practice-sites
