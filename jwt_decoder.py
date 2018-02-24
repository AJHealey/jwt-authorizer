import base64 as b64
import binascii

from models import MalformedTokenException


def decode_token(token):
    try:
        padded_token = _add_missing_padding(token)
        header, payload, signature = padded_token.split('.')
        return b64.b64decode(header), b64.b64decode(payload), b64.b64decode(signature)
    except binascii.Error:
        raise Exception('Cannot decode token')
    except ValueError:
        raise MalformedTokenException("Cannot differentiate header, payload and signature")


def _add_missing_padding(token):
    missing_pad = len(token) % 3
    return token + (missing_pad * '=')