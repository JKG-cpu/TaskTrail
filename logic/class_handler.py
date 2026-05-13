from typing import Literal
from fractions import Fraction

__all__ = [
    "ClassHandler"
]

"""
Class Data Model

{
    "name": ...,
    "percent": ...,
    "assignment_weight": 0,
    "test_weight": 0,
    "assignments": [],
    "tests": []
}

Assignment Data Model
{
    "name": ...,
    "score": fractions.Fraction,
    "due_date": ...,
    "date_turned_in": ...,
    "completed: bool
}

Forumals

Assignments + Test:
    (Test(s) Avgs * Weight) + (Assignment(s) Avgs * Weight)

Empty Section:
    (Category Avg * Weight) / Active Weights

    EXAMPLE:
        assignments = 40% weight, 90%
        tests = 60% weight, 0% (No assignments)

        0.40 = Full weight (No tests = No 60%)

        90 * 0.40 = 36
        36 / 0.40 = 90%

"""

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
            "assignments": [
                {
                    "name": "assignment",
                    "score": Fraction(2, 2),
                    "due_date": "",
                    "date_turned_in": "",
                    "completed": True
                }
            ],
            "tests": []
        }
        return True

    def remove_class(self, class_name: str) -> bool:
        if class_name not in self.classes:
            return False

        del self.classes[class_name]
        return True
    #endregion

    # Calculations
    def _get_scores(self, class_name: str, category: Literal["assignments", "tests"]) -> tuple[float | int, bool]:
        if category == "assignments":
            assignments: list[dict] = self.classes.get(class_name).get("assignments")
            assignment_weight: float = self.classes.get(class_name).get("assignment_weight")
            
            if not assignments:
                return (0, False)

            average_assigments = 0
            count = 0
            for assignment in assignments:
                average_assigments += assignment["score"].numerator / assignment["score"].denominator
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
                average_tests += test["score"].numerator / test["score"].denominator
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
