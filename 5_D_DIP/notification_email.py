from .notification_interface import NotificationInterface


class NotificationEmail(NotificationInterface):
    def send_notification(self, message: str):
        print(f"Sending Email: {message}")