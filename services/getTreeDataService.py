from services.parseService import Parsing


class GetTreeData:
    # получаем список элементов и превращаем их в int
    def get_sorted_int_list(self):
        parsing_lines = Parsing()
        lines = parsing_lines.parsing_txt()
        for line in lines:
            items = line.split()
        setitems = set(items)
        setitems = [int(i) for i in setitems if i.isdigit()]
        setitems.sort()
        return setitems


    # получаем первые три наименьших элемента из отсортированного списка
    def get_three_smallest_num(self):
        items = self.get_sorted_int_list()
        three_item = items[0:3]
        return three_item


    # получаем список чисел для узла второго наименьшего элемента
    def get_sqr_list_second_number(self):
        all_nums_list = self.get_sorted_int_list()
        three_smallest_num = self.get_three_smallest_num()
        second_num = three_smallest_num[1]
        print("all nums from txt", all_nums_list)
        second_list = [second_num]
        second_num_while = second_num
        while second_num_while * second_num_while <= max(all_nums_list):
            second_num_while = second_num_while * second_num_while
            second_list.append(second_num_while)
        result_second_list = sorted(list(set(all_nums_list) & set(second_list)))
        return result_second_list


    # получаем список чисел для узла третьего наименьшего элемента
    def get_sqr_list_third_number(self):
        all_nums_list = self.get_sorted_int_list()
        three_smallest_num = self.get_three_smallest_num()
        third_num = three_smallest_num[2]
        third_list = [third_num]
        second_num_while = third_num
        while second_num_while * second_num_while <= max(all_nums_list):
            second_num_while = second_num_while * second_num_while
            third_list.append(second_num_while)
        result_three_list = sorted(list(set(all_nums_list) & set(third_list)))
        return result_three_list


