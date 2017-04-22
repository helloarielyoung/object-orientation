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
    Should also have said:  a class is a blueprint description of objects
    including their methods and attributes.

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
class Student(object):
 
    """Store student data.

    Class attributes:
    last_name = student last name
    first_name = student first name
    address = student street address
    """

    def __init__(self, last, first, address):
        self.last_name = last
        self.first_name = first
        self.address = address

    #note: I would not have outdented the Address line, but found that to be the
    #only way to get the result to line up nicely in the terminal.
    def __repr__(self):
        return """Name: {} {}
Address: {}""".format(self.last_name, self.first_name, self.address)


class Question(object):
 
    """Create

    Class attributes:
    question = the text of the question
    correct_answer = the text of the answers

    Public methods:
    ask_and_evaluate()
    """

    def __init__(self, question, answer):
        self.question = question
        self.correct_answer = answer

    def __repr__(self):
        #note:  __repr__ can only return a STRING
        return "{'%s': '%s'}" % (self.question, self.correct_answer)

        #this format causes exam to return wrong data
        #return "question: %s, correct_answer: %s" % (self.question, self.correct_answer)
        #exam.questions
        # [[question: What day is it?, correct_answer: Saturday, 'Saturday']]
        #oh my gosh, i had to try so many different formats before I got
        #it right!

    def ask_and_evaluate(self):
        """Prompts user for answer to the question

        Returns True or False depending on whether user's answer matches
        correct_answer.
        """

        answer = raw_input(self.question + " >")

        #this works, but even more simple way is below
        # if answer == self.correct_answer:
        #     return True
        # else:
        #     return False
        return answer == self.correct_answer


class Exam(object):
 
    """Exam holds exam name and list of questions

    Class attributes:
    name = the name of the exam
    questions = a list of the questions and their answers

    Public methods:
    add_question(question, correct_answer)
    administer()
    """

    def __init__(self, name):
        self.name = name
        self.questions = []

    def __repr__(self):
        return self.name + str(self.questions)

    def add_question(self, question, correct_answer):
        """Makes an instance of Question and add to exam attributes

        Adds question and correct_answer to exam instance's attributes

        """

        new_question = Question(question, correct_answer)
        self.questions.append(new_question)

    def administer(self):
        """administers all the exam's questions and returns user's score."""

        count = 0
        score = 0

        #loop through the questions in questions
        for i, question in enumerate(self.questions):
            #ask the question and get answer
            answer = question.ask_and_evaluate()
            #keep track of questions
            count += 1
            #keep track of the score
            if answer:
                score += 1

        #return the score as a percentage
        return (float(score) / count) * 100
        #will need to change this to a decimal percentage of score/count


class StudentExam(object):
 
    """Stores a student, an exam, student's score for the exam.

    Class attributes:
    student = student's full name
    exam = name of the exam

    Public methods:
    take_test(student, exam)
    """
    score = 0

    def __init__(self, student, exam):
        self.student = student
        self.exam = exam

    def __repr__(self):
        return "Student: %s, Exam: %s, Score: %s" % (self.student, self.exam,
                                                     str(self.score))

    def take_test(self):  #removed incorrect parameters - alreayd have student & exam as class attributes
        """Admisters the exam, assigns the score to the StudentExam instance"""

        self.score = exam.administer()
        print "Your score:  " + str(self.score)


def example():
 
    """Creates an example exam.

    Creates an exam
    Adds a few questions to the exam
    Creates a student
    Instantiates a Student exam, passing the student and exam just created as
      arguments
    Administers the test for that student usint take_test method
    """
    #create an exam
    exam1 = Exam('midterm')
    #add questions to the exam
    exam1.add_question("What day is it", "Sunday")
    exam1.add_question("What month is it?", "April")

    #Create a student
    student1 = Student("Smith", "Joe", "120 Main St")

    #Instantiate Student exam
    student_exam1 = StudentExam(student1, exam1)
    #administer the exam
    student_exam1.take_test(student_exam1, exam1)


class Quiz(Exam):
    """Quiz holds quiz name and list of questions.

    Inherits from Exam, overrides administer to change the user's score
    from percentage to pass/fail

    Class attributes:
    name = the name of the quiz
    questions = a list of the questions and their answers

    Public methods:
    add_question(question, correct_answer)
    administer()
    """

    def __repr__(self):
        return self.name + str(self.questions)

    def administer(self):
        """administers all the exam's questions and returns user's score."""

        #This worked, but more elegant way is below using Super
        # count = 0
        # score = 0

        # #loop through the questions in questions
        # for i, question in enumerate(self.questions):
        #     #ask the question and get answer
        #     answer = question.ask_and_evaluate()
        #     #keep track of questions
        #     count += 1
        #     #keep track of the score
        #     if answer:
        #         score += 1

        # #calculate percentage
        # score = (float(score) / count) * 100

        super(Quiz, self).administer()

        if self.score >= 50:
            return "pass"
        return "fail"


class StudentQuiz(object):
 
    """Stores a student, a quiz, student's score for the quiz.

    Class attributes:
    student = student's full name
    quiz = name of the quiz

    Public methods:
    take_test(student, quiz)
    """
    score = 0

    def __init__(self, student, quiz):
        self.student = student
        self.quiz = quiz

    def __repr__(self):
        return "Student: %s, Quiz: %s, Score: %s" % (self.student, self.quiz,
                                                     self.score)

    def take_test(self, student, quiz):
        """Admisters the exam, assigns the score to the StudentQuiz instance"""

        self.score = quiz.administer()
        print "Your score:  " + self.score


def example_quiz():
    """Creates an example quiz.

    Creates an quiz
    Adds a few questions to the exam
    Creates a student
    Instantiates a Student exam, passing the student and exam just created as
      arguments
    Administers the test for that student usint take_test method
    """
    #create an exam
    quiz1 = Quiz('quiz')
    #add questions to the exam
    quiz1.add_question("What day is it", "Sunday")
    quiz1.add_question("What month is it?", "April")
    quiz1.add_question("What color is the sun?", "yellow")

    #Create a student
    student1 = Student("Smith", "Joe", "120 Main St")

    #Instantiate Student exam
    student_quiz1 = StudentQuiz(student1, quiz1)
    #administer the exam
    student_quiz1.take_test(student_quiz1, quiz1)
