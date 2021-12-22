from services.logger import logger_instance
import os
from flask import request, redirect


class TxtParser:

    UPLOAD_FOLDER = './uploads'
    ALLOWED_EXTENSIONS = {'txt'}

    def parser_txt_file(self) -> bool:
        if request.method == 'POST':

            if 'file' not in request.files:
                logger_instance.log_warning(self.__class__.__name__ + ' - File can`t read')
                return

            file = request.files['file']

            if file.filename == '':
                logger_instance.log_warning(self.__class__.__name__ + ' - Filename isn`t exist')
                return redirect(request.url)

            if file and self.allowed_file(file.filename):
                file.save(os.path.join(self.UPLOAD_FOLDER, 'numbers.txt'))

        return True

    def allowed_file(self, filename) -> bool:
        return '.' in filename and \
               filename.rsplit('.', 1)[1].lower() in self.ALLOWED_EXTENSIONS

    def get_nodes_count_from_page(self) -> int:
        node_count = request.form.get('nodeCount')
        return int(node_count)
