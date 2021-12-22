import connexion
from flask import send_file
from services.tree_construct_service import TreeConstructService
from services.parser import TxtParser

parser = TxtParser()
construct_tree = TreeConstructService()


def create_app():
    template = 'templates/HomePage.html'
    return send_file(template, mimetype='html')


def upload_and_create_tree():
    log = parser.parser_txt_file()
    print("log", log)
    nodes_count = parser.get_nodes_count_from_page()
    construct_tree.create_tree(nodes_count)
    filename = 'images/new-tree.png'
    return send_file(filename, mimetype='image/gif')


def create_tree():
    tree = construct_tree.create_tree(7)
    filename = 'images/new-tree.png'
    return send_file(filename, mimetype='image/gif')


if __name__ == '__main__':
    app = connexion.FlaskApp(__name__, specification_dir='openapi/')
    app.add_api('spec.yaml')
    app.run(debug=True)

