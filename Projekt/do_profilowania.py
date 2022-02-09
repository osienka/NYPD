import analiza.analizy.liczenie.liczenie as licz
import analiza.analizy.czytanie.wczytywanie as czyt

PROCPRAC = 0.75 ##Procent osób płacących podatki w tym emeryci
PROCPODAT = 17 ##Wszyscy opodatkowani wg pierwszego progu - 17%
#Procent z podatku PIT trafiający do poszczególnych jednostek samorządu terytorialnego
PROCWOJ = 1.6
PROCPOW = 10.25
PROCGMIN = 39
PROCMET = 5

gm20 = czyt.load_jst("./dane/20210215_Gminy_2_za_2020.xlsx")
woj20 = czyt.load_jst("./dane/20210211_Województwa_za_2020.xlsx")
pow20 = czyt.load_jst("./dane/20210211_Powiaty_za_2020.xlsx")
miasta20 = czyt.load_jst("./dane/20210215_Miasta_NPP_2_za_2020.xlsx")
gm19 = czyt.load_jst("./dane/20200214_Gminy_za_2019.xlsx")
woj19 = czyt.load_jst("./dane/20200214_Wojewodztwa_za_2019.xlsx")
pow19 = czyt.load_jst("./dane/20200214_Powiaty_za_2019.xlsx")
miasta19 = czyt.load_jst("./dane/20200214_Miasta_NPP_za_2019.xlsx")

woj_lud = czyt.load_lud("./dane/Tabela_II.xls")
pow_lud = czyt.load_lud("./dane/Tabela_III.xls")
gm_lud = czyt.load_lud("./dane/Tabela_IV.xls")

miasta19_lud = czyt.lacz(miasta19, pow_lud)
miasta20_lud = czyt.lacz(miasta20, pow_lud)
gm19_lud = czyt.lacz(gm19, gm_lud)
gm20_lud = czyt.lacz(gm20, gm_lud)
pow20_lud = czyt.lacz(pow20, pow_lud)
pow19_lud = czyt.lacz(pow19, pow_lud)
miasta20_doch = licz.dochod_jst(czyt.code_jst(miasta20))

pow19_war = licz.licz_war_i_sr(pow19_lud)[0]
pow19_sr = licz.licz_war_i_sr(pow19_lud)[1]
por_pow19 = licz.porownaj_przewidywany(pow20_lud, licz.licz_war_i_sr(gm20_lud)[1])
miasta19_sr_doch_opo = licz.sr_dochod_opodatkowany(miasta19_lud)["mean"]

