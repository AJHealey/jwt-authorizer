import json

from jwt_encoder import sign_with_hs256


def signature_is_valid(header, payload, signature):
    is_valid = False
    try:
        algorithm = _get_algo(header)
        if algorithm is 'HS256':
            expected_signature = sign_with_hs256(header, payload, 'secret')
            is_valid = expected_signature.equals(signature)
    except:
        pass

    return is_valid


def _get_algo(header):
    header = json.loads(header)
    return header['alg'] if 'alg' in header else None