from configui import load

# create a configuration_object from the yaml file
with open('simple.yaml') as infile:
    configuration_object = load(infile)

# The object has member variables associated with the entries
#    from the yaml file.

# alpha was defined as an int, but given nothing else it will
#    use the defaults.
print configuration_object.alpha
# >>> None

# it supports assignment as well
configuration_object.alpha = 42
print configuration_object.alpha
# >>> 42

# if you assign a floating point number, it will become an int()
configuration_object.alpha = 4.2
print configuration_object.alpha
# >>> 4

# trying to assign things that cannot become integers throw errors.
configuration_object.alpha = 'Frank'
"""
 >>> Traceback (most recent call last):
  File "simple.py", line 27, in <module>
    configuration_object.alpha = 'Frank'
  File "/home/davidmorton/configui/configui/presenter.py", line 8, in __setattr__
    self.__dict__['_daos'][attribute_name].value = value
  File "/home/davidmorton/configui/configui/type_classes.py", line 51, in value
    self._value = int(new_value)
ValueError: invalid literal for int() with base 10: 'Frank'
"""
