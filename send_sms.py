from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = ""
# Your Auth Token from twilio.com/console
auth_token  = ""

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="", 
    from_="+19389999211 ",
    body="Alert - Intrusion detected at house!")

print(message.sid)
