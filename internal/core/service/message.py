import logging

from core.port.llm import LlmGatewayPort
from models.message import MessageModel
from core.port.message import MessageServicePort, MessageGatewayPort
from core.util.message import generate_response, get_message_body


class MessageService(MessageServicePort):
    _instance = None

    def __init__(self, openai: LlmGatewayPort, replier: MessageGatewayPort):
        self.openai = openai
        self.replier = replier

    def __new__(cls, openai: LlmGatewayPort, replier: MessageGatewayPort):
        """Singleton Pattern"""
        if cls._instance is None:
            cls._instance = super(MessageService, cls).__new__(cls)
        return cls._instance

    def send_message(self, payload: MessageModel):
        """
        This function processes incoming WhatsApp messages and other events,
        such as delivery statuses.Every message send will trigger 4 HTTP requests
        to your webhook: message, sent, delivered, read.

        Returns:
            err: bool indicating if the process is successful
        """

        # TODO: implement custom function here
        response = generate_response(payload.message)

        # OpenAI Integration
        # response = self.openai.generate_response(payload)
        # response = self.openai.process_text_for_whatsapp(response)
        # response = generate_response(message_body, wa_id, name)
        # response = process_text_for_whatsapp(response)

        data = get_message_body(payload.wa_id, response)
        logging.info("request body: ", data)
        self.replier.send_message(data)
