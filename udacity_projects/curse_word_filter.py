# # Download the helper library from https://www.twilio.com/docs/python/install
# from twilio.rest import Client


# # Your Account Sid and Auth Token from twilio.com/console
# # DANGER! This is insecure. See http://twil.io/secure
# account_sid = 'AC81443fb744fc4a8701f8657b9f70b8a2'
# auth_token = 'a1abdca177de368b19c31e6a85998337'
# client = Client(account_sid, auth_token)

# message = client.messages.create(
#                               body='Hi there!',
#                               from_='+17083989253',
#                               to='+17087179049'
#                           )

# print(message.sid)
from urllib import request, parse

def read_text():
    quotes = open("./message.txt")
    content = quotes.read()

    quotes.close()
    check_curse_word(content)



def check_curse_word(txt):
    url = "http://www.wdylike.appspot.com/?q="
    connection = url + parse.quote(txt)
    req = request.urlopen(connection)
    answer = req.read()
    print(answer)
    req.close()

read_text()