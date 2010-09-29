
import yaml

from configui.utils.coherse_name import coherse_name

def settings_list_from_yaml(yaml_filename):
    with open(yaml_filename) as infile:
        parsed_yaml = yaml.load(infile)
    # TODO check for proper yaml formatting
    settings_list = []
    for settings_dict in parsed_yaml:
        name = settings_dict.keys()[0]
        setting = settings_dict.values()[0]
        setting['name'] = coherse_name(name)
        settings_list.append(setting)
    return settings_list
