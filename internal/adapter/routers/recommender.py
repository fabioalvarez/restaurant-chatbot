from adapter.inject.injector import Injector
from models.http import HTTPResponse
from models.message import MessageModel
from fastapi import APIRouter, Depends, Response, Query
from typing import Annotated

router = APIRouter()


@router.get("/webhook")
def verify(
        response: Response,
        injector: Annotated[Injector, Depends()],
        mode: str = Query(..., alias="hub.mode"),
        token: str = Query(..., alias="hub.verify_token"),
        challenge: str = Query(..., alias="hub.challenge"),
):
    msg, status = injector.handlers.message.verify(mode, token, challenge)
    response.status_code = status
    return msg, status


@router.post("/webhook")
def chatbot(
        response: Response,
        payload: MessageModel,
        injector: Annotated[Injector, Depends()],
) -> HTTPResponse:
    """
    Allows communication between users and Open AI, also books reservations.

    Args:
    response (Response): FastAPI Response object associated with the current call.
    payload: (MessageModel): Request model from WhatsApp API.

    Returns:
    HTTPResponse: A response model containing the HTTP status code and response
    message.
    """

    msg, status = injector.handlers.message.send_message(payload)
    response.status_code = status
    return HTTPResponse(msg=msg, status=status)
