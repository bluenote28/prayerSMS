import os
import random
from twilio.rest import Client

prayers = ["Pray three hail mary's for the souls in purgatory",
           "Pray three our fathers for more priests",
           "Pray three our fathers for the holy father",
           "Pray three our fathers for fallen away catholics",
           "Pray three our fathers for persecuted christians",
           "Pray three our fathers for those who are dying",
           "Pray three our fathers for the conversion of your family members",
           "Pray three our fathers for the protection of priests and bishops",
           "Pray three our fathers for the conversion of protestants"
           ]

prayer_choice = random.randrange(len(prayers) - 1)

account_sid = os.environ['account_sid'] #twilio account sid environment variable
auth_token = os.environ['auth_token'] #twilio auth token environment varibale
client = Client(account_sid, auth_token)
message = client.messages.create(
  body=prayers[prayer_choice],
  from_="+", #add twilio number
  to="+" #add your number
)


