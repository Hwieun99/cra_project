from config import *
from abc import ABC, abstractmethod
class Calculator:
    @abstractmethod
    def get_point(self, player):
        ...
    @abstractmethod
    def get_grade(self):
        ...
    @abstractmethod
    def print_grade(self):
        ...

class PointCalculator(Calculator):
    @classmethod
    def get_point(self, day_idx) -> int:
        if day_idx == TRAINED_DAY_IDX:
            return TRAINED_POINT
        elif day_idx in WEEKEND_IDX:
            return WEEKEND_POINT
        return WEEKDAY_POINT

class TrainPointCalculator(Calculator):
    def get_point(self, player):
        if player.day[TRAINED_DAY_IDX] >= BONUS_ATTENDANCE:
            return BONUS_POINT
        return 0

class WeekendPointCalculator(Calculator):
    def get_point(self, player):
        if player.day[WEEKEND_IDX[0]] + player.day[WEEKEND_IDX[1]] >= BONUS_ATTENDANCE:
            return BONUS_POINT
        return 0

class GoldGradeCalculator(Calculator):
    def print_grade(self):
        print("GOLD")
    def get_grade(self):
        return GOLD_GRADE

class SilverGradeCalculator(Calculator):
    def print_grade(self):
        print("SILVER")
    def get_grade(self):
        return SILVER_GRADE

class DefaultGradeCalculator(Calculator):
    def print_grade(self):
        print("NORMAL")
    def get_grade(self):
        return NORMAL_GRADE