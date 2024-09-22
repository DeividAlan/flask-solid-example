from .notification_interface import NotificationInterface


class ClientService:
    def __init__(self, notification: NotificationInterface) -> None:
        self.notification = notification

    def send(self, message: str) -> None:
        self.notification.send_notification(message)