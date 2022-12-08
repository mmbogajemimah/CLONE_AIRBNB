## AirBnB clone - The console
-> The console helps to: Place the parent Class (BaseModel) to take care of the initialization, serialization and deserialization of future instances

-> Create a simple flow of serialization/deserialization: 
      Instance <-> Dictionary <-> JSON string <-> file
-> Create all classes used for AirBnB(User, state, City, Place, Amenities, Reviews ...) that inherit from the BaseModel
-> Create the first abstructed storage engine of the project: File Storage
-> Create Unitests to validate all our class and storage engine

#### The Command interpreter (CRUD)
-> Creates new Object
-> Retrive an Object from a file, a database
-> Do Operations on objects(count, compute stats, etc...)
-> Update attributes of an object
-> Destroy an object

Code must pass unit tests
python3 -m unittests discover tests
