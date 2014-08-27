__author__ = 'pablo'
from html.parser import HTMLParser


class MangaWindowPageParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        #print("Encountered a start tag:", tag)
        for attr in attrs:
            if 'href' in attr:
                if 'http://a-old.mwfile.com/' in attr[1]:
                    #print("     attr:", attr[1])
                    self.img_base_url = attr[1]

    def handle_data(self, data):
        if "1 of " in data:
            self.pages = data[4:]

    def init_status(self):
        self.pages = 0
        self.img_base_url = None
