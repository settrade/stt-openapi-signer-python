from ecpy.curves import Curve
from ecpy.keys import ECPrivateKey
from ecpy.ecdsa import ECDSA
import base64
import hashlib
import time

cv = Curve.get_curve('secp256r1')


def sign(api_key, api_secret, params, timestamp=None):
    if timestamp is None:
        timestamp = __currentTimestamp()
    payload = __composePayload(api_key, params, timestamp)
    hashed_payload = hashlib.sha256(payload.encode("UTF-8")).hexdigest()

    pv_key = ECPrivateKey(int(base64.b64decode(api_secret).hex(), 16), cv)
    signature = ECDSA().sign(bytes.fromhex(hashed_payload), pv_key).hex()
    return signature, timestamp


def verify(api_key, api_secret, params, signature, timestamp):
    payload = __composePayload(api_key, params, timestamp)
    pv_key = ECPrivateKey(int(base64.b64decode(api_secret).hex(), 16), cv)
    hashed_payload = hashlib.sha256(payload.encode("UTF-8")).hexdigest()

    return ECDSA().verify(
        bytes.fromhex(hashed_payload),
        bytes.fromhex(signature),
        pv_key.get_public_key())


def __composePayload(api_key, params, timestamp):
    return "{}.{}.{}".format(api_key, params, timestamp)


def __currentTimestamp():
    return int(round(time.time() * 1000))
