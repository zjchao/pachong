from scrapy.dupefilter import BaseDupeFilter
from  scrapy.utils.request import request_fingerprint
class MyDupeFilter(BaseDupeFilter):

    def __init__(self, path=None, debug=False):
        self.record = set()

    @classmethod
    def from_settings(cls, settings):

        return cls()

    def request_seen(self, request):
        fingerprint = request_fingerprint(request)
        if fingerprint in self.record:
            print(request.url,'已经访问过')
            return True
        else:
            self.record.add(fingerprint)


    def request_fingerprint(self, request):
        pass

    def close(self, reason):

        pass