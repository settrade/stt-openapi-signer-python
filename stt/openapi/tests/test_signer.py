import unittest
from unittest import TestCase
from stt.openapi.signer import sign, verify, cv

from ecpy.curves import Curve, Point
from ecpy.keys import ECPublicKey, ECPrivateKey
from ecpy.ecdsa import ECDSA
import base64
import hashlib
import binascii


class SignerTest(TestCase):
    api_key = 'key1'
    private_key_b64 = 'AIKi/X7lvfu0haz0SttdbCj+nXmWBt/jfrbPAHRjwNHq'
    public_key_b64 = 'BHgE2uNGubxdex5rWgKdGeVZZKat+DQQ5R+EGmW30d53SeYZ83frLak9MWbgcl3Wz68ROIu9kWLwzbaBqB6rciY='

    def test_sign_verify(self):
        params = 'test-params'
        signature, timestamp = sign(self.api_key, self.private_key_b64, params)
        self.assertTrue(verify(self.api_key, self.private_key_b64,
                               params, signature, timestamp))
        self.assertTrue(self.__verifyUsingPublicKey(signature, self.api_key,
                                                    params, timestamp, self.public_key_b64))

    def test_sign_empty_params(self):
        params = ''
        signature, timestamp = sign(self.api_key, self.private_key_b64, params)
        self.assertTrue(verify(self.api_key, self.private_key_b64,
                               params, signature, timestamp))
        self.assertTrue(self.__verifyUsingPublicKey(signature, self.api_key,
                                                    params, timestamp, self.public_key_b64))

    def __verifyUsingPublicKey(self, signature, api_key, params, timestamp, public_key):
        signer = ECDSA()
        pu_bytes = base64.b64decode(public_key)
        # int(pu_bytes[1:33].encode('hex'), 16)
        x = int(binascii.hexlify(pu_bytes[1:33]), 16)
        y = int(binascii.hexlify(pu_bytes[33:]), 16)
        pu_key = ECPublicKey(Point(x, y, cv))
        hashed = hashlib.sha256(
            "{}.{}.{}".format(api_key, params, timestamp).encode("UTF-8")).hexdigest()

        return signer.verify(
            bytearray.fromhex(hashed),
            bytearray.fromhex(signature),
            pu_key)
