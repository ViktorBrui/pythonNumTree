from anytree import Node, RenderTree
from anytree.exporter import DotExporter
from services.getTreeDataService import GetTreeData


class ConstructTree:
    # создание дерева и отрисовка его с помощью DotExporter
    def construct_tree(self):
        tree_data = GetTreeData()
        setitems = tree_data.get_sorted_int_list()
        second_items = tree_data.get_sqr_list_second_number()
        third_items = tree_data.get_sqr_list_third_number()
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
        DotExporter(first_el, nodeattrfunc=lambda node: "fixedsize=true, width=1, height=1, shape=box",
                    edgeattrfunc=lambda parent, child: "style=bold").to_picture(
            "images/tree.png")
        return True
