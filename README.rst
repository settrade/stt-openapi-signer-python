Settrade OpenAPI parameters signer
====================================

Overview
--------
Website: `Settrade OpenAPI <https://developer.settrade.com/open-api>`_.

Related API: `Login by APP <https://developer.settrade.com/open-api/document/api-reference/oam/broker-app-auth-controller/loginByApp>`_.


Installation & Usage
--------------------
Installation: 

.. code-block:: shell-session

    # 1) install stt-openapi-signer
    pip install stt-openapi-signer


Usage:

.. code-block:: python

    from stt.openapi.signer import sign

    api_key = 'key1'
    api_secret = 'AIKi/X7lvfu0haz0SttdbCj+nXmWBt/jfrbPAHRjwNHq'
    params = 'test-params'
    
    signature, timestamp = sign(api_key, api_secret, params)
    # print (signature, timestamp)
   
   