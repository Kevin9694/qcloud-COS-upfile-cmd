import os


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
