
import yaml

from configui.utils.coherse_name import coherse_name

def settings_list_from_yaml(yaml_file):
    parsed_yaml = yaml.load(yaml_file)
    # TODO check for proper yaml formatting
    settings_list = []
    for settings_dict in parsed_yaml:
        name = settings_dict.keys()[0]
        setting = settings_dict.values()[0]
        cohersed_setting = {}
        for key, value in setting.items():
            cohersed_setting[coherse_name(key)] = value
        cohersed_setting['name'] = coherse_name(name)
        settings_list.append(cohersed_setting)
    return settings_list
