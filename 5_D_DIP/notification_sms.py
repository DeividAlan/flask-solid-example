from .notification_interface import NotificationInterface


class NotificationSMS(NotificationInterface):
    def send_notification(self, message: str):
        print(f"Sending SMS: {message}")