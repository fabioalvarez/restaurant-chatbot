import requests
from adapter.config.settings import Settings
from core.port.message import MessageGatewayPort
from core.util.message import log_http_response

_facebook_url = "https://graph.facebook.com/"


class MessageGateway(MessageGatewayPort):

    def __init__(self, settings: Settings):
        self.settings = settings

    def send_message(self, data: str) -> requests.Response:
        headers = {
            "Content-type": "application/json",
            "Authorization": f"Bearer {self.settings.access_token}",
        }

        url = (f"{_facebook_url}{self.settings.version}"
               f"/{self.settings.phone_number_id}/messages")

        # 10 seconds timeout as an example
        response = requests.post(url, data=data, headers=headers, timeout=10)

        # Raises an HTTPError if the HTTP request returned an unsuccessful status code
        response.raise_for_status()

        # Log the response
        log_http_response(response)

        return response

