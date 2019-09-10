import os
import numpy as np
from datetime import datetime

class DetailRecorder():
    '''
    Parameters:
        detail_dir: str
            The direction of a folder that the document of detail is saved. If detail_dir doesn't exisit, all of the inexistent folder will automatically be created.
        use_time_as_name: bool (default=True)
            Use current time as file name.
        file_name: str (default=None)
            Needed if use_time_as_name is False, and it won't be used while use_time_as_name is True.
        encoding: str (default='utf-8-sig')
            Type of encoding used to write the document.
        show_time: bool (default=False)
            Add full text of time in front of the input text.
    '''
    def __init__(self, detail_dir, use_time_as_name=True, file_name=None, encoding='utf-8-sig', show_time=False):
        # Check if detail_dir is a string.
        assert isinstance(detail_dir, str), 'detail_dir is needed to be a string.'

        # If use_time_as_name is true, using current time as file name.
        if use_time_as_name:
            file_name = datetime.now().strftime('%Y%m%d_%H%M%S')
        else:
            # Check if file_name is set when use_time_as_name is False.
            assert isinstance(file_name, str), 'file_name is needed if use_time_as_name is False.'

        self._encoding_ = encoding
        self._full_dir_ = '{:}/{:}.txt'.format(detail_dir, file_name)
        self._check_and_create_dir(detail_dir)
        self._show_time = show_time

    def dprint(self, *strings, enable_var_form=True):
        write_string = ''
        for string in strings:
            if enable_var_form:
                write_string += self._var_form(string) + ' '
            else:
                write_string += str(string) + ' '
        write_string = write_string[:-1]
        self._write_to_file(write_string)

    def dprint_line(self, symbol, times=60):
        write_string = str(symbol) * times
        self._write_to_file(write_string)

    def _var_form(self, var):
        # This method is made for making variable easily being copied to use in further coding.
        # check list, np.ndarray, tuple
        if type(var) in [list, np.ndarray, tuple]:
            if isinstance(var, list):
                temp_str, end_str = '[', ']'
            elif isinstance(var, np.ndarray):
                temp_str, end_str = 'np.array([', '])'
            elif isinstance(var, tuple):
                temp_str, end_str = '(', ')'

            if len(var) != 0:
                for v in var:
                    if isinstance(var, np.ndarray):
                        temp_str += self._var_form(v.tolist()) + ', '
                    else:
                        temp_str += self._var_form(v) + ', '
                temp_str = temp_str[:-2] + end_str
            else:
                temp_str += end_str

            return temp_str

        # check dict
        elif isinstance(var, dict):
            if len(var) != 0:
                temp_str = '{'
                for key, value in var.items():
                    temp_str += '{:}: {:}, '.format(self._var_form(key), self._var_form(value))
                temp_str = temp_str[:-2] + '}'
                return temp_str
            else:
                return '{}'
        else:
            return str(var)

    def _check_and_create_dir(self, detail_dir):
        arr_folder = detail_dir.split('/')
        current_dir = ''
        for f in arr_folder:
            current_dir += f
            if not os.path.isdir(current_dir):
                os.mkdir(current_dir)
            current_dir += '/'

    def _write_to_file(self, string):
        if self._show_time:
            write_string = '<{:}> {:}'.format(datetime.now().strftime('%Y/%m/%d %H:%M:%S.%f'), string)
        else:
            write_string = string

        if os.path.exists(self._full_dir_):
            write_string = '\n' + write_string
        # write
        with open(self._full_dir_, 'a', encoding=self._encoding_) as fp:
            fp.write(write_string)
