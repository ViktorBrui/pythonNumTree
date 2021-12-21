from anytree import Node, RenderTree
from anytree.exporter import DotExporter
from services.dataService import DataLists
import logging
logging.basicConfig(level=logging.INFO, filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %('
                                                                                 'message)s')


class TreeConstruct:

    def create_tree(self) -> list:
        tree_return = self.construct_tree()
        return tree_return

    @staticmethod
    def create_next_level_nodes(node_list, parent_node, has_parent=False) -> list:
        second_nodes_list = []
        if node_list:
            for node in node_list:
                second_nodes = Node(node, parent=parent_node)
                second_nodes_list.append(second_nodes)
                if has_parent:
                    parent_node = second_nodes
            return second_nodes_list
        else:
            logging.warning('node_list is empty')

    def construct_tree(self) -> list:
        tree_data = DataLists()
        items_sets = tree_data.get_lists()
        setitems = tree_data.get_sorted_int_list()
        first_node_level = Node(min(setitems), parent=None)
        next_node_level = []
        if items_sets:
            for node_columns in items_sets:
                if node_columns:
                    next_node_level.append(node_columns[0])
                elif not node_columns:
                    logging.warning('node columns is empty')
                    next_node_level.append('')
            second_node_level_origin = self.create_next_level_nodes(next_node_level, first_node_level)
            index = 0
            for next_node in second_node_level_origin:
                if not items_sets[index]:
                    index += 1
                    logging.warning('Node is empty')
                    pass
                else:
                    items_sets[index].pop(0)
                    self.create_next_level_nodes(items_sets[index], next_node, True)
                    index += 1
            for pre, fill, node in RenderTree(first_node_level):
                print("%s%s" % (pre, node.name))
            DotExporter(first_node_level, nodeattrfunc=lambda node: "fixedsize=true, width=1, height=1, shape=box",
                        edgeattrfunc=lambda parent, child: "style=bold").to_picture(
                "images/new-tree.png")
            return next_node_level
        else:
            logging.warning('Input number is < 2 or items_sets is empty')


