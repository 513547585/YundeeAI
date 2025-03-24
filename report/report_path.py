# coding=utf8
import os


# 获取上传本地图片路径
def report_relative_path():
    # 获取报告路径
    curpath = os.path.dirname(os.path.realpath(__file__))
    photo_paths = curpath + "\\" + "report.html"
    return photo_paths


def report_path_dir():
    # 获取report地址
    curpath = os.path.dirname(os.path.realpath(__file__))

    print(curpath)
    return curpath


if __name__ == "__main__":
    report_path_dir()