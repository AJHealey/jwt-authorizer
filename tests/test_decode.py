from unittest import TestCase

from jwt_decoder import decode_token
from jwt_encoder import sign_with_hs256


class TestDecodeToken(TestCase):

    def test_decode_token(self):
        # Given
        token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.' \
                'eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiYWRtaW4iOnRydWV9.' \
                'TJVA95OrM7E2cBab30RMHrHDcEfxjoYZgeFONFh7HgQ'

        # When
        header, payload, signature = decode_token(token)

        # Then
        expected_header = {'alg': 'HS256', 'typ': "JWT"}
        self.assertDictEqual(header, expected_header, "Header is not correctly decoded")
        expected_payload = {'sub': '1234567890', 'name': "John Doe", "admin": True}
        self.assertDictEqual(payload, expected_payload, "Payload is not correctly decoded")
        expected_signature = sign_with_hs256(header, payload, 'secret')
        self.assertEqual(signature, expected_signature, "Signature is not correct")
