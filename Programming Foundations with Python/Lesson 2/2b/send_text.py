## needed to add directory to path
import os.path, sys
## adding directory outside of repository to path
sys.path.append("C:\Users\William\Projects\python\Udacity - Non Github\AuthTokens")
## to import the real auth data
import twilioauth


from twilio.rest import TwilioRestClient
auth_data = twilioauth.TwilioAuth()

print(auth_data.to)
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = auth_data.account_sid
auth_token  = auth_data.auth_token
client = TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(body="Morning Mom, Are you going to be able to give me a ride tomorrow? I can ride the bus.",
    to=auth_data.to,    # Replace with your phone number
    from_=auth_data.from_) # Replace with your Twilio number
print message.sid
