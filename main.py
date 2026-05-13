from logic import *

ch = ClassHandler()

ch.add_class(
    class_name = "AP CSP",
    assignment_weight = 0.6,
    test_weight = 0.4
)

worked = ch.calculate_overall("AP CSP")

print(ch.classes["AP CSP"])