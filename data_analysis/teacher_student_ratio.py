import os

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sb

SEP = os.path.sep


def get_teacher_student_ratio(teachers_df, students_df, join_key='cid', cnt_col='student_cnt'):
    cnts_by_id = students_df.groupby(by=[join_key]).size().reset_index(name=cnt_col)
    teacher_student_ratio = teachers_df.join(cnts_by_id.set_index(join_key), on=join_key)
    teacher_student_ratio = teacher_student_ratio.fillna(0)
    return teacher_student_ratio


def main():
    students_csv = os.getcwd() + SEP + 'data' + SEP + 'students.csv'
    teachers_pq = os.getcwd() + SEP + 'data' + SEP + 'teachers.parquet'
    if os.path.exists(students_csv) and os.path.exists(teachers_pq):
        students_df = pd.read_csv(students_csv, delimiter='_')
        teachers_df = pd.read_parquet(teachers_pq, engine='pyarrow')
        t_s_r = get_teacher_student_ratio(teachers_df, students_df)
        t_s_r_plot = sb.barplot(x='lname', y='student_cnt', data=t_s_r[['lname', 'student_cnt']])
        plt.xlabel('Teachers')
        for bar in t_s_r_plot.patches:
            t_s_r_plot.annotate(format(bar.get_height(), '.0f'),
                                (bar.get_x() + bar.get_width() / 2,
                                 bar.get_height()), ha='center', va='center',
                                size=9, xytext=(0, 9),
                                textcoords='offset points')

        plt.show()


if __name__ == "__main__":
    main()
