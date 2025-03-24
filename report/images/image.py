import os


def path():
    # 写入到指定的文件
    curpath = os.path.dirname(os.path.realpath(__file__))
    print("curpath地址", curpath)
    # casepath = os.path.join(curpath, "case")
    # reportpath = os.path.join(curpath, "report")
    return curpath


if __name__ == "__main__":
    ...
