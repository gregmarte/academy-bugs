# Create a virtual environment named 'venv'
python -m venv venv

# Activate the virtual environment
# On Windows
venv\\Scripts\\activate
# On macOS/Linux
source venv/bin/activate

# Install Playwright inside the virtual environment
pip install playwright

# Install the browser binaries
playwright install

# Action: 
# Open srp.tests.py in VSCode, 
# bottom right, switch the python interpreter to the venv.