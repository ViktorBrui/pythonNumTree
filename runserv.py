import connexion
from flask import send_file
from services.constructTree import ConstructTree


def create_app():
    construct_tree = ConstructTree()
    tree = construct_tree.construct_tree()
    filename = 'images/tree.png'
    return send_file(filename, mimetype='image/gif')


if __name__ == '__main__':
    app = connexion.FlaskApp(__name__, specification_dir='openapi/')
    app.add_api('spec.yaml')
    app.run(debug=True)
