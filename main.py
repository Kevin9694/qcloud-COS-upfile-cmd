from file import file
from sys import argv
from upload import upload


def start():
    up = upload
    up.initSetting()
    arg1 = argv[1]
    arg2 = argv[2]
    first_arg_dict = {"-o": "/other/", "-s": "/static/", "-a": "/archive/"}
    if arg1 in first_arg_dict:
        basicPath = first_arg_dict[arg1]
        f = file()
        f.init(arg2)
    elif arg1 == "-d":
        pass
    else:
        basicPath = "/static/"
        f = file()
        f.init(arg1)

    pass


def secondDir(ext):


if __name__ == "__main__":
    start()
