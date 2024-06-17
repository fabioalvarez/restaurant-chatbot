from adapter.config.settings import Settings
from models.message import MessageModel
from abc import ABCMeta, abstractmethod


class MessageGatewayPort(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, settings: Settings):
        self.settings = settings

    @abstractmethod
    def send_message(self, data: str):
        pass


class MessageServicePort(metaclass=ABCMeta):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def send_message(self, payload: MessageModel):
        pass


