import logging,os


class log:
    # 配置日志输出格式
    logging.basicConfig(format='[%(asctime)s] %(levelname)s - %(message)s', level=logging.INFO)
    # 日志对象
    logger = logging.getLogger()

    # 设置日志级别
    # logger.setLevel(logging.DEBUG)
    logger.setLevel(logging.INFO)
    # logger.setLevel(logging.WARNING)
    # logger.setLevel(logging.ERROR)
    # logger.setLevel(logging.CRITICAL)

    # 写入到指定的文件
    curpath = os.path.dirname(os.path.realpath(__file__))
    # casepath = os.path.join(curpath, "case")
    # reportpath = os.path.join(curpath, "report")
    fh = logging.FileHandler(curpath+".text")
    logger.addHandler(fh)

    # 输出不同级别的日志信息
    # logger.debug('This is a debug message')
    # logger.info('This is a info message')
    # logger.warning('This is a warning message')
    # logger.error('This is a error message')
    # logger.critical('This is a critical message')


if __name__ == "__main__":
    print(log.curpath)
    log = log().logger
