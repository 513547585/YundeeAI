# coding=utf8
import os


def page_relative_path():
    curpath = os.path.dirname(os.path.realpath(__file__))
    photo_paths = curpath + "\\" + "loding_photo.exe"
    return photo_paths


if __name__ == "__main__":
    page_relative_path()