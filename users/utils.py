#!/usr/bin/env python
# -*- coding: utf-8 -*-


import hashlib
import uuid
from PIL import Image


AVATAR_PATH = r"/home/tt/codeFunland/media/avatar/"
REGION = (100,22,281,203)


def handle_upload_files(file, request):
    if not file:
        raise ValueError(u"The file is not empty!")
    file.name = file.name.encode('utf-8') + str(uuid.uuid1())
    file.name = "%s.jpg" % hashlib.md5(file.name).hexdigest()
    file_path = AVATAR_PATH + file.name

    x1 = int(request.POST.get("x1", 92))
    y1 = int(request.POST.get("y1", 0))
    x2 = int(request.POST.get("x2", 302))
    y2 = int(request.POST.get("y2", 225))
    width = int(request.POST.get("width", 400))
    height = int(request.POST.get("height", 225))

    REGION = (x1,y1,x2,y2)
    image = Image.open(file)
    image.thumbnail((width, height), Image.ANTIALIAS)
    image.crop(REGION).save(file_path, "JPEG")
    # with open(file_path, "wb+") as info:
        # for chunk in file.chunks():
            # info.write(chunk)
    return file

