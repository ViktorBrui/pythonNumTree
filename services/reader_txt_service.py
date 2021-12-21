import logging
logging.basicConfig(level=logging.INFO, filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %('
                                                                                 'message)s')


class TxtReader:

    @staticmethod
    def read_txt():
        file = open("numbers.txt", "r")
        if file:
            lines = file.readlines()
            file.close()
            return lines
        else:
            logging.warning('File is clear...')

