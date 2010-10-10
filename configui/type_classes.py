
import random

class BasicAttribute(object):
    def __init__(self, value=None, metadata={}):
        actionable_attributes = {'mouseover_text': 'This is a Basic Attribute',
                                 'style': None}
        self.process_metadata(actionable_attributes, metadata)
        self._value = None

    def process_metadata(self, actionable_attributes, metadata):
        if hasattr(self, 'metadata'):
            self.metadata.update(metadata)
        else:
            self.metadata = metadata

        for attribute_name, default_value in actionable_attributes.items():
            if attribute_name in metadata.keys():
                setattr(self, attribute_name, metadata[attribute_name])
            else:
                setattr(self, attribute_name, default_value)

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = new_value

class IntAttribute(BasicAttribute):
    def __init__(self, value=None, metadata={}):
        BasicAttribute.__init__(self, value=value, metadata=metadata)
        actionable_attributes = {'min_value': None, 
                                 'max_value': None}
        self.process_metadata(actionable_attributes, metadata)
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if self.max_value is not None and new_value > self.max_value:
            new_value = int(self.max_value)
        elif self.min_value is not None and new_value < self.min_value:
            new_value = int(self.min_value)
        if new_value != self._value:
            # TODO publish change
            self._value = int(new_value)

class RandomNormalAttribute(BasicAttribute):
    def __init__(self, value=None, metadata={}):
        BasicAttribute.__init__(self, value=value, metadata=metadata)
        actionable_attributes = {'average_value': 0.0, 
                                 'standard_deviation': 1.0,
                                 'recalculating': True}
        self.process_metadata(actionable_attributes, metadata)

    @property
    def value(self):
        if self.recalculating or self._value is None:
            self._value = random.normalvariate(self.average_value, 
                                               self.standard_deviation)
        return self._value

    @value.setter
    def value(self, new_value):
        raise NotImplementedError('RandomNormalAttributes cannot be set.')

type_registry = {'default':BasicAttribute,
                 'int':IntAttribute,
                 'random-normal': RandomNormalAttribute}

