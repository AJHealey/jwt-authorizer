import base64
import hashlib
import hmac
import json


def sign_with_hs256(header, payload, secret):
    b64_header = base64.urlsafe_b64encode(bytes(json.dumps(header, separators=(',', ':')), encoding='utf-8')).replace(b'=', b'')
    b64_payload = base64.urlsafe_b64encode(bytes(json.dumps(payload, separators=(',', ':')), encoding='utf-8')).replace(b'=', b'')

    content = b64_header + bytes('.', 'utf-8') + b64_payload

    return hmac.new(key=bytes(secret, encoding='utf-8'),
                    msg=content,
                    digestmod=hashlib.sha256).digest()


