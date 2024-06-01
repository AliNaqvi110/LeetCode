import pandas as pd

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    df = {'student_id':[], 'age':[]}
    for i in student_data:
        df['student_id'].append(i[0])
        df['age'].append(i[1])
    return pd.DataFrame(df)