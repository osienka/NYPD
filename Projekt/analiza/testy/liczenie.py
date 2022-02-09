import pandas as pd

import analiza.analizy.liczenie.liczenie as licz
import analiza.analizy.czytanie.wczytywanie as czyt

pow19_lud = pd.DataFrame([['02', '01', None, None, 'bolesławiecki', 'dolnośląskie', None,
                           756, 75622, 10, 21984822, 21981364, 3458, 3458, '0201',
                           'bolesławiecki', '0201', 89762],
                          ['02', '02', None, None, 'dzierżoniowski', 'dolnośląskie', None,
                           756, 75622, 10, 21906718, 21903272, 3446, 3446, '0202',
                           'dzierżoniowski', '0202', 99935],
                          ['02', '03', None, None, 'głogowski', 'dolnośląskie', None, 756,
                           75622, 10, 30347660, 30342887, 4773, 4773, '0203',
                           'głogowski', '0203', 88447],
                          ['02', '04', None, None, 'górowski', 'dolnośląskie', None, 756,
                           75622, 10, 5784270, 5783360, 910, 910, '0204',
                           'górowski', '0204', 34552],
                          ['02', '05', None, None, 'jaworski', 'dolnośląskie', None, 756,
                           75622, 10, 10550026, 10548367, 1659, 1659, '0205',
                           'jaworski', '0205', 49734],
                          ['02', '06', None, None, 'jeleniogórski', 'dolnośląskie', None,
                           756, 75622, 10, 15627843, 15625385, 2458, 2458, '0206',
                           'jeleniogórski', '0206', 63333]])

pow19_lud.columns = ['0_x', '1_x', '2_x', 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 'code', '0_y', '1_y', '2_y']
pow20_lud = pd.DataFrame([['02', '01', None, None, 'bolesławiecki', 'dolnośląskie', None,
                           756, 75622, 10, 21276533, 21276533, None, None, '0201',
                           'bolesławiecki', '0201', 89762],
                          ['02', '02', None, None, 'dzierżoniowski', 'dolnośląskie', None,
                           756, 75622, 10, 21328692, 21328692, None, None, '0202',
                           'dzierżoniowski', '0202', 99935],
                          ['02', '03', None, None, 'głogowski', 'dolnośląskie', None, 756,
                           75622, 10, 28916309, 28916309, None, None, '0203',
                           'głogowski', '0203', 88447],
                          ['02', '04', None, None, 'górowski', 'dolnośląskie', None, 756,
                           75622, 10, 5682116, 5682116, None, None, '0204',
                           'górowski', '0204', 34552],
                          ['02', '05', None, None, 'jaworski', 'dolnośląskie', None, 756,
                           75622, 10, 10450783, 10450783, None, None, '0205',
                           'jaworski', '0205', 49734],
                          ['02', '06', None, None, 'karkonoski (jeleniogórski)',
                           'dolnośląskie', None, 756, 75622, 10, 15444321, 15444321, None,
                           None, '0206', 'jeleniogórski', '0206', 63333]])
pow20_lud.columns = ['0_x', '1_x', '2_x', 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 'code', '0_y', '1_y', '2_y']

gm20_lud = pd.DataFrame([['02', '01', '01', '1', 'BOLESŁAWIEC', 'dolnośląskie',
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
                          '0201043', 'M-W.Nowogrodziec', '0201043', 15229],
                         ['02', '01', '05', '2', 'OSIECZNICA', 'dolnośląskie',
                          'bolesławiecki', 756, 75621, 10, 5844560, 5844560, None, None,
                          '0201052', 'G.Osiecznica', '0201052', 7288],
                         ['02', '01', '06', '2', 'WARTA BOLESŁAWIECKA', 'dolnośląskie',
                          'bolesławiecki', 756, 75621, 10, 5992663, 5992663, None, None,
                          '0201062', 'G.Warta Bolesławiecka', '0201062', 8579]])

gm20_lud.columns = ['0_x', '1_x', '2_x', 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 'code', '0_y', '1_y', '2_y']


def test_dochod_jst():
    result = {"0201011": 40456699, "0201022": 13789712, "0201032": 3573540, "0201043": 9553744, "0201052": 5844560,
              "0201062": 5992663}
    assert licz.dochod_jst(gm20_lud) == result


def test_porownaj_lata():
    result = {'0201': -704831, '0202': -574580, '0203': -1426578, '0204': -101244, '0205': -97584, '0206': -181064}
    assert licz.porownaj_lata(licz.dochod_jst(pow20_lud), pow19_lud) == result


def test_sr_dochod_opodatkowany():
    result = [9522.118766, 8573.770598, 13133.636840, 6606.358810, 8441.520770, 9796.343669]
    assert licz.sr_dochod_opodatkowany(pow20_lud)["mean"] == result


def test_licz_war_i_sr():
    result = [{'dolnośląskie': 3916679.000884527}, {'dolnośląskie': 9727.71308018942}]
    assert licz.licz_war_i_sr(licz.sr_dochod_opodatkowany(pow20_lud)) == result


def test_porownaj_przewidywany():
    por = licz.por_przewidywany(licz.sr_dochod_opodatkowany(pow20_lud),
                                licz.licz_war_i_sr(licz.sr_dochod_opodatkowany(gm20_lud))[1])
    assert por == {'bolesławiecki': 205.09855677296764}
