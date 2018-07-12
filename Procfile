# workers has to be set to 1 as the app currently only has in-memory storage
web: gunicorn -b 0.0.0.0:$PORT --workers 1 --timeout 60 sdc_mock_gov_notify:app
