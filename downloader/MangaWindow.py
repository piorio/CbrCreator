import os
from downloader.mangawindowparser import MangaWindowParser
from downloader.mangawindowpageparser import MangaWindowPageParser
from subprocess import call
import urllib
import zipfile

__author__ = 'pablo'
import urllib.request

class MangaWindow():
    def __init__(self, url, out_folder):
        self.url = url
        self.chapters_url = None
        self.out_folder = out_folder

        #if not os.path.exists(self.out_folder):
        #    os.makedirs(self.out_folder)

    def extract_all_chapters_url(self):
        if self.url is None:
            return

        response = urllib.request.urlopen(self.url)
        data = response.read()
        parser = MangaWindowParser()
        parser.reset_status()
        parser.feed(str(data))

        self.chapters_url = {}

        for url in parser.urls:
            chapter = url.split('/')[-2]
            #To order the 'c1' must be change to c01
            if len(chapter) == 2:
                char_array = list(chapter)
                chapter = "".join(char_array[0:1] + ['0'] + char_array[1:])
            self.chapters_url[chapter] = url

        return self.chapters_url

    def download_specific_chapter(self, url, chapter):
        pages, img_base = self.get_image_information(url)
        print("For {} we have {} imgs".format(chapter, pages))
        sub_folder = self.out_folder + "/" + chapter
        if not os.path.exists(sub_folder):
            os.makedirs(sub_folder)
        zf = zipfile.ZipFile(sub_folder + ".cbr", mode='w')
        for i in range(1, int(pages) + 1):
            img = "{}{}.jpg".format(img_base, i)
            local_img = img.split('/')[-1]
            urllib.request.urlretrieve(img, sub_folder + "/" + local_img)
            zf.write(sub_folder + "/" + local_img)
        zf.close()

    def download_each_chapter(self):
        for url in self.chapters_url:
            pages, img_base = self.get_image_information(url)
            print("Pages from {} are {} with base url {}".format(url, pages, img_base))
            subfolder = self.out_folder + "/" + url.split('/')[-2]
            print(subfolder)

            if not os.path.exists(subfolder):
                os.makedirs(subfolder)
            zf = zipfile.ZipFile(subfolder + ".cbr", mode='w')

            for i in range(1, int(pages)):
                img = "{}{}.jpg".format(img_base, i)
                print("DOWNLOAD: ", img)
                localimg = img.split('/')[-1]
                print("DOWNLOADX: ", localimg)
                print("Subfolder: ", subfolder)

                urllib.request.urlretrieve(img, subfolder + "/" + localimg)
                zf.write(subfolder + "/" + localimg)

                #call(["wget", "-P", subfolder, img])
                #call(["zip", "-r", subfolder + ".cbr", subfolder])
            zf.close()

    def get_image_information(self, url):
        page_response = urllib.request.urlopen(url)
        data = page_response.read()
        parser = MangaWindowPageParser()
        parser.init_status()
        parser.feed(str(data))
        return parser.pages, parser.img_base_url[:-5]