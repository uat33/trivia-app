# this will take care of the getting questions

# import the requests module
import requests



# make this here so number of questions can be changed with minimal hassle
AMOUNT_OF_QUESTIONS = 10

# set the api link as constant
URL = "https://opentdb.com/api.php"

# give the parameters
parameters = {
    "amount": AMOUNT_OF_QUESTIONS, # number of questions
    "type": "boolean" # true or false
}

# form the requests
response = requests.get(url=URL, params=parameters)
response.raise_for_status() # get the status
question_data = response.json()['results'] # parse into json, and get the results of the api call
