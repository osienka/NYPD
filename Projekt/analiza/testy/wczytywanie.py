import pandas as pd

import analiza.analizy.czytanie.wczytywanie as czyt
from pandas._testing import assert_frame_equal

gm20 = pd.DataFrame([['02', '01', '01', '1', 'BOLESŁAWIEC', 'dolnośląskie',
                      'bolesławiecki', 756, 75621, 10, 40456699, 40456699, None, None],
                     ['02', '01', '02', '2', 'BOLESŁAWIEC', 'dolnośląskie',
                      'bolesławiecki', 756, 75621, 10, 13789712, 13789712, None, None],
                     ['02', '01', '03', '2', 'GROMADKA', 'dolnośląskie',
                      'bolesławiecki', 756, 75621, 10, 3573540, 3573540, None, None],
                     ['02', '01', '04', '3', 'NOWOGRODZIEC', 'dolnośląskie',
                      'bolesławiecki', 756, 75621, 10, 9553744, 9553744, None, None],
                     ['02', '01', '05', '2', 'OSIECZNICA', 'dolnośląskie',
                      'bolesławiecki', 756, 75621, 10, 5844560, 5844560, None, None],
                     ['02', '01', '06', '2', 'WARTA BOLESŁAWIECKA', 'dolnośląskie',
                      'bolesławiecki', 756, 75621, 10, 5992663, 5992663, None, None]])
lud = pd.DataFrame([['M.Bolesławiec', '0201011', 38486],
                    ['G.Bolesławiec', '0201022', 14863],
                    ['G.Gromadka', '0201032', 5317],
                    ['M-W.Nowogrodziec', '0201043', 15229],
                    ['M.Nowogrodziec', '0201044', 4263],
                    ['G.Nowogrodziec', '0201045', 10966]])


def test_code_jst():
    result = pd.DataFrame([['02', '01', '01', '1', 'BOLESŁAWIEC', 'dolnośląskie',
                            'bolesławiecki', 756, 75621, 10, 40456699, 40456699, None, None,
                            '0201011'],
                           ['02', '01', '02', '2', 'BOLESŁAWIEC', 'dolnośląskie',
                            'bolesławiecki', 756, 75621, 10, 13789712, 13789712, None, None,
                            '0201022'],
                           ['02', '01', '03', '2', 'GROMADKA', 'dolnośląskie',
                            'bolesławiecki', 756, 75621, 10, 3573540, 3573540, None, None,
                            '0201032'],
                           ['02', '01', '04', '3', 'NOWOGRODZIEC', 'dolnośląskie',
                            'bolesławiecki', 756, 75621, 10, 9553744, 9553744, None, None,
                            '0201043'],
                           ['02', '01', '05', '2', 'OSIECZNICA', 'dolnośląskie',
                            'bolesławiecki', 756, 75621, 10, 5844560, 5844560, None, None,
                            '0201052'],
                           ['02', '01', '06', '2', 'WARTA BOLESŁAWIECKA', 'dolnośląskie',
                            'bolesławiecki', 756, 75621, 10, 5992663, 5992663, None, None,
                            '0201062']])
    result.columns = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 'code']
    assert_frame_equal(czyt.code_jst(gm20), result)


def test_lacz():
    result = pd.DataFrame([['02', '01', '01', '1', 'BOLESŁAWIEC', 'dolnośląskie',
                            'bolesławiecki', 756, 75621, 10, 40456699, 40456699, None, None,
                            '0201011', 'M.Bolesławiec', '0201011', 38486],
                           ['02', '01', '02', '2', 'BOLESŁAWIEC', 'dolnośląskie',
                            'bolesławiecki', 756, 75621, 10, 13789712, 13789712, None, None,
                            '0201022', 'G.Bolesławiec', '0201022', 14863],
                           ['02', '01', '03', '2', 'GROMADKA', 'dolnośląskie',
                            'bolesławiecki', 756, 75621, 10, 3573540, 3573540, None, None,
                            '0201032', 'G.Gromadka', '0201032', 5317],
                           ['02', '01', '04', '3', 'NOWOGRODZIEC', 'dolnośląskie',
                            'bolesławiecki', 756, 75621, 10, 9553744, 9553744, None, None,
                            '0201043', 'M-W.Nowogrodziec', '0201043', 15229]])
    result.columns = ['0_x', '1_x', '2_x', 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 'code', '0_y', '1_y', '2_y']
    assert_frame_equal(czyt.lacz(gm20, lud), result)
