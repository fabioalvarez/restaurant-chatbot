from adapter.config.settings import Settings
from core.port.llm import LlmGatewayPort
from models.message import MessageModel


class LlmGateway(LlmGatewayPort):
    def __init__(self, settings: Settings):
        self.settings = settings

    def generate_response(self, payload: MessageModel) -> str:
        return ""

    def process_text_for_whatsapp(self, response: str) -> str:
        return ""
