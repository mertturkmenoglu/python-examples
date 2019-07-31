import logging


if __name__ == '__main__':
    logger = logging.getLogger("main-module-logger")
    logger.setLevel(logging.DEBUG)

    file = logging.FileHandler("main-module.log")
    std_out = logging.StreamHandler()

    log_format = logging.Formatter('%(asctime)s - %(name)s [%(levelname)s]: %(message)s')

    file.setFormatter(log_format)
    std_out.setFormatter(log_format)

    logger.addHandler(file)
    logger.addHandler(std_out)

    logger.info("Info level message")
    logger.warning("Warning level message")
    logger.critical("Critical level message")
    logger.error("Error level message")
    logger.debug("Debug level message")
