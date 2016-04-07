import json, requests, os

class PyScanii(object):

    key = ''
    secret = ''
    requests_session = None
    url = ''
    # EICAR test string. (Encoded to prevent host-OS false-positive)
    EICAR = 'WDVPIVAlQEFQWzRcUFpYNTQoUF4pN0NDKTd9JEVJQ0FSLVNUQU5E'.decode('base64') \
            + 'QVJELUFOVElWSVJVUy1URVNU\nLUZJTEUhJEgrSCo=\n'.decode('base64')
    # Use latency distributed endpoint by default.
    base_url = 'https://api.scanii.com'
    api_version = 'v2.1'
    verbose = False

    # Used for batch scanning.
    files = []

    def __init__(self, key, secret, **kwargs):
        self.key = key
        self.secret = secret
        for key in kwargs:
            # Set kwargs to properties
            setattr(self, key, kwargs[key])

        self.requests_session = requests.Session()
        self.requests_session.auth = (self.key, self.secret)
        if self.api_version.startswith('v2'):
            self.scan_method = 'files'
        else:
            self.scan_method = 'scan'

    def _get_url(self, method):
        return '/'.join((self.base_url, self.api_version, method))

    @property
    def last_file(self):
        return self.files[-1]

    def ping(self):
        url = self._get_url('ping')
        if self.verbose:
            print("Pinging: {}".format(url))

        r = self.requests_session.get(url)
        response = r.json()

        if self.verbose:
            print(response)

        return response

    def test(self):
        return self.scan(self.EICAR)

    def scan(self, files=None):
        self.files = []
        ftype = type(files)
        if not any([ftype is list, ftype is tuple]):
            files = [files]

        for scanfile in files:
            try:
                if os.path.isfile(scanfile):
                    self._scan(path=scanfile)
                else:
                    self._scan(string=scanfile)
            except TypeError:
                # must be encoded string without NULL bytes, not str
                self._scan(string=scanfile)


    def _scan(self, path=None, string=None):
        url = self._get_url(self.scan_method)
        if self.verbose:
            print("URL: {}".format(url))

        if path:
            name = path
            if self.verbose:
                print("Scanning file at: {}".format(path))
            files = {'file': open(path, 'rb')}
        else:
            name = 'string.bin'
            if self.verbose:
                print("Scanning string as filename: {}".format(name))
            files = {'file': (name, string)}

        r = self.requests_session.post(url, files=files)
        response = r.json()

        if self.verbose:
            print(response)

        scanfile = ScanFile(name=name, **response)
        self.files.append(scanfile)
        return self.files

class ScanFile(object):
    name = ''
    checksum = ''
    content_length = 0
    content_type = u'text/plain'
    creation_date = None
    findings = []
    id = ''
    metadata = {}
    infected = False

    def __init__(self, **kwargs):
        for key in kwargs:
            # Set kwargs to properties
            setattr(self, key, kwargs[key])

        if self.findings:
            self.infected = True

    def __str__(self):
        return json.dumps({
            'name': self.name,
            'checksum': self.checksum,
            'content_length': self.content_length,
            'content_type': self.content_type,
            'creation_date': self.creation_date,
            'findings': self.findings,
            'id': self.id,
            'metadata': self.metadata,
            'infected': self.infected
        })

    def __repr__(self):
        return("({}) {} - Infected: {} - Findings: {}".format(self.id, self.name,
                                                             self.infected, self.findings))
