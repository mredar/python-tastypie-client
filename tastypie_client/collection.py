
import simplejson as json
from httplib2 import Http

from tastypie_client import Resource
from tastypie_client.url import urljoin

class Collection(object):
    def __init__(self, url, schema_url = None):
        self.url = url
        self.schema_url = schema_url
        self.meta = { 'limit':None, 'offset':None, 'next':None, 'previous':None, 'total_count':None}
        self.url_next = self.url

    @staticmethod
    def __load_url(url):
        '''Load a url into a dictionary: meta & a list of objects
        '''
        response, content = Http().request(url)
        meta = json.loads(content)['meta']
        objects = [obj for obj in json.loads(content)['objects']]
        return meta, objects

    def __iter__(self):
        '''Get the next set of Resources for the collection'''
        while True:
            self.meta, objects = self.__load_url(self.url_next)
            for obj in objects:
                yield Resource(url = urljoin(self.url, obj['resource_uri']), fields = obj)
            if not self.meta['next']:
                raise StopIteration
            self.url_next = self.url+self.meta['next']

    def __len__(self):
        if not self.meta['total_count']:
            self.meta, objs = self.__parse_url(self.url)
        return self.meta['total_count']

    def __contains__(self, v):
        return True if self.get(v) else False

    def __getitem__(self, v):
        return self.get(v)

    def get(self, id):
        return Resource(urljoin(self.url, id))
        
    def put(self, id, value):
        return None

    def post(self, id, value):
        return None

    def patch(self, id, changes):
        return None

    def schema(self):
        if self.schema_url:
            response, content = Http().request(self.schema_url)
            return json.loads(content)
