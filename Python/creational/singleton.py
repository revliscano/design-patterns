class Singleton(type):

    _instance = None

    def __call__(cls):
        if not cls._instance:
            cls._instance = type.__call__(cls)
        return cls._instance


class Configuration(metaclass=Singleton):
    def __init__(self):
        print('Initializing configuration object')

    def set_some_setting(self):
        self.some_setting = 12345


conf = Configuration()
conf.set_some_setting()

conf_somewhere_else = Configuration()

print(conf.some_setting, conf_somewhere_else.some_setting)
if conf is conf_somewhere_else:
    print('Both names reference the same object')
