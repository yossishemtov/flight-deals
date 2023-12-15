from twilio.rest import Client
import os

# Retrieve Twilio credentials and phone numbers from environment variables
twilio_sid = os.environ.get("TWILIO_SID")
twilio_auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
twilio_virtual_number = os.environ.get("TWILIO_VIRTUAL_NUMBER")
twilio_verified_number = os.environ.get("TWILIO_VERIFIED_NUMBER")

class NotificationManager:
    """
    The NotificationManager class is responsible for sending SMS notifications using the Twilio API.
    It requires Twilio SID, authentication token, virtual number, and verified number to operate.
    """

    def __init__(self):
        """
        Initializes a new instance of the NotificationManager class.

        The Twilio client is created using the provided Twilio SID and authentication token.
        """
        self.client = Client(twilio_sid, twilio_auth_token)

    def send_sms(self, message):
        """
        Sends an SMS notification using the Twilio API.

        :param message: The text message to be sent in the SMS.
        """
        # Create an SMS message using the Twilio client
        sms_message = self.client.messages.create(
            body=message,
            from_=twilio_virtual_number,
            to=twilio_verified_number,
        )

        # Print the SID if the SMS was successfully sent
        print(sms_message.sid)
