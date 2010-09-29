
from configui.utils import coherse_name

class ConfigurationObject(object):
    def __init__(self, settings_list):
        self.metadata = {}
        for setting in settings_list:
            name = setting['name']
            value = setting['value']
            del setting['name']
            del setting['value']
            setattr(self, name, value)
            self.metadata[name] = setting
