import pandas as pd
import pytest

from data_analysis.teacher_student_ratio import get_teacher_student_ratio


def test_with_empty_data():
    t_df = pd.DataFrame.from_dict({})
    s_df = pd.DataFrame.from_dict({})
    with pytest.raises(KeyError, match=r".*cid.*"):
        r_df = get_teacher_student_ratio(t_df, s_df)


def test_with_no_match():
    t_df = pd.DataFrame.from_dict(
        {'id': {1: '3333'}, 'fname': {1: 'Teacher1'}, 'lname': {1: 'Weekley'}, 'cid': {1: '3333'}})
    s_df = pd.DataFrame.from_dict(
        {'id': {1: 2}, 'fname': {1: 'Student1', 2: 'Student1', }, 'lname': {1: 'SL1', 2: 'SL2'},
         'cid': {1: '1111', 2: '2222'}})
    r_df = get_teacher_student_ratio(t_df, s_df, 'cid','student_cnt')
    assert r_df.student_cnt[1] == 0


def test_with_match():
    t_df = pd.DataFrame.from_dict(
        {'id': {1: '1111'}, 'fname': {1: 'Teacher1'}, 'lname': {1: 'Weekley'}, 'cid': {1: '1111'}})
    s_df = pd.DataFrame.from_dict(
        {'id': {1: 2}, 'fname': {1: 'Student1', 2: 'Student1', }, 'lname': {1: 'SL1', 2: 'SL2'},
         'cid': {1: '1111', 2: '1111'}})
    r_df = get_teacher_student_ratio(t_df, s_df, 'cid','student_cnt')
    assert r_df.student_cnt[1] == 2
