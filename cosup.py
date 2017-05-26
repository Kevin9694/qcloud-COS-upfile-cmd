# coding:utf-8
from file import file
from sys import argv
from sys import exit
from upload import upload


class main:
    def start(self):
        up = upload()
        # TODO add 'catch'
        up.initSetting()
        arg1 = argv[1]
        arg2 = argv[2]
        first_arg_dict = {"-o": "/other/", "-s": "/static/", "-a": "/archive/"}
        if arg1 in first_arg_dict:
            basicPath = first_arg_dict[arg1]
            f = file()
            f.init(arg2)
            remotePath = basicPath + f.getsecondDir()
            try:
                ret = up.upfile(f, remotePath)
            except IOError as ioe:
                print ioe
                exit()
            if ret['message'] == 'SUCCESS':
                print up.bucketPath + remotePath + f.filename
            else:
                print ret
            exit()
        elif arg1 == "-d":  # to upload all files in the directory
            # TODO finish the function
            pass
        else:
            basicPath = "/static/"
            f = file()
            f.init(arg1)
            remotePath = basicPath + f.getsecondDir()
            try:
                ret = up.upfile(f, remotePath)
            except IOError as ioe:
                print ioe
                exit()
            print up.bucketPath + remotePath + f.filename
            exit()
        pass


if __name__ == "__main__":
    m = main()
    m.start()
