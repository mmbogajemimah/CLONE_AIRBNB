#!/usr/bin/python3
# This class defines all common attributes/methods inherited by other classes because they are common.

import uuid
from datetime import datetime

class BaseModel:
    # All classes have an __init__ function that is executed when the class is being initiated
    id = str(uuid.uuid4())
    created_at = datetime.now()
    updated_at = datetime.now()
    # A Pythonic way to convert Python objects into strings by using __str__
    # This method must return the String object.
    def __str__(self):
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'

    # Public Instance Methods
    def save(self):
        self.updated_at = datetime.now()
        return self.updated_at

    def to_dict(self):
        return self.__dict__
        
        

instance = BaseModel()
print(instance.id)
print(instance.created_at)
print(instance.updated_at)
print(instance.__class__.__name__)

print(instance.__str__())
print(instance.save())
print(instance.to_dict())