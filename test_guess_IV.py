# test function guess_IV

from multi_poke_v1 import guess_IV, narrow_IV, read_stardust, read_base_stats,\
    read_cp_mult, narrow_cp_mult

def run_functions(entry):
    dic_cp_mult = read_cp_mult()
    dic_stardust = read_stardust()
    base_stats = read_base_stats()
    d_list_levels, cp_mult = narrow_cp_mult(dic_cp_mult, dic_stardust, entry)
    stam_IV, atk_IV, def_IV, is_single, two_stats = narrow_IV(entry)
    for poke in base_stats:
        if poke[0] == entry[1]:
            t_base_stats = poke[1:]
    IV = guess_IV(cp_mult, stam_IV, atk_IV, def_IV, t_base_stats, entry, d_list_levels, is_single,
             two_stats)
    return IV

def test_meltan_3():
    entry = ['3', 'meltan', 362, 64, 1600, 'above average', 'attack', 'noticeably']
    IV = run_functions(entry)

    #IV: [[i_lvl, i_stam, j_atk, k_def, IV_percent]]

    assert len(IV) == 1
    i_lvl, i_stam, j_atk, k_def, IV_percent = IV[0]
    assert i_lvl == 13.0
    assert i_stam == 4
    assert j_atk == 12
    assert k_def == 9

if __name__ == "__main__":
    test_meltan_3()