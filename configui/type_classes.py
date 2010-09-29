import yaml

class BasicAttribute(object):
    def __init__(self, value=None, metadata={}):
        self.metadata = metadata
        self.process_metadata()
        self._value = None
        self.value = value

    def process_metadata(self):
        metadata = self.metadata
        actionable_attributes = ['mouseover_text', 'style']
        for attribute_name in actionable_attributes:
            if attribute_name in metadata.keys():
                setattr(self, attribute_name, metadata[attribute_name])
            else:
                setattr(self, attribute_name, None)

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = new_value

class IntAttribute(BasicAttribute):
    def process_metadata(self):
        BasicAttribute.process_metadata(self)
        metadata = self.metadata
        actionable_attributes = ['min_value', 'max_value']
        for attribute_name in actionable_attributes:
            if attribute_name in metadata.keys():
                setattr(self, attribute_name, metadata[attribute_name])
            else:
                setattr(self, attribute_name, None)

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

type_registry = {'default':BasicAttribute,
                 'int':IntAttribute}

