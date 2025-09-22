from Manager import Manager

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