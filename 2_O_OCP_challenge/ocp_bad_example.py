'''
OPEN CLOSED PRINCIPLE

Imagine that a veterinary clinic has its own system for approving exams. Initially, 
it has a method for verifying blood tests. Later, 
it adds an X-ray exam. We notice in the code that as the clinic adds more exams, 
new validation methods for each exam will need to be added. 
This would increase the code complexity and make it harder to maintain.

The solution for this case can be addressed using the Open-Closed Principle (OCP).

Using the concept of OCP, 
create an interface and classes that implement it so that if the clinic needs a new type of exam, 
a new class can be added, implementing the methods from a standard interface for exams.

'''


class ApproveExam:
    def approve_exam_request(self, exam):

        if blood_exam.type == "blood":
            if approver.check_blood_test_conditions(blood_exam):
                print("Blood test approved!")

        elif xray_exam.type == "xray":
            if approver.check_xray_conditions(xray_exam):
                print("X-ray approved!")
                pass

    def check_blood_test_conditions(self, exam):
        # implement the specific conditions for the blood test
        pass

    def check_xray_conditions(self, exam):
        # implement the specific conditions for the X-ray test
        pass

# Example of usage:
class Exam:
    def __init__(self, type):
        self.type = type

blood_exam = Exam("blood")
xray_exam = Exam("xray")

approver = ApproveExam()