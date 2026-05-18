from typing import Literal
from fractions import Fraction

__all__ = [
    "ClassHandler"
]

class ClassHandler:
    def __init__(self) -> None:
        self.classes = {}

    # Manage class data    
    #region
    def add_class(self, class_name: str, assignment_weight: float = 0.50, test_weight: float = 0.50) -> bool:
        if class_name in self.classes:
            return False
        
        self.classes[class_name] = {
            "name": class_name,
            "percent": None,
            "assignment_weight": assignment_weight,
            "test_weight": test_weight,
            "assignments": {},
            "tests": {}
        }
        return True

    def remove_class(self, class_name: str) -> bool:
        if class_name not in self.classes:
            return False

        del self.classes[class_name]
        return True
    #endregion

    # Manage Assignments
    #region
    def add_assignment(self, class_name: str, name: str) -> bool:
        if class_name not in self.classes:
            return False

        if name in self.classes[class_name]["assignments"]:
            return False
        
        self.classes[class_name]["assignments"][name] = {
            "name": name,
            "grade": 0,
            "completed": False
        }
        return True

    def remove_assignment(self, class_name: str, assignment_name: str) -> bool:
        if class_name not in self.classes:
            return False
        
        if assignment_name not in self.classes[class_name]["assignments"]:
            return False

        del self.classes[class_name]["assignments"][assignment_name]
        return True
    
    def check_completed_assignment(self, class_name: str, assignment_name: str, grade: str) -> bool:
        if class_name not in self.classes:
            return False
        
        if assignment_name not in self.classes[class_name]["assignments"]:
            return False
        
        self.classes[class_name]["assignments"][assignment_name]["completed"] = True
        self.classes[class_name]["assignments"][assignment_name]["grade"] = Fraction(grade)
        return True
    #endregion

    # Manage Tests
    #region
    def add_test(self, class_name: str, name: str, grade: str) -> bool:
        if class_name not in self.classes:
            return False
        
        if name in self.classes[class_name]["tests"]:
            return False
        
        self.classes[class_name]["tests"][name] = {
            "name": name,
            "grade": Fraction(grade)
        }
        return True

    def remove_test(self, class_name: str, name: str) -> bool:
        if class_name not in self.classes:
            return False
        
        if name not in self.classes[class_name]["tests"]:
            return False

        del self.classes[class_name]["tests"][name]
        return True
    #endregion

    # Calculations
    #region
    def _get_scores(self, class_name: str, category: Literal["assignments", "tests"]) -> tuple[float | int, bool]:
        if category == "assignments":
            assignments: dict = self.classes.get(class_name).get("assignments")
            assignment_weight: float = self.classes.get(class_name).get("assignment_weight")
            
            if not assignments:
                return (0, False)

            average_assigments = 0
            count = 0
            for assignment in assignments:
                average_assigments += assignments[assignment]["grade"].numerator / assignments[assignment]["grade"].denominator
                count += 1
            
            average_assigments = average_assigments / count

            return (round(average_assigments * assignment_weight, 2), True)

        elif category == "tests":
            tests = self.classes.get(class_name).get("tests")
            test_weight = self.classes.get(class_name).get("test_weight")

            if not tests:
                return (0, False)

            average_tests = 0
            count = 0
            for test in tests:
                average_tests += tests[test]["grade"].numerator / tests[test]["grade"].denominator
                count += 1
            
            average_tests = average_tests / count

            return (round(average_tests * test_weight, 2), True)

    def calculate_overall(self, class_name: str) -> bool:
        if class_name not in self.classes:
            raise TypeError(
                f"Class name: {class_name} not in self.classes.\nself.classes contains {str(self.classes.keys())}"
            )
    
        overall_grade = 0.0
        active_weight = 0.0

        for category in ["assignments", "tests"]:
            score, is_valid = self._get_scores(class_name, category)
            if is_valid:
                overall_grade += score
                weight_key = f"{category[:-1]}_weight"
                active_weight += self.classes[class_name][weight_key]

        if active_weight == 0:
            return False

        result = round(overall_grade / active_weight, 4)
        self.classes[class_name]["percent"] = int(result * 100)
        return True
    #endregion

    # Get Data
    #region
    def get_class_names(self) -> list[str]:
        return list(self.classes.keys())
    #endregion
