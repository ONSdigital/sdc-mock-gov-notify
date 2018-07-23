import uuid

from flask import Flask, request, Response
import json

app = Flask(__name__)

emails = []


@app.route('/v2/notifications/email', methods=['POST'])
def send_email():
    data = json.loads(request.data)

    emails.append(data)

    template_id = 'https://api.notifications.service.gov.uk/templates/' + \
                  data["template_id"]

    response = {'id': str(uuid.uuid4()),
                'reference': data['reference'],
                'template': {
                    'version': 1,
                    'id': data['template_id'],
                    'uri': template_id},
                'content': {
                    'body': json.dumps(data),
                    'subject': 'An example subject'}
                }

    return Response(response=json.dumps(response),
                    status=201, mimetype='application/json')


@app.route('/inbox/emails', methods=['GET'])
def get_emails():
    return json.dumps(emails), 200


@app.route('/inbox/emails', methods=['DELETE'])
def clear_emails():
    emails.clear()
    return json.dumps({'success': True}), 200
