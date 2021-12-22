from services.reader_txt_service import TxtReader
from services.logger import logger_instance


class StructureData:

    def get_sorted_int_list(self) -> list:
        parsing_lines = TxtReader()
        lines = parsing_lines.read_txt()

        for line in lines:
            items = line.split()
        setitems = set(items)
        setitems = [int(i) for i in setitems if i.isdigit()]

        return setitems

    def get_lists(self, input_num=22) -> list:
        if input_num > 1:
            input_nums = [int(i) for i in range(2, input_num+1)]
            all_num_list = self.get_sorted_int_list()
            data_tree = []

            for i in input_nums:
                list_items = [i]
                num_while = i

                while num_while * num_while <= max(all_num_list):
                    num_while = num_while * num_while
                    list_items.append(num_while)

                result_list = sorted(list(set(all_num_list) & set(list_items)))
                data_tree.append(result_list)

            return data_tree

        else:
            logger_instance.log_warning(self.__class__.__name__ + ' - Input number is <= 1!')

