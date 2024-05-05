from tests.fixtures import mongodb
from python_rest_api.model.user import User, user_with_id
import python_rest_api.helpers as hlp
import pytest
import uuid


def test_writing_user(mongodb):
    user = user_with_id(
        {
            'first_name': "Manni",
            'last_name': "Mensch",
            'email_address': "bla@blub.com"
        }
    )

    user.save()

    retrieved = User.objects[0]

    assert retrieved.first_name == user.first_name
    assert retrieved.last_name == user.last_name


def test_unique_email_address(mongodb):
    u1 = user_with_id(
        {
            'first_name': "Manni",
            'last_name': "Mensch",
            'email_address': "bla1@blub.com"
        }
    )

    u2 = user_with_id(
        {
            'first_name': "Manni",
            'last_name': "Mensch",
            'email_address': "bla1@blub.com"
        }
    )

    u1.save()

    with pytest.raises(Exception):
        u2.save()


def test_unique_domain_id(mongodb):
    non_unique_id = hlp.random_id()

    u1 = User(
        domain_id=non_unique_id,
        first_name="bla",
        last_name="blub",
        email_address="mail1"
    )

    u2 = User(
        domain_id=non_unique_id,
        first_name="bla",
        last_name="blub",
        email_address="mail2"
    )

    u1.save()

    with pytest.raises(Exception):
        u2.save()
