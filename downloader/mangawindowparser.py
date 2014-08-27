__author__ = 'pablo'
from html.parser import HTMLParser


class MangaWindowParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        no_jump = True
        if 'a' == tag:
            #print("Encountered a start tag:", tag)
            for attr in attrs:
                if 'title' in attr:
                    no_jump = False
            if no_jump:
                #print("Encountered a start tag:", tag)
                for attr in attrs:
                    if 'href' in attr:
                        if '3-1' not in attr[1] and '6-1' not in attr[1] and '10-1' not in attr[1] and 'all' not in attr[1]:
                            if self.start_recording:
                                #print("     attr:", attr)
                                self.urls.add("http://www.mangawindow.com/" + attr[1])

    def handle_data(self, data):
        if "Volume:" in data:
            #print("Encountered some data  :", data)
            self.start_recording = True

    def reset_status(self):
        self.start_recording = False
        self.urls = set()
