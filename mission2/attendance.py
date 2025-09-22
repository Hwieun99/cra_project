from config import *
from Manager import Manager
name_dict = {}
ID_CNT = 0

class PointCalculator:
    @classmethod
    def get_basic_attendance_point(self, day_idx) -> int:
        if day_idx == TRAINED_DAY_IDX:
            return TRAINED_POINT
        elif day_idx in WEEKEND_IDX:
            return WEEKEND_POINT
        return WEEKDAY_POINT

    @classmethod
    def set_train_day_bonus_point(self, manager, player_id: int):
        if manager.lst[player_id].day[TRAINED_DAY_IDX] >= BONUS_ATTENDANCE:
            manager.lst[player_id].point += BONUS_POINT

    @classmethod
    def set_weekend_bonus_point(self, manager, player_id: int):
        if manager.lst[player_id].day[WEEKEND_IDX[0]] + manager.lst[player_id].day[WEEKEND_IDX[1]] >= BONUS_ATTENDANCE:
            manager.lst[player_id].point += BONUS_POINT

def is_valid_data(day_str):
    if day_str not in DAY_IDX_DICT.keys():
        print(f"{day_str} is not a valid day")
        return False
    return True

def set_basic_point(manager, name, day_str): #함수단위로 쪼개기
    if not is_valid_data(day_str):
        return

    set_user_id_dict(manager, name)
    player_id = name_dict[name]
    day_idx = DAY_IDX_DICT[day_str]

    manager.lst[player_id].point += PointCalculator.get_basic_attendance_point(day_idx)
    manager.lst[player_id].set_attendance(day_idx)

def set_player_attendance(manager, id, day_idx: int):
    manager.lst[id].day[day_idx] += 1
    if day_idx == TRAINED_DAY_IDX:
        manager.lst[id].train_atd += 1
    elif day_idx in WEEKEND_IDX:
        manager.lst[id].weekend_atd += 1

def set_user_id_dict(manager, name):
    global ID_CNT
    if name not in name_dict:
        ID_CNT += 1
        manager.add_player(name, ID_CNT)
        name_dict[name] = ID_CNT

def input_file():
    try:
        manager = Manager()
        with open("attendance_weekday_500.txt", encoding='utf-8') as f:
            for _ in range(500):
                line = f.readline()
                if not line: break
                parts = line.strip().split()
                if len(parts) != 2: continue
                name, day_str = parts
                set_basic_point(manager, name, day_str)

        for player_id in range(1, ID_CNT + 1):
            PointCalculator.set_train_day_bonus_point(manager, player_id)
            PointCalculator.set_weekend_bonus_point(manager, player_id)
            set_user_grade(manager, player_id)

            manager.print_player_point(player_id)
            manager.print_player_grade(player_id)

        manager.print_fail_player_names(ID_CNT)

    except FileNotFoundError:
        print("파일을 찾을 수 없습니다.")


def print_user_point(manager, player_id: int):
    print(f"NAME : {manager.lst[player_id].name}, POINT : {manager.lst[player_id].point}, GRADE : ", end="")


def set_user_grade(manager, player_id: int):
    if manager.lst[player_id].point >= GOLD_MINIMUM:
        manager.lst[player_id].grade = GOLD_GRADE
    elif manager.lst[player_id].point >= SILVER_MINIMUM:
        manager.lst[player_id].grade = SILVER_GRADE
    else:
        manager.lst[player_id].grade = NORMAL_GRADE


if __name__ == "__main__":
    input_file()