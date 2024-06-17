import logging
import requests
from adapter.config.settings import Settings
from models.message import MessageModel
from core.port.message import MessageServicePort
from adapter.handler import response


class MessageHandler:

    def __init__(self, service: MessageServicePort, settings: Settings):
        self.service = service
        self.settings = settings

    def verify(self, mode, token, challenge: str):
        if mode and token:
            # Check the mode and token sent are correct
            if mode == "subscribe" and token == self.settings.verify_token:
                # Respond with 200 OK and challenge token from the request
                logging.info("WEBHOOK_VERIFIED")
                return challenge, 200
            else:
                # Responds with '403 Forbidden' if verify tokens do not match
                logging.info("VERIFICATION_FAILED")
                return response.verification_failed
        else:
            # Responds with '400 Bad Request' if verify tokens do not match
            logging.info("MISSING_PARAMETER")
            return response.missing_parameters

    def send_message(self, payload: MessageModel) -> (str, int):
        """
        Handle incoming webhook events from the WhatsApp API.
        This function handles incoming WhatsApp messages and other events,
        pass the information to be processed and returns a response.

        Returns:
            response: Tuple with message and status code.
        """
        # The result is the same.

        if payload.is_status_update:
            logging.info("Received a WhatsApp status update.")
            return response.ok

        if not payload.is_valid_message:
            logging.error("Not a WhatsApp API event")
            return response.no_event

        try:
            self.service.send_message(payload)
        except requests.Timeout:
            logging.error("Timeout occurred while sending message")
            return response.timeout_error
        except requests.RequestException as e:
            logging.error(f"Request failed due to: {e}")
            return response.request_failed

        return response.ok
