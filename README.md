# SDC Mock GOV.UK Notify

[![Build Status](https://travis-ci.org/ONSdigital/sdc-mock-gov-notify.svg?branch=master)](https://travis-ci.org/ONSdigital/sdc-mock-gov-notify)

## Motivation

This service has been built to enable the testing of user journeys which
require email verification.

## API

### GOV.UK Notify Endpoints

#### `POST /gov_notify_api/v2/notifications/email`
This endpoint receives _send email_ requests for the official GOV.UK Notify API
packages and adds them to the email inbox.

### Programatic Endpoints

#### `GET /inbox/emails`
Get all emails in the inbox in JSON format.

#### `DELETE /inbox/emails`
Clear the inbox.
