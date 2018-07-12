from flask import Flask, request, Response
import json

app = Flask(__name__)

emails = []


@app.route('/gov_notify_api/v2/notifications/email', methods=['POST'])
def send_email():
    data = json.loads(request.data)

    emails.append(data)
    return Response(response="{}", status=200, mimetype="application/json")


@app.route('/inbox/emails', methods=['GET'])
def get_emails():
    return json.dumps(emails), 200


@app.route('/inbox/emails', methods=['DELETE'])
def clear_emails():
    emails.clear()
    return 'OK', 200