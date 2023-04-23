# example one
from abc import ABC, abstractmethod


class Notification(ABC):
    """
    wrong way
    """

    @abstractmethod
    def notify(self, message, email):
        pass


class Email(Notification):
    """
    wrong way
    """

    def notify(self, message, email):
        print(f"Send {message} to {email}")


class SMS(Notification):
    """
    wrong way
    """

    def notify(self, message, phone):
        print(f"Send {message} to {phone}")


class Contact:
    """
    wrong way
    """

    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone


class NotificationManager:
    """
    wrong way
    """

    def __init__(self, notification, contact):
        self.contact = contact
        self.notification = notification

    def send(self, message):
        if isinstance(self.notification, Email):
            self.notification.notify(message, contact.email)
        elif isinstance(self.notification, SMS):
            self.notification.notify(message, contact.phone)
        else:
            raise Exception("The notification is not supported")


# %%%%%%%%%%%%%%%%%%%%%%%%%%
# correct way


class Notification(ABC):
    """
    correct way
    """

    @abstractmethod
    def notify(self, message):
        pass


class EmailCorrect(Notification):
    """
    correct way
    """

    def __init__(self, email):
        self.email = email

    def notify(self, message):
        print(f'Send "{message}" to {self.email}')


class SMSCorrect(Notification):
    """
    correct way
    """

    def __init__(self, phone):
        self.phone = phone

    def notify(self, message):
        print(f'Send "{message}" to {self.phone}')


class NotificationManagerCorrect:
    """
    correct way
    """

    def __init__(self, notification):
        self.notification = notification

    def send(self, message):
        self.notification.notify(message)


# ********************************
# example 2


# wrong example
class MiddleEarthInhabitant(ABC):
    def dance(self):
        ...


class Human(MiddleEarthInhabitant):
    def dance(self):
        print("Going wild on the dance floor.")


class Hobbit(MiddleEarthInhabitant):
    def dance(self):
        print("Look at those big feet go.")


class Party:
    def __init__(self, guests: list[MiddleEarthInhabitant]):
        self._guests = guests

    def que_music(self):
        for guest in self._guests:
            guest.dance()


# correct way


class MiddleEarthInhabitant(ABC):
    ...


class Dancer(ABC):
    def dance(self):
        ...


class HumanCorret(MiddleEarthInhabitant, Dancer):
    def dance(self):
        print("Going wild on the dance floor.")


class HobbitCorrect(MiddleEarthInhabitant, Dancer):
    def dance(self):
        print("Look at those big feet go.")


class PartyCorrect:
    def __init__(self, guests: list[Dancer]):
        self._guests = guests

    def que_music(self):
        for guest in self._guests:
            guest.dance()
