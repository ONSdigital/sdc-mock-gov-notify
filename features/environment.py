import os
import subprocess
from time import sleep

import requests

from sdc_mock_gov_notify import app


def before_feature(context, _step):
    port = os.getenv("PORT", 3001)
    host = 'localhost'
    command = 'pipenv run gunicorn' \
              f'-b {host}:{port}' \
              '--workers 1' \
              '--timeout 60' \
              'sdc_mock_gov_notify:app'
    context.app_url = f'http://{host}:{port}'

    print(f'Starting server with command {command}')
    app.testing = True
    context.process = subprocess.Popen(command, shell=True)

    _wait_for_server(f'{context.app_url}/inbox/emails', retries=10)


def after_feature(context, _scenario):
    context.process.terminate()


def _wait_for_server(test_url, retries):
    print('Waiting for server to start')
    started = False
    while (not started) and retries > 1:
        try:
            response = requests.get(test_url, timeout=30)
            if response.status_code == requests.codes.ok:
                started = True
            else:
                print('retrying')

        except BaseException:
            print(f'retrying...')
            sleep(1)
            retries -= 1
    if not started:
        raise Exception('Failed to start server')
    print('Server started')
