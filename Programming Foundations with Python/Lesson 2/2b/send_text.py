from twilio.rest import TwilioRestClient
 
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "XXX"
auth_token  = "XXX"
client = TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(body="Ok then.",
    to="+XXX",    # Replace with your phone number
    from_="+XXX") # Replace with your Twilio number
print message.sid
