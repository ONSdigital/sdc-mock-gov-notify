from sdc_mock_gov_notify import app


def before_scenario(context, _step):
    app.testing = True
    context.app = app.test_client()
