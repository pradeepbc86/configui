
class Presenter(object):
    def __init__(self):
        self._daos = {} # Delegate Attribute ObjectS

    def __setattr__(self, attribute_name, value):
        try:
            self.__dict__['_daos'][attribute_name].value = value
        except KeyError:
            self.__dict__[attribute_name] = value

    def __getattr__(self, attribute_name):
        try:
            return self.__dict__['_daos'][attribute_name].value
        except KeyError:
            try:
                return self.__dict__[attribute_name]
            except KeyError:
                raise AttributeError("%s instance has no attribute '%s'" %
                                     (self.__class__.__name__, attribute_name))

    def __dir__(self):
        '''This ensures that self._daos is NOT in dir() results, but all its
        keys are.'''
        return dir(self.__class__) + self._daos.keys()

    def add_delegated_attribute(self, attribute_name, attribute_object):
        self._daos[attribute_name] = attribute_object
        
