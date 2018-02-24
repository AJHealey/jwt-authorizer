from jwt_decoder import decode_token


def authorizer(event, context, callback):
    token = event.authorizationToken
    header, payload, signature = decode_token(token)

    signature_algorithm = _get_algo(header)




