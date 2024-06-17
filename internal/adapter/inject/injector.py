from adapter.config.settings import Settings
from core.port.llm import LlmGatewayPort
from adapter.gateway.llm import LlmGateway
from core.port.message import MessageServicePort, MessageGatewayPort
from core.service.message import MessageService
from adapter.gateway.message import MessageGateway
from adapter.handler.message import MessageHandler


class Gateways:
    def __init__(self, settings: Settings):
        self.replier: MessageGatewayPort = MessageGateway(settings)
        self.llm: LlmGatewayPort = LlmGateway(settings)


class Services:
    def __init__(self, gateways: Gateways):
        self.message: MessageServicePort = MessageService(gateways.llm, gateways.replier)


class Handlers:
    def __init__(self, service: Services, settings: Settings):
        self.message = MessageHandler(service.message, settings)


class Injector:
    def __init__(self):
        self.settings = Settings()
        self.gateways: Gateways = Gateways(self.settings)
        self.services: Services = Services(self.gateways)
        self.handlers: Handlers = Handlers(self.services, self.settings)
