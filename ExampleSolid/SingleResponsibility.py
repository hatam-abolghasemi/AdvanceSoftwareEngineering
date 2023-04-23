# Single Responsibility


# example one
class Student:
    """
    wrong way
    """

    def __init__(self):
        pass

    def register_student(self):
        pass

    def calculate_student_results(self):
        pass

    def send_email(self):
        pass


# *********************************************
# correct way


class StudentRegister:
    """
    correct way
    """

    def __init__(self):
        pass

    def register_student(self):
        pass


class StudentResult:
    """
    correct way
    """

    def __init__(self):
        pass

    def calculate_student_results(self):
        pass


class StudentEmails:
    """
    correct way
    """

    def __init__(self):
        pass

    def send_email(self):
        pass


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# example two


class Students:
    """
    wrong way
    """

    def __init__(
        self,
        student_id,
        first_name,
        last_name,
        dob,
        email,
        address1,
        address2,
        state,
        city,
        zipcode,
    ):
        self.student_id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.email = email
        self.address1 = address1
        self.address2 = address2
        self.state = state
        self.city = city
        self.zipcode = zipcode

    def save(self):
        print("Starting Save()")
        print("End Save()")

    def delete(self):
        print("Starting Delete()")
        print("End Delete()")

    def subscribe(self, cs):
        print("Starting Subscribe()")
        if cs.Type != "online":
            pass
        elif cs.type == "live":
            pass
        print("End Subscribe()")


# **************************************
# correct way


class StudentUser:
    """
    correct way
    """

    def __init__(
        self,
        student_id,
        first_name,
        last_name,
        dob,
        email,
        address1,
        address2,
        state,
        city,
        zipcode,
    ):
        self.student_id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.email = email
        self.address1 = address1
        self.address2 = address2
        self.state = state
        self.city = city
        self.zipcode = zipcode

    def save(self):
        print("Starting Save()")
        print("End Save()")

    def delete(self):
        print("Starting Delete()")
        print("End Delete()")


class Logger:
    """
    correct way
    """

    def log(self, message):
        print(message)


class StudentRepository:
    """
    correct way
    """

    def save(self, std):
        Logger().log("Starting Save()")
        Logger().log("Ending Saving()")

    def delete(self):
        Logger().log("Starting Delete()")
        Logger().log("Ending Delete()")

    def save_course(self, std, cs):
        Logger().log("Starting SaveCourse()")

        Logger().log("Ending SaveCourse()")


class EmailManager:
    """
    correct way
    """

    def send_email(self, recEmailed="", senderEmailId="", subject="", message=""):
        pass


class PaymentManger:
    """
    correct way
    """

    def process_payment(self):
        pass


class Course:
    """
    correct way
    """

    def __init__(self, cource_id, title, type):
        self.cource_id = cource_id
        self.title = title
        self.type = type

    def subscribe(self, std):
        Logger().log("Starting Subscribe()")
        if self.type == "online":
            pass
        elif self.type == "live":
            pass

        PaymentManger().process_payment()

        EmailManager().send_email()

        Logger().log("End Subscribe()")
