# test function read_base_stats

from multi_poke_v1 import read_base_stats

def test_meltan():
    base_stats = read_base_stats("meltan")

    assert base_stats[0] == "meltan"
    assert base_stats[1] == 130
    assert base_stats[2] == 118
    assert base_stats[3] == 99
