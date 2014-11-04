from downloader.mangaedenparser import MangaEdenParser

__author__ = 'pablo'
import urllib.request


class MangaEden():
    def __init__(self, url, out_folder):
        self.url = url
        self.chapters_url = None
        self.out_folder = out_folder

    def extract_all_chapters_url(self):
        if self.url is None:
            return

        response = urllib.request.urlopen(self.url)
        data = response.read()
        parser = MangaEdenParser()
        parser.reset_status()
        parser.feed(str(data))

        self.chapters_url = {}

        print(parser.urls)
        for u in parser.urls:
            print(u)

        for url in parser.urls:
            chapter = url.split('/')[-3]
            #To order the 'xx' must be change to 0xx
            if len(chapter) == 2:
                char_array = list(chapter)
                chapter = "".join(['0'] + char_array)
            elif len(chapter) == 1:
                char_array = list(chapter)
                chapter = "".join(['00'] + char_array)

            self.chapters_url[chapter] = url

        return self.chapters_url

