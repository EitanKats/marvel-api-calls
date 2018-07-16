import hashlib
import time

PUBLIC_KEY = "{}"
PRIVATE_KEY = "{}"


class MarvelRequest:
    def __init__(self, url, offset, limit):
        self.url = url + "?apikey={}&offset={}&limit={}".format(PUBLIC_KEY, offset, limit)
        self.build_request_url()

    def build_request_url(self):
        currtime = str(time.time())
        specialHash = hashlib.md5(currtime + PRIVATE_KEY + PUBLIC_KEY).hexdigest()
        self.url = self.url + "&hash={0}&ts={1}".format(specialHash, str(currtime))

    def __str__(self):
        return self.url;
