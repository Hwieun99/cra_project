from Player import Player
from config import *
class Manager:
    def __init__(self):
        self.lst = {}

    def add_player(self, name, id_cnt:int):
        self.lst[id_cnt] = Player(name, id_cnt)

    def print_fail_player_names(self, id_cnt):
        print("\nRemoved player")
        print("==============")
        for player_id in range(1, id_cnt + 1):
            if self.lst[player_id].is_failed_player():
                print(self.lst[player_id].name)

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

