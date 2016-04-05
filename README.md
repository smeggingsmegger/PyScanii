# PyScanii

A Python module for using the [scanii.com](https://scanii.com/) API.

## Installing / Upgrading

`$ pip install -U PyScanii`

## Usage

```python
>>> from PyScanii import PyScanii
>>> pyscanii = PyScanii('SOMEAPIKEY', 'SECRET')

# .scan() is the main method.
# It can accept single strings or paths.
# It can also accept a list or tuple of either of those things.
>>> pyscanii.scan('X5O!P%@AP[4\\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*')
# The files property contains a list of ScanFile instances:

>>> pyscanii.files[0]
(563ef4b7836060b3bb9d0cba3e6a5f84) string.bin - Infected: True - Findings: [u'av.eicar-test-signature']

>>> str(pyscanii.files[0])
'{"content_length": 68, "infected": true, "name": "string.bin", "content_type": "text/plain", "checksum": "3395856ce81f2b7382dee72602f798b642f14140", "metadata": {}, "id": "563ef4b7836060b3bb9d0cba3e6a5f84", "findings": ["av.eicar-test-signature"], "creation_date": "2016-04-05T14:57:35.989Z"}'
```
