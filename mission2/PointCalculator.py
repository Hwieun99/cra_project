from config import *
class PointCalculator:
    @classmethod
    def get_basic_attendance_point(self, day_idx) -> int:
        if day_idx == TRAINED_DAY_IDX:
            return TRAINED_POINT
        elif day_idx in WEEKEND_IDX:
            return WEEKEND_POINT
        return WEEKDAY_POINT


    # @classmethod
    # def set_train_day_bonus_point(self, manager, player_id: int):
    #     if manager.lst[player_id].day[TRAINED_DAY_IDX] >= BONUS_ATTENDANCE:
    #         manager.lst[player_id].point += BONUS_POINT
    #
    # @classmethod
    # def set_weekend_bonus_point(self, manager, player_id: int):
    #     if manager.lst[player_id].day[WEEKEND_IDX[0]] + manager.lst[player_id].day[WEEKEND_IDX[1]] >= BONUS_ATTENDANCE:
    #         manager.lst[player_id].point += BONUS_POINT
    def get_bonus_point(self, manager, player_id):

        pass
