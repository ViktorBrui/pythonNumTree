from anytree import Node, RenderTree
from anytree.exporter import DotExporter
from flask import send_file


# парсим строку из txt фала
def parsing_txt():
    file = open("numbers.txt", "r")
    if file:
        lines = file.readlines()
        file.close()
    return lines


# получаем список элементов и превращаем их в int
def get_sorted_int_list():
    lines = parsing_txt()
    for line in lines:
        items = line.split()
    setitems = set(items)
    setitems = [int(i) for i in setitems if i.isdigit()]
    setitems.sort()
    return setitems


# получаем первые три наименьших элемента из отсортированного списка
def get_three_smallest_num():
    items = get_sorted_int_list()
    three_item = items[0:3]
    return three_item


# получаем список чисел для узла второго наименьшего элемента
def get_sqr_list_second_number():
    all_nums_list = get_sorted_int_list()
    three_smallest_num = get_three_smallest_num()
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
def get_sqr_list_third_number():
    all_nums_list = get_sorted_int_list()
    three_smallest_num = get_three_smallest_num()
    third_num = three_smallest_num[2]
    third_list = [third_num]
    second_num_while = third_num
    while second_num_while * second_num_while <= max(all_nums_list):
        second_num_while = second_num_while * second_num_while
        third_list.append(second_num_while)
    result_three_list = sorted(list(set(all_nums_list) & set(third_list)))
    return result_three_list


# создание дерева и отрисовка его с помощью DotExporter
def construct_tree():
    setitems = get_sorted_int_list()
    second_items = get_sqr_list_second_number()
    third_items = get_sqr_list_third_number()
    first_el = Node(min(setitems), parent=None)
    second_element = Node(second_items[0], parent=first_el)
    third_element = Node(third_items[0], parent=first_el)
    index_second = 0
    second_items.pop(index_second)
    for i in second_items:
        second_elements = Node(second_items[index_second], parent=second_element)
        second_element = second_elements
        index_second += 1
    index_third = 0
    third_items.pop(index_third)
    for j in third_items:
        third_elements = Node(third_items[index_third], parent=third_element)
        third_element = third_elements
        index_third += 1
    for pre, fill, node in RenderTree(first_el):
        print("%s%s" % (pre, node.name))
    DotExporter(first_el, nodeattrfunc=lambda node: "fixedsize=true, width=1, height=1, shape=box", edgeattrfunc=lambda parent, child: "style=bold").to_picture(
        "images/tree.png")
    return True


# функция выведения картинки во view
def result():
    # вывожу tree только для отображения дерева в кансоль
    tree = construct_tree()
    filename = 'images/tree.png'
    return send_file(filename, mimetype='image/gif')
