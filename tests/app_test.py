import json
import unittest
from uuid import UUID

from sdc_mock_gov_notify import app


class AppTest(unittest.TestCase):
    TEMPLATE_ID = '288de68c-f407-4290-92d8-97d84d885e44'
    VALID_SEND_EMAIL_REQUEST = {'email_address': 'tom@example.com',
                                'template_id': TEMPLATE_ID,
                                'personalisation': {'name': 'Tom'},
                                'reference': 'example-reference'}

    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def assertUUID(self, string):
        UUID(string)

    def test_send_email_returns_a_200_status_code(self):
        response = self.app.post(
            '/v2/notifications/email',
            data=json.dumps(self.VALID_SEND_EMAIL_REQUEST),
            content_type='application/json')

        self.assertEqual(201, response.status_code)

    def test_send_email_returns_a_valid_JSON_object(self):
        response = self._send_email_request()
        self.assertIsInstance(response, dict)

    def test_send_email_returns_templateVersion_of_1(self):
        response = self._send_email_request()
        self.assertEqual(1, response['templateVersion'])

    def test_send_email_returns_the_provided_reference(self):
        response = self._send_email_request({'reference': 'this-reference'})
        self.assertEqual('this-reference', response['reference'])

        response = self._send_email_request({'reference': 'another-reference'})
        self.assertEqual('another-reference', response['reference'])

    def test_send_email_returns_the_provided_template_id(self):
        override = {'template_id': '56f9c46c-4672-4cf7-80bf-1f9265e42fba'}
        response = self._send_email_request(override)
        self.assertEqual(
            '56f9c46c-4672-4cf7-80bf-1f9265e42fba',
            response['templateId'])

        override = {'template_id': '92276bc9-1b88-42ff-8a0a-8a0bcdaf43e7'}
        response = self._send_email_request(override)
        self.assertEqual(
            '92276bc9-1b88-42ff-8a0a-8a0bcdaf43e7',
            response['templateId'])

    def test_send_email_returns_notificationId_as_a_UUID(self):
        response = self._send_email_request()
        self.assertUUID(response['notificationId'])

    def test_send_email_returns_a_template_URI_with_template_id(self):
        override = {'template_id': '915ceb17-de9b-466c-beeb-25c9e49a1aa4'}
        response = self._send_email_request(override)
        self.assertEqual(
            'https://api.notifications.service.gov.uk/templates/'
            '915ceb17-de9b-466c-beeb-25c9e49a1aa4',
            response['templateUri'])

        override = {'template_id': 'd92c7ae3-d9c9-454d-8401-cf6bb4c35581'}
        response = self._send_email_request(override)
        self.assertEqual(
            'https://api.notifications.service.gov.uk/templates/'
            'd92c7ae3-d9c9-454d-8401-cf6bb4c35581',
            response['templateUri'])

    def test_send_email_returns_the_body_containing_the_requested_JSON(self):
        response = self._send_email_request()
        self.assertEqual(
            self.VALID_SEND_EMAIL_REQUEST,
            json.loads(response['body']))

    def test_send_email_returns_a_static_subject(self):
        response = self._send_email_request()
        self.assertEqual('An example subject', response['subject'])

    def test_send_email_returns_unique_notification_ids(self):
        uuid1 = self._send_email_request()['notificationId']
        uuid2 = self._send_email_request()['notificationId']

        self.assertNotEqual(uuid1, uuid2)

    def _send_email_request(self, override={}):
        data = self.VALID_SEND_EMAIL_REQUEST.copy()
        data.update(override)

        response = self.app.post(
            '/v2/notifications/email',
            data=json.dumps(data),
            content_type='application/json')
        body = json.loads(response.data)
        return body
