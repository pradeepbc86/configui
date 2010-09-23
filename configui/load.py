from configui.settings_list_from_yaml import settings_list_from_yaml
from configui.configuration_object import ConfigurationObject

def load(yaml_filename):
    settings_list = settings_list_from_yaml(yaml_filename)
    return ConfigurationObject(settings_list)
