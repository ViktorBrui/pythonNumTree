from anytree import Node, RenderTree
from anytree.exporter import DotExporter
from services.structure_data_service import StructureDataService
from services.logger import logger_instance


class TreeConstruct:
    tree_data = StructureDataService()

    def create_tree(self, node_count) -> list:
        build_tree = self.construct_tree(node_count)
        return build_tree

    def create_next_level_nodes(self, node_list, parent_node, has_parent=False) -> list:
        second_nodes_list = []

        if node_list:
            for node in node_list:
                second_nodes = Node(node, parent=parent_node)
                second_nodes_list.append(second_nodes)

                if has_parent:
                    parent_node = second_nodes

            return second_nodes_list
        else:
            logger_instance.log_warning(self.__class__.__name__ + ' - node_list is empty')

    def construct_tree(self, node_count) -> bool:
        items_sets = self.tree_data.get_lists(node_count)
        setitems = self.tree_data.get_sorted_int_list()
        first_node_level = Node(min(setitems), parent=None)
        next_node_level = []

        if items_sets:
            node_index = 1
            for node_columns in items_sets:

                node_index += 1
                if node_columns:
                    next_node_level.append(node_columns[0])

                elif not node_columns:
                    current_node_index = str(node_index)
                    logger_instance.log_warning(self.__class__.__name__ + ' - node list index = ' + current_node_index + ' - is empty')
                    next_node_level.append('')

            second_node_level = self.create_next_level_nodes(next_node_level, first_node_level)
            index = 0

            for next_node in second_node_level:
                if not items_sets[index]:
                    index += 1
                    node_index = str(index + 1)
                    logger_instance.log_warning(self.__class__.__name__ + ' - Node ' + node_index + ' is empty')

                else:
                    items_sets[index].pop(0)
                    self.create_next_level_nodes(items_sets[index], next_node, True)
                    index += 1

            draw_nodes = self.draw_image_png(first_node_level)

            return draw_nodes
        else:
            logger_instance.log_warning(self.__class__.__name__ + ' - Input number is < 2 or items_sets is empty')

    def draw_image_png(self, first_node) -> bool:
        for pre, fill, node in RenderTree(first_node):
            print("%s%s" % (pre, node.name))
        DotExporter(first_node, nodeattrfunc=lambda node: "fixedsize=true, width=1.25, height=1.25, shape=box",
                    edgeattrfunc=lambda parent, child: "style=bold").to_picture(
            "images/tree.png")
        return True
