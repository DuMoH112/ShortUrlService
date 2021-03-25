from time import time

import redis

from app.config import config


class Redis_db:
    def __init__(self):
        self.connect = redis.Redis(
            host=config['REDIS']['REDIS_HOST'],
            port=config['REDIS']['REDIS_PORT'],
            password=config['REDIS']['REDIS_PASSWORD'],
            db=config['REDIS']['REDIS_DB_REPLIC']
        )
        self.error = None

        try:
            self.check_connect(self.connect)
        except Exception as e:
            self.print_error(e)
            self.error = "Ошибка при подключении к Redis"

    def check_connect(self, conn):
        conn.get("ping")

    def close_connection(self):
        del self.connect

        return True

    def __byte_to_str(func):
        def the_wrapper_around_the_original_function(self, *args, **kwargs):
            result = func(self, *args, **kwargs)
            if func.__name__ == 'select_data':
                return result.decode()
            elif func.__name__ == 'hm_select_data':
                return [val.decode() for val in result]

        return the_wrapper_around_the_original_function

    def __handler_exceptions(func):
        def the_wrapper_around_the_original_function(self, *args, **kwargs):
            result = None
            try:
                result = func(self, *args, **kwargs)
            except Exception as e:
                self.print_error(e)

            return result

        return the_wrapper_around_the_original_function

    def print_error(self, e):
        print(f"""
===============REDIS_ERROR===============
    type: {type(e)},
    arguments: {e.args},
    text: {e},
    time: {time()}
=========================================
                """)

    @__handler_exceptions
    def insert_data(self, field, value):
        self.connect.set(field, value)

        return True

    @__handler_exceptions
    def hm_insert_data(self, name, dict_):
        self.connect.hmset(name=name, mapping=dict_)

        return True

    @__handler_exceptions
    def del_data(self, field):
        res = self.connect.delete(field)

        return res

    @__handler_exceptions
    @__byte_to_str
    def select_data(self, field):
        res = self.connect.get(field)

        return res

    @__handler_exceptions
    @__byte_to_str
    def hm_select_data(self, name, fields):
        res = self.connect.hmget(name=name, keys=fields)

        return res
