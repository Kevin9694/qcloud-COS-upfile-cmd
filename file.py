import os
from sys import exit
codeFn = [".py", ".md", ".txt", ".html", ".css", ".sass", ".scss", ".cpp", ".h", ".c", ".hpp", ".m", ".js", ".php"]
docFn = [".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".pages", ".pdf"]
videoFn = [".mp4", ".mov", ".flv", ".avi"]
audioFn = [".wav", ".mp3"]
pluginFn = [".workflow"]
imageFn = [".jpg", ".jpeg", ".png", ".gif"]

class file:
    dir = ""
    filename = ""
    abspath = ""
    name = ""
    extension = ""
    abspath = ""

    def init(self, url):
        (self.dir, self.filename) = os.path.split(url)
        (self.name, self.extension) = os.path.splitext(self.filename)
        self.abspath = os.path.abspath(self.dir)

    def uploadfile(self):
        return 1;

    def getsecondDir(self):
        # print self.extension
        if self.extension in codeFn:
            return "code/" + self.extension[1:] + "/"
        elif self.extension in docFn:
            return "documents/" + self.extension[1:] + "/"
        elif self.extension in videoFn:
            return "video/" + self.extension[1:] + "/"
        elif self.extension in audioFn:
            return "audio/" + self.extension[1:] + "/"
        elif self.extension in pluginFn:
            return "plugin/" + self.extension[1:] + "/"
        elif self.extension in imageFn:
            return "image/"
        else:
            path = raw_input("this extension maybe is not correct , the file will be upload to \"/other/ (Y/N)")
            if (path == "Y") | (path == "y"):
                return "other/" + self.extension[1:] + "/"
            else:
                exit()
