#!/usr/bin/env python
# -*- coding: utf-8 -*-


import hashlib


AVATAR_PATH = r"/home/zhangyd/codeFunland/media/avatar/"

def handle_upload_files(file):
    if not file:
        raise ValueError(u"The file is not empty!")
    file.name = file.name.encode('utf-8')
    file.name = "%s.jpg" % hashlib.md5(file.name).hexdigest()
    file_path = AVATAR_PATH + file.name
    with open(file_path, "wb+") as info:
        for chunk in file.chunks():
            info.write(chunk)
    return file
