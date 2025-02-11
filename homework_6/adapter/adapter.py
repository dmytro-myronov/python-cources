import message_sender


class SMSService:
    """
    Service to send SMS messages.
    """

    def send_sms(self, phone_number: str, message: str) -> None:
        print(f"SMS sent to {phone_number}: {message}")


class EmailService:
    """
    Service to send Email messages.
    """

    def send_email(self, email_address: str, message: str) -> None:
        print(f"Email sent to {email_address}: {message}")


class PushService:
    """
    Service to send Push Notifications.
    """

    def send_push(self, device_id: str, message: str) -> None:
        print(f"Push notification sent to {device_id}: {message}")


class SmsAdapter(message_sender.MessageSender):
    """
    Adapter class to send SMS using SMSService.
    """

    def __init__(self, sms_service: SMSService, phone_number: str):
        """
        Initializes the SMS adapter.
        :param sms_service: Instance of SMSService
        :param phone_number: Recipient phone number
        """
        self.sms_service = sms_service
        self.phone_number = phone_number

    def send_message(self, message: str):
        """
        Sends an SMS message.
        :param message: Message content
        """
        self.sms_service.send_sms(phone_number=self.phone_number, message=message)
        print('SMS')


class EmailAdapter(message_sender.MessageSender):
    """
    Adapter class to send Emails using EmailService.
    """

    def __init__(self, email_service: EmailService, email_address: str):
        """
        Initializes the Email adapter.
        :param email_service: Instance of EmailService
        :param email_address: Recipient email address
        """
        self.email_service = email_service
        self.email_address = email_address

    def send_message(self, message: str):
        """
        Sends an Email message.
        :param message: Message content
        """
        self.email_service.send_email(email_address=self.email_address, message=message)
        print('Email')


class PushAdapter(message_sender.MessageSender):
    """
    Adapter class to send Push Notifications using PushService.
    """

    def __init__(self, push_service: PushService, device_id: str):
        """
        Initializes the Push adapter.
        :param push_service: Instance of PushService
        :param device_id: Recipient device ID
        """
        self.push_service = push_service
        self.device_id = device_id

    def send_message(self, message: str):
        """
        Sends a Push Notification.
        :param message: Message content
        """
        self.push_service.send_push(device_id=self.device_id, message=message)
        print('Push Notification')


smsService = SMSService()
sms_adapter = SmsAdapter(smsService, "+123456789")
sms_adapter.send_message("hello new client")

email_service = EmailService()
email_adapter = EmailAdapter(email_service, "test@example.com")
email_adapter.send_message("Hello via Email!")

push_service = PushService()
push_adapter = PushAdapter(push_service, "device_123")
push_adapter.send_message("Hello via Push Notification!")
