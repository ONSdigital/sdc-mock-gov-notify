from urllib.parse import quote_plus

from behave import *

import requests
from nose.tools import assert_equals
from notifications_python_client import NotificationsAPIClient


@given(u'an email is sent to Gov Notify to "{email_address}"')
def send_email_to_gov_notify(context, email_address):
    service_id = 'S' * 32
    api_id = 'A' * 32
    api_key = api_id + service_id

    client = NotificationsAPIClient(api_key, base_url=f'{context.app_url}')

    client.send_email_notification(
        email_address=email_address,
        template_id='this-is-a-uuid',
        personalisation={'name': 'Tom'},
        reference='example-reference')


@when(u'I check the global email inbox')
def check_inbox(context):
    response = requests.get(f'{context.app_url}/inbox/emails')

    assert_equals(200, response.status_code)

    context.emails = response.json()


@when('I check the email inbox for "{email_address}"')
def check_inbox_for(context, email_address):
    endpoint = f'{context.app_url}/inbox/emails/{quote_plus(email_address)}'
    response = requests.get(endpoint)

    assert_equals(200, response.status_code)

    context.emails = response.json()


@when(u'I clear the email inbox')
def clear_inbox(context):
    response = requests.delete(f'{context.app_url}/inbox/emails')
    assert_equals(200, response.status_code)


@then(u'I should see {email_count:d} email sent to "{email_address}"')
def assert_last_email(context, email_count, email_address):
    assert_equals(len(context.emails), email_count)


@then(u'there should be no emails in the inbox')
def assert_number_of_emails(context):
    check_inbox(context)

    assert_equals(0, len(context.emails))
