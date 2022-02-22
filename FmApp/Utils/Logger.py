"""收集日志信息"""

import logging


class Logger:

    def logger(self, level, msg):
        # 定义日志收集器
        my_logger = logging.getLogger("lyh")

        # 设定级别
        my_logger.setLevel(level)

        # 设置日志输出格式
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(pathname)s[line:%(lineno)d] - %(filename)s - %(name)s - 日志信息: %(message)s')

        # 创建输出渠道
        sh = logging.StreamHandler()  # 输出到控制台
        sh.setLevel(level)
        sh.setFormatter(formatter)

        fh = logging.FileHandler(r"../TestReport/log.txt", encoding="utf-8")  # 输出到指定文件
        fh.setLevel(level)
        fh.setFormatter(formatter)

        # 收集器对接输出渠道
        # my_logger.addHandler(sh)
        my_logger.addHandler(fh)

        if level == "DEBUG":
            my_logger.debug(msg)
        elif level == "INFO":
            my_logger.info(msg)
        elif level == "WARNING":
            my_logger.warning(msg)
        elif level == "ERROR":
            my_logger.error(msg)

        # 关闭渠道
        my_logger.removeHandler(fh)

    def debug(self, msg):
        self.logger("DEBUG", msg)

    def info(self, msg):
        self.logger("INFO", msg)

    def warning(self, msg):
        self.logger("WARNING", msg)

    def error(self, msg):
        self.logger("ERROR", msg)


if __name__ == '__main__':
    log = Logger()
    log.debug("debug信息")
    log.info("info信息")
    log.warning("warning息")
    log.error("error信息")
