from mongoengine import Document, StringField, DateTimeField, UUIDField
from datetime import datetime, UTC
import uuid


class User(Document):
    domain_id = UUIDField()
    first_name = StringField(min_length=1, max_length=200, required=True)
    last_name = StringField(min_length=1, max_length=200, required=True)
    email_address = StringField(max_length=200, required=True)
    date_modified = DateTimeField(default=datetime.now(UTC))

    meta = {
        "indexes": [
            {
                'fields': ["email_address"],
                'unique': True
            },
            {
                'fields': ['domain_id'],
                'unique': True
            }
        ]
    }


def user_with_id(kwargs: dict) -> User:
    return User(
        domain_id=uuid.uuid4(),
        **kwargs
    )
