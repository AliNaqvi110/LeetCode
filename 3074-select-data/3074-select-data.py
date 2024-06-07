import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    data = students[students['student_id'] == 101].drop('student_id', axis=1)
    return data
    