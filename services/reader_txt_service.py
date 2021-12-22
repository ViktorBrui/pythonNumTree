from services.logger import logger_instance


class TxtReader:

    def read_txt(self, input_file="numbers.txt"):
        with open(input_file, encoding='utf-8') as file:

            if file:
                lines = file.readlines()
                return lines

            else:
                logger_instance.log_warning(self.__class__.__name__ + ' - class, Something wrong...')


