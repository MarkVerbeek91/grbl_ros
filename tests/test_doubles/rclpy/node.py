from unittest import mock


class Node:
    def __init__(self, *args, **kwargs):
        pass

    def get_logger(self):
        return DummeLogger()

    def declare_parameters(self, **kwargs):
        pass

    def get_parameter(self, *_):
        return self.GetParameterDummy()

    class GetParameterDummy:
        class ParameterDummy:
            string_value = ""
            integer_value = 0

        @classmethod
        def get_parameter_value(cls):
            return cls.ParameterDummy()

    def create_publisher(self, *args):
        pass

    def create_service(self, *args):
        pass


class DummeLogger:
    @staticmethod
    def info(msg):
        pass

    @staticmethod
    def warn(msg):
        pass