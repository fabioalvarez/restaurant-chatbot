from pydantic import BaseModel
from typing import Optional


class HTTPResponse(BaseModel):
    """Standard Custom Response for HTTP Clients."""
    status: int
    msg: Optional[str]


class HealthCheck(HTTPResponse):
    """Health check response model."""
    api_version: str


class HTTPError(HTTPResponse):
    """Standard Custom Error for HTTP Clients."""
