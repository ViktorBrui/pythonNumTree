import connexion
from flask import send_file
from services.reader import TxtReader
from services.tree_construct import TreeConstruct
from services.parser import TxtParser

parser = TxtParser()
reader = TxtReader()
construct_tree = TreeConstruct()
image_filename = 'images/tree.png'


def create_app():
    template = 'templates/HomePage.html'
    return send_file(template, mimetype='html')


def upload_and_create_tree():
    uploads_count_nodes()
    return send_file(image_filename, mimetype='image/gif')


def create_tree():
    tree = construct_tree.create_tree(5)
    return send_file(image_filename, mimetype='image/gif')


def upload_txt_file_to_storage():
    file = connexion.request.files['txtFile']
    file.seek(0)
    filename = file.filename
    parser.get_txt_file_data(file.read(), filename)
    return file


def uploads_count_nodes():
    count_nodes = connexion.request.form['countNodes']
    upload_txt_file_to_storage()
    construct_tree.create_tree(int(count_nodes))


if __name__ == '__main__':
    app = connexion.FlaskApp(__name__, specification_dir='openapi/')
    app.add_api('spec.yaml')
    app.run(debug=True)

