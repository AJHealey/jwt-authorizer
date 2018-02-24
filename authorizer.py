import os

from jwt_decoder import decode_token
from jwt_validator import signature_is_valid


def authorizer(event: dict, context, callback: staticmethod) -> None:
    secret = os.getenv('SECRET', "")
    token = event['authorizationToken']
    header, payload, signature = decode_token(token)

    if signature_is_valid(header, payload, signature, secret):
        try:
            callback(None, generate_policy_for(payload))
        except:
            raise Exception('Deny')
    else:
        raise Exception('Unauthorized')


def generate_policy_for(payload: dict) -> dict:
    policy = {
        "principalId": '',
        "policyDocument": {
            "Version": "2012-10-17",
            "Statement": {
                "Action": "execute-api:Invoke",
                "Effect": "Allow",
                "Resource": _get_allowed_resource(payload)
            }
        },
        'principalId': payload.get('username', 'anon')}

    return policy


def _get_allowed_resource(payload: dict) -> list:
    resources = []
    is_admin = payload.get('admin', False)
    if is_admin:
        resources.append('*')

    else:
        # Handle custom role
        pass

    return resources







