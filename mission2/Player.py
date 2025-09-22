from config import *

class Player:
    def __init__(self, name, id_cnt):
        self.player_id = id_cnt
        self.name = name
        self.grade = 0
        self.point = 0
        self.day = [0] * MAX_DAY
        self.weekend_atd = 0
        self.train_atd = 0

    def set_attendance(self, day_idx):
        self.day[day_idx] += 1
        if day_idx == TRAINED_DAY_IDX:
            self.train_atd += 1
        elif day_idx in WEEKEND_IDX:
            self.weekend_atd += 1

    def print_info(self):
        print(f"NAME : {self.name}, POINT : {self.point}, GRADE : ", end="")

    def is_failed_player(self):
        return self.grade == NORMAL_GRADE and \
            self.train_atd == 0 and \
            self.weekend_atd == 0