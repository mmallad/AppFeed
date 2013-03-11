import random
import string
import AppFeed.settings as s


class Global:
    def token(self):
        st = ''
        for i in range(1, 40):
            st = st + random.choice(string.ascii_uppercase)
        return st + str(random.randrange(1, 98887776783883, 1)) + random.choice(string.ascii_lowercase)

    def checkHost(self, host):
        h = host.replace("www.", "").replace("http://", "")
        oh = s.MEDIA_URL.replace("http://", "").replace("/", "")
        if h != oh:
            return False
        else:
            return True