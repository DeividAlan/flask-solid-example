from abc import ABC, abstractmethod

class Exam(ABC):
    @abstractmethod
    def check_condition(self) -> None:
        pass

class BloodTest(Exam):
    def check_condition(self) -> None:
        # implement the specific conditions for the blood test
        pass

class XrayTest(Exam):
    def check_condition(self) -> None:
        # implement the specific conditions for the X-ray test
        pass

class ApproveExam:
    def approve_exam_request(self, exam: Exam):
        if exam.check_blood_test_conditions():
            print("Test approved!")

# Example of usage:
blood_test = BloodTest()
xray_test = XrayTest()

approver = ApproveExam()
blood_test_approver = approver.approve_exam_request(blood_test)
xray_test_approver =approver.approve_exam_request(xray_test)