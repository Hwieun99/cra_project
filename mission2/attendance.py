from Player import Player
from config import *
from Calculator import PointCalculator, DefaultGradeCalculator, TrainPointCalculator, WeekendPointCalculator, \
    SilverGradeCalculator
from Calculator import GoldGradeCalculator

class Manager:
    def __init__(self):
        self.id_cnt = 0
        self.lst = {}
        self.name_dict = {}

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

        self.lst[player_id].point += PointCalculator().get_point(day_idx)
        self.lst[player_id].set_attendance(day_idx)

    def set_player_grade(self, player_id):
        player = self.lst[player_id]
        if player.point >= GOLD_MINIMUM:
            g_cal = GoldGradeCalculator()
        elif player.point >= SILVER_MINIMUM:
            g_cal = SilverGradeCalculator()
        else:
            g_cal = DefaultGradeCalculator()
        player.grade = g_cal.get_grade()

    def set_player_bonus_point(self, player_id):
        player = self.lst[player_id]
        self.lst[player_id].point += TrainPointCalculator().get_point(player)
        self.lst[player_id].point += WeekendPointCalculator().get_point(player)

    def print_player_point(self, player_id: int):
        player = self.lst[player_id]
        player.print_info()

    def print_player_grade(self, player_id: int):
        player = self.lst[player_id]
        g_cal = DefaultGradeCalculator()
        if player.grade == GOLD_GRADE:
            g_cal = GoldGradeCalculator()
        elif player.grade == SILVER_GRADE:
            g_cal = SilverGradeCalculator()
        g_cal.print_grade()

    def is_valid_data(self, day_str):
        if day_str not in day_str_to_idx.keys():
            print(f"{day_str} is not a valid day")
            return False
        return True

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
                manager.set_player_basic_point(name, day_str)

        for player_id in range(1, manager.id_cnt + 1):
            manager.set_player_bonus_point(player_id)
            manager.set_player_grade(player_id)

            manager.print_player_point(player_id)
            manager.print_player_grade(player_id)

        manager.print_fail_player_names()

    except FileNotFoundError:
        print("파일을 찾을 수 없습니다.")



if __name__ == "__main__":
    input_file()