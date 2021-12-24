import connexion
from services.logger import logger_instance
import os
from flask import request, redirect


class TxtParser:

    file_data_list = []
    UPLOAD_FOLDER = './uploads'
    ALLOWED_EXTENSIONS = {'txt'}

    def parser_txt_file(self) -> bool:
        if request.method == 'POST':
            if 'txtFile' not in request.files:
                logger_instance.log_warning(self.__class__.__name__ + ' - File can`t read')
                return

            file = request.files['txtFile']

            if file.filename == '':
                logger_instance.log_warning(self.__class__.__name__ + ' - Filename isn`t exist')
                return redirect(request.url)

            if file and self.allowed_file(file.filename):
                file.save(os.path.join(self.UPLOAD_FOLDER, 'numbers.txt'))

        return True

    def allowed_file(self, filename) -> bool:
        return '.' in filename and \
               filename.rsplit('.', -1)[1].lower() in self.ALLOWED_EXTENSIONS

    def get_txt_file_data(self, data, filename) -> list:
        if data and self.allowed_file(filename):
            self.file_data_list.clear()
            self.file_data_list.append(data)

            return self.file_data_list

        else:
            self.file_data_list.clear()
            logger_instance.log_warning(self.__class__.__name__ + ' - The downloaded file extension is not .txt...')
