#!/usr/bin/env python
# -*- coding: utf-8 -*-


import hashlib
import uuid
from PIL import Image


AVATAR_PATH = r"/home/tt/codeFunland/media/avatar/"
REGION = (11,10,59,58)

def handle_upload_files(file):
    if not file:
        raise ValueError(u"The file is not empty!")
    file.name = file.name.encode('utf-8') + str(uuid.uuid1())
    file.name = "%s.jpg" % hashlib.md5(file.name).hexdigest()
    file_path = AVATAR_PATH + file.name
    image = Image.open(file)
    image.crop(REGION).save(file_path, "JPEG")
    # with open(file_path, "wb+") as info:
        # for chunk in file.chunks():
            # info.write(chunk)
    return file


def pre_handle_image(image_file):
    pass

