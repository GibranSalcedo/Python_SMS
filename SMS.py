from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC92d8d30dea871853f9b0eb383d9beab9"
# Your Auth Token from twilio.com/console
auth_token  = "df1b011254e5e16dc4808ffc617520dd"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+1525571504017", 
    from_="+1525563310656",
    body="Hello from Python!")

print(message.sid)