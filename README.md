# Clone the flight booking application

# cd into the app 

# create a virtual env : python3 -m venv venv
# Activate th venv   : source venv/bin/activate
# run pip install requirements.txt to install all dependencies
# Run

'''
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
'''
start app with 

# python3 app.py  or  flask run 

# It Will open Port  localhost: 5000

# you will see these when started

 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 243-160-191



 # Create and activate a virtual environment (if not already done)
python3 -m venv venv
source venv/bin/activate  # On macOS/Linux
# venv\Scripts\activate  # On Windows

# Install the required dependencies
pip install -r requirements.txt

# Set environment variables
export FLASK_APP=app.py   # On macOS/Linux
# set FLASK_APP=app.py   # On Windows
export FLASK_ENV=development   # On macOS/Linux
# set FLASK_ENV=development   # On Windows

# Run the Flask app
flask run /python app.py
