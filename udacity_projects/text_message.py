# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'AC81443fb744fc4a8701f8657b9f70b8a2'
auth_token = ''
client = Client(account_sid, auth_token)

message = client.messages.create(
                              body='Hi there!',
                              from_='+17083989253',
                              to='+17087179049'
                          )

print(message.sid)
