from services.reader_txt_service import TxtReader
import logging
logging.basicConfig(level=logging.INFO, filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %('
                                                                                 'message)s')


class DataLists:
    @staticmethod
    def get_sorted_int_list() -> list:
        parsing_lines = TxtReader()
        lines = parsing_lines.read_txt()
        for line in lines:
            items = line.split()
        setitems = set(items)
        setitems = [int(i) for i in setitems if i.isdigit()]
        return setitems

    def get_lists(self, input_num=21) -> list:
        if input_num > 1:
            input_nums = [int(i) for i in range(2, input_num+1)]
            print('some list', input_nums)
            all_num_list = self.get_sorted_int_list()
            result_data = []
            for i in input_nums:
                list_items = [i]
                num_while = i
                while num_while * num_while <= max(all_num_list):
                    num_while = num_while * num_while
                    list_items.append(num_while)
                result_list = sorted(list(set(all_num_list) & set(list_items)))
                result_data.append(result_list)
            print('result_list', result_data)
            return result_data
        else:
            logging.warning('Input number is <= 1')
