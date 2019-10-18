## Local installation

These instructions are written primarily for Ubuntu Linux.  
**For other operating systems:** you may need to change the commands used for activating the virtual environment, but all pip and heroku commands should be the same.  
Please refer to a search engine for installation the following on your OS:  
- Python 3 (or higher), which should come built in with pip and [venv](https://docs.python.org/3/tutorial/venv.html).  
- SQLite 3  

## Ubuntu

Remember to update first with sudo `apt-get update`, then run the following commands:  
`sudo apt-get install python3`  
`sudo apt-get install sqlite3`  

1. Download the project .zip file and extract it, or clone the repo by any other means you choose. Open the command prompt and navigate to the project folder.
2. Create a virtual environment for the project with the command  
`python3 -m venv venv`  
and activate it with the command  
`source venv/bin/activate`  
This way any depencendies we're going to install don't interfere with any other projects on the machine.  
3. Make sure you have updated pip with  
`pip install --upgrade pip`
4. Install project dependencies with  
`pip install -r requirements.txt`
5. You're ready to run the project, yay! Run the program with  
`python3 run.py` and navigate to [localhost:5000/](localhost:5000) to begin using it.


Always remember to activate the virtual environment with `source venv/bin/activate` before you run the program.


## Running the project on Heroku

1. Install the project locally.  
2. Make sure you have a Heroku account, create one if not.  
3. Install the heroku CLI by following the instructions [here.](https://devcenter.heroku.com/articles/heroku-cli)  
4. Navigate to the project folder in your terminal if you aren't there already, and create an instance for the project on heroku's side with  
`heroku create PROJECT_NAME` (replace PROJECT_NAME with whatever you want to name this instance)
5. Initiate the persistent PostgreSQL database environment (you may skip this step if you do not want the Heroku app to have a persistent database):
`heroku config:set HEROKU=1`
`heroku addons:add heroku-postgresql:hobby-dev`  
6. Add project version control to Heroku:
`git remote add heroku https://git.heroku.com/PROJECT_NAME.git`  
7. Deploy the project files to Heroku:
`git add .`
`git commit -m"You may add any short, descriptive message here! eg. Deploying to Heroku"`
`git push heroku master`
8. You're done! The Heroku instance is now visible in the address `https://PROJECT_NAME.herokuapp.com` and any future changes you make to the files can be deployed using the commands in step 6.