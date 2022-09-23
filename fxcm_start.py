import os
from configparser import ConfigParser

from typing import Dict, List, Union, Tuple
from functools import partial, update_wrapper

# EDIT ORIGIN LIB 2419 def __reconnect__
# EDIT ORIGIN LIB__init__

import fxcmpy

from dotenv import load_dotenv

load_dotenv(dotenv_path='.env')


def create_connection(access_token: str, log_level: str = 'debug', log_file: str = 'log.txt', server: str = 'demo'):
    """Create connection with FXCM"""
    connection = fxcmpy.fxcmpy(access_token=access_token, log_level=log_level, log_file=log_file, server=server)
    return connection


def round_data(float_digits: float, round_digit: int = 5) -> float:
    return round(float_digits, round_digit)


def determine_the_signal(symbol: str, value: Union[str, int], dict_symbol_matching: dict) \
        -> Tuple[bool, str, Union[str, int]]:
    list_map = dict_symbol_matching.get(symbol)
    if value in list_map:
        return True, value, ''
    return False, symbol, value, ''


def normalize_data(float_digits: float, round_int:int) -> int:
    """Custom normalize)))"""
    return int(str(round(float_digits, round_int)).split('.')[1][-3::])


def data_processing(msg, *args, dict_map=None):
    print(msg)
    pass


def func_create_dict_digits_for_symbol(dict_symbol: Dict, constant_list: List) -> Dict:
    result_dict = {}
    for symbol, value in dict_symbol.items():
        result_dict[symbol] = list(map(lambda x: x + int(value), constant_list))
    return result_dict


def wrapped_partial(func, *args, **kwargs):
    partial_func = partial(func, *args, **kwargs)
    update_wrapper(partial_func, func)
    return partial_func


def create_subscribe(dict_symbol: Dict, connection, func_callback=data_processing) -> None:
    callback = wrapped_partial(func_callback, dict_map=dict_symbol)
    for symbol in list(dict_symbol.keys())[:10]:
        connection.subscribe_market_data(symbol=symbol, add_callbacks=(callback,))


def read_conf(file: Union[str, None] = 'config.ini', name_section: str = 'symbol') -> Dict:
    dict_conf = {}
    config = ConfigParser()
    config.read(file)
    for options in config.options(name_section):
        data = config.get(name_section, options)
        dict_conf[options.upper()] = data
    return dict_conf


def preparing_data_from():
    data_constant_list = read_conf(name_section='CONSTANT_LIST').get('CONSTANT_LIST')
    CONSTANT_LIST = list(map(int, map(str.strip, data_constant_list.split(','))))
    data_symbol_dict = read_conf(name_section='symbol')
    dict_for_work = func_create_dict_digits_for_symbol(dict_symbol=data_symbol_dict, constant_list=CONSTANT_LIST)
    return dict_for_work


def start_server():
    TOKEN = os.getenv("TOKEN")
    dict_for_work = preparing_data_from()
    connection = create_connection(access_token=TOKEN)
    create_subscribe(dict_for_work, connection)
    return connection


if __name__ == "__main__":
    start_server()
