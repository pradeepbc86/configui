from configui.settings_list_from_yaml import settings_list_from_yaml
from configui.configuration_object import ConfigurationObject

def load(yaml_file):
    settings_list = settings_list_from_yaml(yaml_file)
    return ConfigurationObject(settings_list)
