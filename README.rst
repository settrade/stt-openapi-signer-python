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


Installation & Usage
--------------------
Installation: 

.. code-block:: shell-session

    pip install stt-openapi-signer


Usage:


.. code-block:: python

    ## Python 3.x ##
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
    url = 'http://open-api.settrade.com/api/oam/v1/{}/broker-apps/{}/login'.format(broker_id, app_code)
    resp = requests.post(url, json={
        "apiKey": api_key,
        "params": params,
        "signature": signature,
        "timestamp": timestamp
    }
   