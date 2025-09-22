ID_DICT = {}
ID_CNT = 0

WEEKDAY_POINT = 1
WEEKEND_POINT = 2
TRAINED_POINT = 3
BONUS_ATTENDANCE = 10
BONUS_POINT = 10

DAY_IDX_DICT = {
    "monday":0,
    "tuesday":1,
    "wednesday":2,
    "thursday":3,
    "friday":4,
    "saturday":5,
    "sunday":6
}
WEEKEND_IDX = [5, 6]
TRAINED_DAY_IDX = 2

# dat[사용자ID][요일]
user_id_to_day = [[0] * 100 for _ in range(100)]
points = [0] * 100
grade = [0] * 100
names = [''] * 100
train_day_attendance = [0] * 100
weekend_attendance = [0] * 100

GOLD_MINIMUM = 50
SILVER_MINIMUM = 30
GOLD_GRADE = 1
SILVER_GRADE = 2
NORMAL_GRADE = 0


def is_valid_data(day_str):
    if day_str not in DAY_IDX_DICT.keys():
        print(f"{day_str} is not a valid day")
        return False
    return True

def set_basic_point(name, day_str): #함수단위로 쪼개기
    global ID_CNT
    if not is_valid_data(day_str):
        return

    set_user_id_dict(name)
    user_id = ID_DICT[name]
    day_idx = DAY_IDX_DICT[day_str]

    points[user_id] += get_basic_attendance_point(day_idx)

    set_user_attendance(user_id, day_idx)


def set_user_attendance(user_id, day_idx: int):
    user_id_to_day[user_id][day_idx] += 1
    if day_idx == TRAINED_DAY_IDX:
        train_day_attendance[user_id] += 1
    elif day_idx in WEEKEND_IDX:
        weekend_attendance[user_id] += 1

def set_user_id_dict(name):
    global ID_CNT
    if name not in ID_DICT:
        ID_CNT += 1
        ID_DICT[name] = ID_CNT
        names[ID_CNT] = name

def get_basic_attendance_point(day_idx) -> int:
    add_point = 0
    if day_idx == TRAINED_DAY_IDX:
        add_point += TRAINED_POINT
    elif day_idx in WEEKEND_IDX:
        add_point += WEEKEND_POINT
    else:
        add_point += WEEKDAY_POINT
    return add_point

def input_file():
    try:
        with open("attendance_weekday_500.txt", encoding='utf-8') as f:
            for _ in range(500):
                line = f.readline()
                if not line:
                    break
                parts = line.strip().split()
                if len(parts) == 2:
                    set_basic_point(parts[0], parts[1])

        for user_id in range(1, ID_CNT + 1):
            set_train_day_bonus_point(user_id)
            set_weekend_bonus_point(user_id)
            set_user_grade(user_id)

            print_user_point(user_id)
            print_user_grade(user_id)

        print_fail_user_names()

    except FileNotFoundError:
        print("파일을 찾을 수 없습니다.")

def print_fail_user_names():
    print("\nRemoved player")
    print("==============")
    for user_id in range(1, ID_CNT + 1):
        if is_failed_user(user_id):
            print(names[user_id])

def print_user_grade(user_id: int):
    if grade[user_id] == GOLD_GRADE:
        print("GOLD")
    elif grade[user_id] == SILVER_GRADE:
        print("SILVER")
    else:
        print("NORMAL")


def print_user_point(user_id: int):
    print(f"NAME : {names[user_id]}, POINT : {points[user_id]}, GRADE : ", end="")

def is_failed_user(user_id: int) -> bool:
    return grade[user_id] == NORMAL_GRADE and train_day_attendance[user_id] == 0 and weekend_attendance[user_id] == 0

def set_user_grade(user_id: int):
    if points[user_id] >= GOLD_MINIMUM:
        grade[user_id] = GOLD_GRADE
    elif points[user_id] >= SILVER_MINIMUM:
        grade[user_id] = SILVER_GRADE
    else:
        grade[user_id] = NORMAL_GRADE

def set_weekend_bonus_point(user_id: int):
    if user_id_to_day[user_id][WEEKEND_IDX[0]] + user_id_to_day[user_id][WEEKEND_IDX[1]] >= BONUS_ATTENDANCE:
        points[user_id] += BONUS_POINT

def set_train_day_bonus_point(user_id: int):
    if user_id_to_day[user_id][TRAINED_DAY_IDX] >= BONUS_ATTENDANCE:
        points[user_id] += BONUS_POINT


if __name__ == "__main__":
    input_file()