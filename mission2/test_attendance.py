import pytest

from attendance import weekend_attendance, set_user_attendance, user_id_to_day, is_valid_data, \
    set_user_id_dict, names, ID_DICT, get_basic_attendance_point, WEEKEND_IDX, WEEKEND_POINT, TRAINED_POINT, \
    TRAINED_DAY_IDX, is_failed_user, NORMAL_GRADE, grade, set_user_grade, points, set_weekend_bonus_point, BONUS_POINT, \
    set_train_day_bonus_point, set_basic_point, input_file
from attendance import train_day_attendance
from mission2.attendance import GOLD_GRADE, SILVER_GRADE, GOLD_MINIMUM, SILVER_MINIMUM


@pytest.fixture
def shared_data():
    return ID_DICT, names

@pytest.fixture
def shared_attendance():
    return user_id_to_day, train_day_attendance, weekend_attendance

@pytest.fixture
def shared_grade():
    return points, grade

@pytest.mark.parametrize("day, result", [
    ('monday', True),
    ('monkey', False),
    ('banana', False),
    ('wednesday', True)
])
def test_is_valid_data(day, result):
    assert is_valid_data(day) == result

def test_set_user_id_dict(shared_data): # 다시
    name_list = ['Alex', 'Cameron', 'Andre']
    for idx, name in enumerate(name_list):
        set_user_id_dict(name)
        assert shared_data[0][name] == idx+1
        assert shared_data[1][idx+1] == name

def test_set_user_attendance(shared_attendance):
    set_user_attendance(0, 1)
    set_user_attendance(0, 1)
    set_user_attendance(0, 2)
    set_user_attendance(0, 5)
    set_user_attendance(0, 6)
    assert shared_attendance[0][0][1] == 2
    assert shared_attendance[0][0][2] == 1
    assert shared_attendance[0][0][3] == 0
    assert shared_attendance[1][0] == 1
    assert shared_attendance[2][0] == 2

def test_get_basic_attendance_point():
    point = get_basic_attendance_point(1)
    assert point == 1
    point = get_basic_attendance_point(TRAINED_DAY_IDX)
    assert point == TRAINED_POINT
    point = get_basic_attendance_point(5)
    assert point == WEEKEND_POINT

def test_is_failed_user():
    grade[0] = NORMAL_GRADE
    train_day_attendance[0] = 0
    weekend_attendance[0] = 0
    grade[1] = GOLD_GRADE
    train_day_attendance[1] = 1
    weekend_attendance[1] = 1
    assert is_failed_user(0) == True
    assert is_failed_user(1) == False


def test_set_user_grade(shared_grade):
    points = shared_grade[0]
    points[0] = GOLD_MINIMUM
    points[1] = SILVER_MINIMUM
    points[2] = 1
    set_user_grade(0)
    set_user_grade(1)
    set_user_grade(2)
    assert shared_grade[1][0] == GOLD_GRADE
    assert shared_grade[1][1] == SILVER_GRADE
    assert shared_grade[1][2] == NORMAL_GRADE

def test_set_weekend_bonus_point(shared_attendance, shared_grade):
    user_id_to_day = shared_attendance[0]
    user_id_to_day[0][5] = 4
    user_id_to_day[0][6] = 6
    set_weekend_bonus_point(0)
    assert shared_grade[0][0] == BONUS_POINT


def test_set_train_day_bonus_point(shared_attendance, shared_grade):
    user_id_to_day = shared_attendance[0]
    user_id_to_day[0][TRAINED_DAY_IDX] = 12
    user_id_to_day[1][TRAINED_DAY_IDX] = 1
    set_train_day_bonus_point(0)
    assert shared_grade[0][0] == BONUS_POINT
    assert shared_grade[0][1] == 0

def test_set_basic_point(shared_grade, capsys):
    set_basic_point("Alex", "wednesday")
    assert shared_grade[0][1] == TRAINED_POINT

    set_basic_point("Alex", "monkey")
    output = capsys.readouterr()
    assert output.out == 'monkey is not a valid day\n'

def test_input_file():
    input_file()
