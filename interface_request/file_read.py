import os
import yaml


# 读yml
def read(name_file=None, key=None):
    curpath = os.path.dirname(os.path.realpath(__file__))
    # casepath = os.path.join(curpath, "configuration.yml")
    print(curpath)
    # with open('./configuration.yml', 'r', encoding='utf-8') as f:
    with open(curpath + name_file, 'r', encoding='utf-8') as f:
        data = yaml.load(stream=f, Loader=yaml.FullLoader)[key]
    return data


if __name__ == '__main__':
    print(read(name_file="./configuration.yml", key="ip"))
