import connexion
from flask import send_file
from services.tree_construct_service import TreeConstruct


def create_app():
    filename = 'images/tree.png'
    return send_file(filename, mimetype='image/gif')


def create_tree():
    construct_tree = TreeConstruct()
    tree = construct_tree.create_tree()
    filename = 'images/new-tree.png'
    return send_file(filename, mimetype='image/gif')


if __name__ == '__main__':
    app = connexion.FlaskApp(__name__, specification_dir='openapi/')
    app.add_api('spec.yaml')
    app.run(debug=True)
