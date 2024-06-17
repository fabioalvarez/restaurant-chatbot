from pydantic import BaseModel, Field, model_validator
from typing import List, Optional


class Text(BaseModel):
    body: str


class Message(BaseModel):
    from_value: str = Field(..., alias="from")
    type_value: str = Field(..., alias="type")
    timestamp: str
    text: Text
    id: str


class Profile(BaseModel):
    name: str


class Contact(BaseModel):
    profile: Profile
    wa_id: str


class Pricing(BaseModel):
    billable: bool
    pricing_model: str
    category: str


class Origin(BaseModel):
    type: str


class Conversation(BaseModel):
    id: str
    expiration_timestamp: str
    origin: Origin


class Status(BaseModel):
    id: str
    status: str
    timestamp: str
    recipient_id: str
    conversation: Conversation
    pricing: Pricing


class Metadata(BaseModel):
    display_phone_number: str
    phone_number_id: str


class Value(BaseModel):
    messaging_product: str
    metadata: Metadata
    statuses: Optional[List[Status]] = Field(None)
    contacts: Optional[List[Contact]] = Field(None)
    messages: Optional[List[Message]] = Field(None)


class Changes(BaseModel):
    field: str
    value: Value


class Entry(BaseModel):
    id: str
    changes: List[Changes]


class MessageModel(BaseModel):
    """Standard Message Request from Whatsapp"""
    object: str
    entry: Optional[List[Entry]] = Field(None)
    message: Optional[str] = Field(None)
    wa_id: Optional[str] = Field(None)
    is_status_update: Optional[bool] = Field(False)
    is_valid_message: Optional[bool] = Field(False)

    # @model_validator(mode='after')
    # def validate_json(self):
    #     logging.error("Failed to decode JSON")
    #     Raise Error isn't valid
    #     response.invalid_json
    #     pass

    @model_validator(mode='after')
    def check_status(self):
        """Check status of message"""
        if self.entry[0].changes[0].value.statuses:
            self.is_status_update = True
        return self

    @model_validator(mode="after")
    def check_messages(self):
        """Check if a message is valid"""
        if (self.object
                and self.entry
                and self.entry[0].changes
                and self.entry[0].changes[0].value
                and self.entry[0].changes[0].value.messages
                and self.entry[0].changes[0].value.messages[0]):

            value = self.entry[0].changes[0].value

            self.message = value.messages[0].text.body
            self.wa_id = value.contacts[0].wa_id

            self.is_valid_message = True

        return self


{
    "object": "asdasd",
    "entry": [
        {
            "message": "asdasd"
        }
    ]
}