
from twilio.rest import Client

TWILIO_SID = "AC5445f48d0268120d008a52e58253304b"
TWILIO_AUTH_TOKEN = "d75d9155e5daeb5987bf7fbd8fcc831b"
TWILIO_VIRTUAL_NUMBER = '+19362373772'
TWILIO_VERIFIED_NUMBER = '+6591608840'


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)