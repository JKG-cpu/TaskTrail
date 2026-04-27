from ..helpers import *

class ClassHandler:
    def __init__(self):
        self.class_data = None
        self.letter_grades = {
            90: "A",
            80: "B",
            70: "C",
            60: "D"
        }

    # Helpers
    def _letter_grade(self, percent: str) -> str: 
        percent = int(percent)
        for num in self.letter_grades.keys():
            if percent > num:
                return self.letter_grades[num]

        return "F"

    # Callables
    def set_data(self, data: dict | None) -> None: self.class_data = data

    def get_assignments(self) -> list[tuple[str, dict]] | None: 
        return None if self.class_data is None else [
            (
                str(key), 
                self.class_data[key]["assignments"]
            ) for key in self.class_data.keys()
        ]
    
    def get_class_grades(self) -> list[tuple[str, str, str]] | None: 
        return None if self.class_data is None else [
            (
                str(key), 
                self.class_data[key]["grade"], 
                self._letter_grade(self.class_data[key]["grade"])
            ) for key in self.class_data.keys()
        ]
    
