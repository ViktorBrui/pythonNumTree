import logging


class Logger:

    def log_warning(self, data: str or dict):
        logging.basicConfig(level=logging.WARNING, format='%(name)s - %(levelname)s - %(message)s - %(asctime)s ', datefmt="%d %b %Y %H:%M:%S",
                            filename='app.log', filemode='w')
        return logging.warning(data)

    def log_info(self, data: str or dict):
        logging.basicConfig(level=logging.INFO, format='%(name)s - %(levelname)s - %(message)s', datefmt="%d %b %Y %H:%M:%S",
                            filename='app.log', filemode='w')
        return logging.info(data)


logger_instance = Logger()
