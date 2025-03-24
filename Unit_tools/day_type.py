import time
from datetime import datetime


def Now_time():
    '''获取当前日期 '''
    # now = datetime.now()  #当前日期
    today = datetime.today()   # 获取当前时间
    # utcnow = datetime.utcnow()  #获取当前的格林你治时间
    return today.date()


def time_add_time(day):
    '''time_add_time(day)时间往前+day天，往后-day天'''
    time_year = time.strftime("%Y-%m-%d", time.localtime(time.time() + 86400 * day))
    print("最新的修改时间", time_year)
    return time_year


def Now_year():
    '''获取当前年'''
    return datetime.now().year


def Now_month():
    '''获取当前月'''
    return datetime.now().month


def Now_day():
    '''获取当前日'''
    return datetime.now().day


def Now_hour():
    '''获取当前时'''
    return datetime.now().hour


def Now_minute():
    '''获取当前分钟'''
    return datetime.now().minute


def Now_second():
    '''获取当前秒'''
    return datetime.now().second


def Now_time_ms():
    '''获取毫秒'''
    return datetime.now()


def orderNumber():
    '''时间戳'''
    return 'DC369'+str(int(time.time()))


def invoice_number():
    '''发票编号'''
    text = str(int(time.time()))
    # print(text[2:], text)
    return text[2:]


if __name__ == "__main__":
    print(Now_time())