import pandas as pd

def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    return students[students['name'].notna()]

students = {
    'student_id': [32, 217, 779, 849],
    'name': ['Piper', None, 'Georgia', 'Willow'],
    'age': [5, 19, 20, 14]
}

dropMissingData(pd.DataFrame(students))