
from configui.utils import coherse_name
from configui.presenter import Presenter
from configui.type_classes import type_registry

class ConfigurationObject(Presenter):
    def __init__(self, settings_list):
        Presenter.__init__(self)
        for setting in settings_list:
            name = setting['name']
            value = setting['value']
            del setting['name']
            del setting['value']

            if 'type' in setting.keys():
                if setting['type'] in type_registry.keys():
                    attribute_type = type_registry[setting['type']]
                else:
                    attribute_type = type_registry['default']
                attribute_object = attribute_type(value=value, 
                                                  metadata=setting)

            self.add_delegated_attribute(name, attribute_object)
