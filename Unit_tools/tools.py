# coding=utf8
import random
import time
import os
from report import report_path


def name_random():
    a1 = ['张', '金', '李', '王', '赵', '万', '毛',
          '周', '腾', '讯', '马', '云', '懂', '曹', '刘',
          '诸葛', '赵', '关', '赵', '钱', '孙', '李',
          '周', '吴', '郑', '王', '冯']
    a2 = ['', '玉', '明', '龙', '芳', '军', '玲', '文', '敏',
          '同', '丽', '一', '次', '生', '长', '在', '非', '洲', '荒', '漠', '地', '带', '依', '米', '花']
    a3 = ['', '方', '立', '玲', '家', '国', '秀', '桦', '丽']
    name = random.choice(a1)+random.choice(a2)+random.choice(a3)
    return name


def number_random():
    a1 = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    a2 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    number_random = 'HT369'+random.choice(a1) + random.choice(a2) + random.choice(a2)+random.choice(a2)+random.choice(a2)+\
                    random.choice(a2)+random.choice(a2)+random.choice(a2)+random.choice(a2)
    return number_random


def order_Number_random():
    a0 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
          'W', 'X', 'Y', 'Z']
    a1 = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    a2 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    number_random = 'SD369'+random.choice(a0)+random.choice(a1)+random.choice(a2) + random.choice(a2)+random.choice(a2)+random.choice(a2)+\
                    random.choice(a2)+random.choice(a2)+random.choice(a2)+random.choice(a2)
    return number_random


def get_mobile():
    mobiles = ['130', '131', '132', '133', '134', '130', '157', '158', '135', '183']
    number = str(int(time.time()))[2:]
    mobile = random.choice(mobiles)+number
    return mobile


def text_remark():
    a0 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
          'W', 'X', 'Y', 'Z']
    a1 = ['内不欺己，外不欺人。———孔子',
          '生于忧患，死于安乐。——孟子',
          '穷不失义，达不离道。——孔丘《论语》',
          '朝闻道，夕死可矣。——孔子',
          '命为志存。 —— 朱熹',
          '何以称英雄人物？识以领其先。——袁枚',
          '士为知己者死。——司马迁',
          '生、死、穷、达不易其志。——苏轼',
          '不知其人，视其友。——司马迁',
          '君子忧道不忧贫。 —— 孔丘',
          '君子忧道不忧贫。 —— 孔丘',
          '命为志存。——朱熹励志名言',
          '不义而疆，其毙必速。',
          '与其找糊涂导师，倒不如自己走。',
          '穷且益坚，不坠青云之志。',
          '没有在深夜痛哭过的人，不足以谈人生。',
          '有种信息叫，已读不回。',
          '今日乐相乐，别后莫相忘。',
          '我不知道遇见你是对是错，但我知道遇见你我开心过。',
          '人死了，但事业永存。——柯西']
    return random.choice(a0)+random.choice(a1)



def Car_Number():
    char0 = ["京", "津", "沪", "渝", "冀", "豫", "云", "辽", "黑", "湘", "皖", "鲁", "新", "苏", "浙", "赣", "鄂", "桂", "甘", "晋", "蒙"
             , "陕", "吉", "闽", "赣", "粤", "青", "藏", "川", "宁", "琼"]
    char1 = 'ABCDEFGHJKLMNPQRSTUVWXYZ'
    char2 = '0123456789ABCDEFGHJKLMNPQRSTUVWXYZ'
    id_1 = random.choice(char0)
    id_2 = ''.join(random.sample(char1, 1))
    while True:
        id_3 = ''.join(random.sample(char2, 5))
        v = id_3.isalpha()
        if v == True:
            continue
        else:
            car_id = id_1 + id_2 + id_3
            break
    return car_id


def Car_Numbers():
    a1 = ['冀V40JUG', '豫GTRX2C', '渝WSF0ET', '川U5AUNQ', '桂ENW8M6', '皖CN6ZGM', '桂L7NYU0',
          '新XR8PWN', '云ZL2UN6', '青KFHY6X', '琼S8WKLA', '沪S0RWQJ', '宁D7NZFB', '藏ET0S1W', '粤DJTCN8',
          '赣PB48UT', '青V2VPXZ']
    name = random.choice(a1)
    return name


def delete_file():
    '''删除文件,报告images'''
    path = report_path.report_path_dir()
    print("地址", path)
    for item in os.listdir(path):
        directoryPath = os.path.join(path, item)
        print("directoryPath", directoryPath)

        if os.path.isdir(directoryPath):
            for file in os.listdir(directoryPath):
                filePath = os.path.join(directoryPath, file)
                temp = os.path.splitext(file)
                if temp[1] == ".png":
                    os.remove(filePath)


if __name__ == '__main__':
    delete_file()