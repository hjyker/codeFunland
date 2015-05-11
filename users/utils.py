#!/usr/bin/env python
# -*- coding: utf-8 -*-


import hashlib
import uuid
from PIL import Image


AVATAR_PATH = r"/home/hjyker/codeUtopia/media/avatar/"
REGION = (100,22,281,203)


def handle_upload_files(file, request):
    if not file:
        raise ValueError(u"The file is not empty!")

    file.name = file.name.encode('utf-8') + str(uuid.uuid1())
    file.name = "%s.jpg" % hashlib.md5(file.name).hexdigest()
    file_path = AVATAR_PATH + file.name

    file, image_raw, region = handle_image_size(file, request)

    image_raw.crop(region).save(file_path, "JPEG")
    # with open(file_path, "wb+") as info:
        # for chunk in file.chunks():
            # info.write(chunk)
    # return file, w,h,persent,width,height,x2,y2
    return file


def handle_image_size(file, request):
    x1 = int(request.POST.get("x1", 92))
    y1 = int(request.POST.get("y1", 0))
    x2 = int(request.POST.get("x2", 302))
    y2 = int(request.POST.get("y2", 225))
    width = int(request.POST.get("width", 400))
    height = int(request.POST.get("height", 225))

    image_raw = Image.open(file)
    w, h = image_raw.size
    persent = w / float(width)
    width = (x2-x1) * persent
    height = (y2-y1) * persent
    x1 = int(x1 * persent)
    y1 = int(y1 * persent)
    x2 = int(x1 + width)
    y2 = int(y1 + height)

    return file, image_raw, (x1, y1, x2, y2)

