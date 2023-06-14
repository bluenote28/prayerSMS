import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

proxy_client = TwilioHttpClient()
proxy_client.session.proxies = {'https': os.environ['https_proxy']}

morning_offering = "O Jesus, through the Immaculate Heart of Mary, I offer you my prayers, works, joys, \
and sufferings of this day for all the intentions of your Sacred Heart in union with the Holy Sacrifice \
 of the Mass throughout the world, for the salvation of souls, the reparation of sins, the reunion of \
all Christians, and in particular for the intentions of the Holy Father this month. Amen."




account_sid = os.environ["account_sid"] #twilio account SID environment variable
auth_token = os.environ["auth_token"] #twilio authorization token environemnt variable
client = Client(account_sid, auth_token)
message = client.messages.create(
  body=morning_offering,
  from_="+",
  to="+" 
)

