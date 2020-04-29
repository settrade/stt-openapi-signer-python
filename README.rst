Settrade OpenAPI parameters signer
====================================
.. image:: https://travis-ci.org/theerapatcha/stt-openapi-signer-python.svg?branch=master
   :target: https://travis-ci.org/theerapatcha/stt-openapi-signer-python/builds
.. image:: https://codecov.io/gh/theerapatcha/stt-openapi-signer-python/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/theerapatcha/stt-openapi-signer-python


Overview
--------
Website: `Settrade OpenAPI <https://developer.settrade.com/open-api>`_.

Related API: `Login by APP <https://developer.settrade.com/open-api/document/api-reference/oam/broker-app-auth-controller/loginByApp>`_.


Installation
------------

.. code-block:: shell-session

    pip install -U git+https://github.com/theerapatcha/stt-openapi-signer-python


Usage
-----

Python: 

.. code-block:: python

    from stt.openapi.signer import sign
    import requests

    # STT Open API Parameters
    broker_id = '0XX' # Broker ID
    app_code = '<you_service_code>'
    api_key = '<your_api_key>'
    api_secret = '<your_api_secret>'
    params = ''

    # Sign it
    signature, timestamp = sign(api_key, api_secret, params)
    
    # Use it
    url = 'https://open-api.settrade.com/api/oam/v1/{}/broker-apps/{}/login'.format(broker_id, app_code)
    resp = requests.post(url, json={
        "apiKey": api_key,
        "params": params,
        "signature": signature,
        "timestamp": timestamp
    }
   
CLI:

.. code-block:: shell-session

    $ python -m stt.openapi.signer "<your_api_key>" "<your_api_secret>" "<your_params>" [<your_timestamp>]
    $ 3044022076edd40a9b92fe4435f3f1c42eac4ef858c395de81169ae2577d31637bd0a34f02207f98ddc8e4d22fbd3a11216cd4e76139d3f212f18e9bd36520db90f7d9a91869 1588136696131
