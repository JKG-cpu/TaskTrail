from src.logic import *
from pprint import pprint

ch = ClassHandler()

ch.add_class(
    class_name = "AP CSP",
    assignment_weight = 0.6,
    test_weight = 0.4
)

ch.add_assignment(
    class_name = "AP CSP",
    name = "Test Assignment"
)
ch.check_completed_assignment(
    class_name = "AP CSP",
    assignment_name = "Test Assignment",
    grade = "10/12"
)

ch.add_test(
    class_name = "AP CSP",
    name = "Unit Test",
    grade = "5/10"
)

worked = ch.calculate_overall("AP CSP")

pprint(ch.classes["AP CSP"])