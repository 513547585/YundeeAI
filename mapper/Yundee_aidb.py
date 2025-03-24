# coding=utf8
import pymysql, sys
from Unit_tools import day_type
from logs import loginfo
log = loginfo.log().logger


def connect():
    global db
    db = pymysql.connect(
        host="172.21.129.231",
        port=3306,
        user="root",
        password="Ydconn$2021",
        database="yd_ai_dev",
        charset="utf8"
    )
    return db.cursor()


def delivery_note(name):
    '''查询热词次数'''
    cursor = connect()
    # SELECT * FROM t_dialogue_hot_words where word="奥特曼";
    sql = "SELECT T.count FROM t_dialogue_hot_words T where T.word = '%s'"%(name)
    cursor.execute(sql)
    db.commit()
    date = cursor.fetchone()

    if date ==None:
        log.info(str(day_type.Now_time_ms()) + "没有查到热词，请知悉")
        close_db()
        sys.exit()
    else:
        print("执行成功：", date[0])
        log.info("执行成功：" + str(date))
        close_db()
    return date[0]


def close_db():
    db.close()


if __name__ == "__main__":
    delivery_note('命令')