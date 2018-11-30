'''
from twilio.rest import TwilioRestClient

account_sid = "AC0e1d196147b8c2241a43f532067f73db"
auth_token="26cbaaef133f24e5dd5f429e80f4ed92"
client= TwilioRestClient(account_sid,auth_token)

message = client.sms.messages.create(
	body="hola",
	to="+59178853748",
	from_="+19282670089"
	)
print (message.id)
'''
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC0e1d196147b8c2241a43f532067f73db"
# Your Auth Token from twilio.com/console
auth_token  = "26cbaaef133f24e5dd5f429e80f4ed92"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+59178853748", 
    from_="+19282670089",
    body="se va hacer la carnita asada siono")

print(message.sid)