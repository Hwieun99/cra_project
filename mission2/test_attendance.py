import pytest
from config import *
from attendance import Manager, input_file
def test_manager():
    manager = Manager()
    assert manager.id_cnt == 0
    assert manager.player_list == {}
    assert manager.name_dict == {}

def test_add_player():
    manager = Manager()
    manager.add_player('Alex')
    assert manager.name_dict['Alex'] == manager.id_cnt

def test_print_fail_player_nams(capsys):
    manager = Manager()
    manager.set_player_basic_point('Alex', 'monday')
    manager.print_fail_player_names()
    output = capsys.readouterr()
    assert output.out == '\nRemoved player\n==============\nAlex\n'

def test_set_player_basic_point():
    manager = Manager()
    manager.set_player_basic_point('Alex', 'monday')
    assert manager.id_cnt == 1
    assert manager.player_list[manager.id_cnt].name == 'Alex'
    assert manager.name_dict['Alex'] == manager.id_cnt

def test_set_player_grade():
    manager = Manager()
    manager.set_player_basic_point('Alex', 'monday')
    manager.set_player_grade(1)
    player = manager.player_list[1]
    assert player.grade == NORMAL_GRADE

    manager.player_list[1].point = GOLD_MINIMUM
    manager.set_player_grade(1)
    assert player.grade == GOLD_GRADE

    manager.player_list[1].point = SILVER_MINIMUM
    manager.set_player_grade(1)
    assert player.grade == SILVER_GRADE

def test_set_player_bonus_point_fail():
    manager = Manager()
    manager.set_player_basic_point('Alex', 'monday')
    manager.set_player_bonus_point(1)
    assert manager.player_list[1].point == 1

def test_set_player_bonus_point_success():
    manager = Manager()
    for i in range(10):
        manager.set_player_basic_point('Alex', 'wednesday')
    manager.set_player_bonus_point(1)
    assert manager.player_list[1].point == 40

def test_set_player_weekend_bonus_point_success():
    manager = Manager()
    for i in range(10):
        manager.set_player_basic_point('Alex', 'sunday')
    manager.set_player_bonus_point(1)
    assert manager.player_list[1].point == 30

def test_print_player_point(capsys):
    manager = Manager()
    manager.set_player_basic_point('Alex', 'monday')
    manager.print_player_point(1)
    output = capsys.readouterr()
    assert output.out == 'NAME : Alex, POINT : 1, GRADE : '

def test_print_player_grade(capsys):
    manager = Manager()
    manager.set_player_basic_point('Alex', 'monday')
    manager.print_player_grade(1)
    output = capsys.readouterr()
    assert output.out == 'NORMAL\n'

    manager.player_list[1].grade = GOLD_GRADE
    manager.print_player_grade(1)
    output = capsys.readouterr()
    assert output.out == 'GOLD\n'
    #
    manager.player_list[1].grade = SILVER_GRADE
    manager.print_player_grade(1)
    output = capsys.readouterr()
    assert output.out == 'SILVER\n'

def test_is_valid_data(capsys):
    manager = Manager()
    manager.set_player_basic_point('Alex', 'monkey')
    assert capsys.readouterr().out == 'monkey is not a valid day\n'

def test_input_file(capsys):
    input_file()
    output = capsys.readouterr()
    assert output.out == '파일을 찾을 수 없습니다.\n'
