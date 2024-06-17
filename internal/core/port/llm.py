from abc import abstractmethod, ABCMeta
from models.message import MessageModel


class LlmGatewayPort(metaclass=ABCMeta):
    @abstractmethod
    def generate_response(self, payload: MessageModel):
        pass

    def process_text_for_whatsapp(self, response: str):
        pass
