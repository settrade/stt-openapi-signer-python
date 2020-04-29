from ecpy.curves import Curve
from ecpy.keys import ECPrivateKey
from ecpy.ecdsa import ECDSA
import base64
import hashlib
import time
import binascii

cv = Curve.get_curve('secp256r1')


def sign(api_key, api_secret, params, timestamp=None):
    if timestamp is None:
        timestamp = __currentTimestamp()
    payload = __composePayload(api_key, params, timestamp)
    hashed_payload = hashlib.sha256(payload.encode("UTF-8")).hexdigest()

    pv_key = ECPrivateKey(
        int(binascii.hexlify(base64.b64decode(api_secret)), 16), cv)
    signature_bytes = ECDSA().sign(bytearray.fromhex(hashed_payload), pv_key)
    return binascii.hexlify(signature_bytes).decode("UTF-8"), timestamp


def verify(api_key, api_secret, params, signature, timestamp):
    payload = __composePayload(api_key, params, timestamp)
    pv_key = ECPrivateKey(
        int(binascii.hexlify(base64.b64decode(api_secret)), 16), cv)
    hashed_payload = hashlib.sha256(payload.encode("UTF-8")).hexdigest()

    return ECDSA().verify(
        bytearray.fromhex(hashed_payload),
        bytearray.fromhex(signature),
        pv_key.get_public_key())


def __composePayload(api_key, params, timestamp):
    return "{}.{}.{}".format(api_key, params, timestamp)


def __currentTimestamp():
    return int(round(time.time() * 1000))
