__author__ = 'pablo'
from html.parser import HTMLParser


class MangaEdenParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        #print("Encountered a start tag:", tag)
        #print("\tWith attrs:", attrs)

        if tag == 'tr':
            for attr in attrs:
                if 'id' in attr:
                    self.get_next_ref = True

        if tag == 'a' and self.get_next_ref:
            self.get_next_ref = False
            self.urls.add("http://www.mangaeden.com" + attrs[0][1])

    def handle_data(self, data):
        if "Volume:" in data:
            #print("Encountered some data  :", data)
            self.start_recording = True

    def reset_status(self):
        self.start_recording = False
        self.urls = set()
        self.get_next_ref = False