import os
import numpy as np
from datetime import datetime

class DetailRecorder():
    '''
        Parameters:
            detail_dir: str
                Direction of folder used to save the detail file.
            use_time_as_name: bool, optional (default: True)
                If true, it will use time as file name.
            file_name: str, optional (default: None)
                If use_time_as_name is False, file_name is needed.
            encoding: str, optional (default: 'utf-8-sig')
                Encoding type for writing file.
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

    def dprint(self, *strings, enable_var_former=True):
        write_string = ''
        for string in strings:
            if enable_var_former:
                write_string += self._var_former(string) + ' '
            else:
                write_string += str(string) + ' '
        write_string = write_string[:-1]
        if self._show_time:
            write_string = '<{:}> {:}'.format(datetime.now().strftime('%Y/%m/%d %H:%M:%S.%f'), write_string)

        if os.path.exists(self._full_dir_):
            write_string = '\n' + write_string
        # write
        with open(self._full_dir_, 'a', encoding=self._encoding_) as fp:
            fp.write(write_string)

    def _var_former(self, var):
        # This method is made for making variable easily being copied to use in further coding.

        # check int, float, string.
        if type(var) in [int, float, str, complex, np.int_, np.float_, np.complex_]:
            return str(var)

        # check list, np.ndarray, tuple
        elif type(var) in [list, np.ndarray, tuple]:
            if isinstance(var, list):
                temp_str, end_str = '[', ']'
            elif isinstance(var, np.ndarray):
                temp_str, end_str = 'np.array([', '])'
            elif isinstance(var, tuple):
                temp_str, end_str = '(', ')'

            for v in var:
                temp_str += self._var_former(v) + ', '
            temp_str = temp_str[:-2] + end_str

            return temp_str

        # check dict
        elif isinstance(var, dict):
            temp_str = '{'
            for key, value in var.items():
                temp_str += '{:}: {:}, '.format(self._var_former(key), self._var_former(value))
            temp_str = temp_str[:-2] + '}'
            return temp_str

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
