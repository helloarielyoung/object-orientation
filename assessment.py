"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.

   Abstraction, which means hiding details we don't need, such as not having
   to know how a method or function works, only needing to know what it does and
   how to use it.  For example, we don't need to know anything about how list()
   turns the input into a list, we just need to know how parameters to pass it
   in order to use it to make lists.

   Encapsulation, which means keeping everything together.  Data and it's
   functionality are kept in one place.  An example of encapsulation is classes,
   where data (the values in class or instance attributes) are kept right in
   the same code as the functionality (the methods.)

   Polymorphism, which refers to the interchangeablilty of components,
   such as having a method with the same name in a class and a subclass which
   do different things.

2. What is a class?
    A class is a type of thing.

3. What is an instance attribute?
    It is an attibute of an instance of a class.  When you change the value,
    it changes just for this instance, not the whole class.

4. What is a method?
    A method is a function defined within a class.

5. What is an instance in object orientation?
    It's like a copy of a class.  When you instantiate an object from
    a class, it makes an instance - or a copy - of that class that is
    now it's own thing.

6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.
   A class attribute stays the same for all instances of the class.
   You usually use a class attribute for things that are constants, and
   use instance attributes for things that might be different in different
   instances.  For example, if I have a class Elephants, a class attribute
   might be species = 'elephant' because they're all elephants, while an 
   instance attribute might be elephant_type, which could have the values
   such as 'African', 'pink', 'Borneo', or 'stuffed'.

"""


# Parts 2 through 5:
# Create your classes and class methods
class StudentData(object):
    """A class for students

    Class attributes:
    last_name = student last name
    first_name = student first name
    address = student street address



    """

    def __init__(self, last, first, address):
        self.last_name = last
        self.first_name = first
        self.address = address

    def __repr__(self):
        print "Name: " + self.last_name + self.first_name
        print "Address: " + self.address


class QuestionAndAnswer(object):
    """A class of questions and answers

    Class attributes:
    question = the text of the question
    correct_answer = the text of the answers
    """

    def_