from Player import Player
from config import *
from PointCalculator import PointCalculator

class Manager:
    def __init__(self):
        self.id_cnt = 0
        self.lst = {}
        self.name_dict = {}
        self.p_calc = PointCalculator()

    def add_player(self, name):
        self.lst[self.id_cnt] = Player(name, self.id_cnt)
        self.name_dict[name] = self.id_cnt

    def print_fail_player_names(self):
        print("\nRemoved player")
        print("==============")
        for player_id in range(1, self.id_cnt + 1):
            if self.lst[player_id].is_failed_player():
                print(self.lst[player_id].name)

    def set_player_basic_point(self, name, day_str):
        if not self.is_valid_data(day_str):
            return
        if name not in self.name_dict:
            self.id_cnt += 1
            self.add_player(name)
        player_id = self.name_dict[name]
        day_idx = day_str_to_idx[day_str]

        self.lst[player_id].point += self.p_calc.get_basic_attendance_point(day_idx)
        self.lst[player_id].set_attendance(day_idx)

    def set_player_grade(self, player_id):
        player = self.lst[player_id]
        grade = GradeCalc().get_grade(player.point)
        player.grade = grade

    def set_player_bonus_point(self, player_id):
        player = self.lst[player_id]
        point = self.p_calc.get_bonus_point()

    def print_player_point(self, player_id: int):
        player = self.lst[player_id]
        print(f"NAME : {player.name}, POINT : {player.point}, GRADE : ", end="")

    def print_player_grade(self, player_id: int):
        player = self.lst[player_id]
        if player.grade == GOLD_GRADE:
            print("GOLD")
        elif player.grade == SILVER_GRADE:
            print("SILVER")
        else:
            print("NORMAL")

    def is_valid_data(self, day_str):
        if day_str not in day_str_to_idx.keys():
            print(f"{day_str} is not a valid day")
            return False
        return True