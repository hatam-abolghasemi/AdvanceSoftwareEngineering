# example one
# wrong way

from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def fly(self):
        pass


class Aircraft(Vehicle):
    def go(self):
        print("Taxiing")

    def fly(self):
        print("Flying")


class Car(Vehicle):
    def go(self):
        print("Going")

    def fly(self):
        raise Exception("The car cannot fly")


# correct way


class Movable(ABC):
    @abstractmethod
    def go(self):
        pass


class Flyable(Movable):
    @abstractmethod
    def fly(self):
        pass


class AircraftCorrect(Flyable):
    def go(self):
        print("Taxiing")

    def fly(self):
        print("Flying")


class CarCorrect(Movable):
    def go(self):
        print("Going")


# example 2
# wrong way


class IStudentRepository:
    @abstractmethod
    def AddStudent(self, std):
        pass

    @abstractmethod
    def EditStudent(self, std):
        pass

    @abstractmethod
    def DeleteStudent(self, std):
        pass

    @abstractmethod
    def AddCourse(self, cs):
        pass

    @abstractmethod
    def EditCourse(self, cs):
        pass

    @abstractmethod
    def DeleteCourse(self, cs):
        pass

    @abstractmethod
    def SubscribeCourse(self, cs):
        pass

    @abstractmethod
    def UnSubscribeCourse(self, cs):
        pass

    @abstractmethod
    def GetAllStudents(self):
        pass

    @abstractmethod
    def GetAllCourse(self):
        pass

    @abstractmethod
    def GetAllCourses(self, std):
        pass


class StudentRepository(IStudentRepository):
    def AddCourse(self, cs):
        pass
        # implementation code removed for better clarity

    def AddStudent(self, std):
        pass
        # implementation code removed for better clarity

    def DeleteCourse(self, cs):
        pass
        # implementation code removed for better clarity

    def DeleteStudent(self, std):
        pass
        # implementation code removed for better clarity

    def EditCourse(self, cs):
        pass
        # implementation code removed for better clarity

    def EditStudent(self, std):
        pass
        # implementation code removed for better clarity

    def GetAllCourse(self):
        pass
        # implementation code removed for better clarity

    def GetAllCourses(self, std):
        pass
        # implementation code removed for better clarity

    def GetAllStudents(self):
        pass
        # implementation code removed for better clarity

    def SubscribeCourse(self, cs):
        pass
        # implementation code removed for better clarity

    def UnSubscribeCourse(self, cs):
        pass
        # implementation code removed for better clarity


# correct way


class IStudentRepository(ABC):
    @abstractmethod
    def AddStudent(self, std):
        pass

    @abstractmethod
    def EditStudent(self, std):
        pass

    @abstractmethod
    def DeleteStudent(self, std):
        pass

    @abstractmethod
    def SubscribeCourse(self, cs):
        pass

    @abstractmethod
    def UnSubscribeCourse(self, cs):
        pass

    @abstractmethod
    def GetAllStudents(self):
        pass


class ICourseRepository(ABC):
    @abstractmethod
    def AddCourse(self, cs):
        pass

    @abstractmethod
    def EditCourse(self, cs):
        pass

    @abstractmethod
    def DeleteCourse(self, cs):
        pass

    @abstractmethod
    def GetAllCourse(self):
        pass

    @abstractmethod
    def GetAllCourses(self, std):
        pass
