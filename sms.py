from twilio.rest import Client

account_sid = 'AC775edf2839969f82c46f94fb6fce68e5'
auth_token = '7f7b2c8f58dfef7ec501b4b613064fe4'
client = Client(account_sid, auth_token)

message = client.messages.create(
    messaging_service_sid='MGb894dc095c06a02ef225bdc62c453ded',
    body='Mein Apke bare me sb janta hu!! Hehehehe ',
    to='+916378378839'
)

print(message.sid)