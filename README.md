## Classes and Objects
* Noun => Class
* Adjective => Attribute => properties that define your class further
* Verb => Method => functions that perform a specific task
* Everything in Python is an object

## Attributes and Methods
* A **class attribute** is common to all the instances of your class
* An **instance attribute** is specific to each instance of your class
* Check the class attribute first, and then check the instance attribute
* The lifespan of attributes with **self** parameter: creation to deletion an object
* Otherwise, the lifespan is only within the method
* Instance Methods are methods of your class that make use of self parameter to access and modify the instance attribute of your class
* Static Methods are methods that do not take the default self parameter and ignore the binding of the object
* decorators (@): functions that take another function and extend their functionality
* init method: the first method being called at the time of object creation

## Abstraction and Encapsulation
* Encapsulation is done to achieve abstraction
* Encapsulation is the process of hiding implementation details from the users
* For example, listName.append() -> list is a **class**, append is the **method** encapsulated by the class

## Inheritance
* Child class inherits certain characteristics and features from parent class
* Child class can have its own attributes and methods and have access to attributes and methods of the parent class
* Single inheritance
* Multiple inheritance: the value of the same attribute names from multiple base classes depends on the order of inheritance
* Multi-level inheritance: the lower level classes will have access to all the attributes and methods to all the classes in the upper levels.
* Public: memberName, accessible to your class, derived classes, and anywhere outside your derived classes
* Protected: _memberName, accessible to your class, derived classes
* Private: __memberName, only accessible to your class
