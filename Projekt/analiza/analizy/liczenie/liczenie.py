import pandas as pd
import numpy as np
import collections

PROCPRAC = 0.75  ##Procent osób płacących podatki w tym emeryci
PROCPODAT = 17  ##Wszyscy opodatkowani wg pierwszego progu - 17%
# Procent z podatku PIT trafiający do poszczególnych jednostek samorządu terytorialnego
PROCWOJ = 1.6  # województwa
PROCPOW = 10  # powiaty
PROCGMIN = 39  # gminy
PROCMET = 5  # metropolia


def dochod_jst(jst: pd.DataFrame):
    """Funkcja tworzy słownik z kodami jednostek samorządu terytorialnego jako kluczem
   i dochodem jako wartością; dla miast na prawach powiatu, to suma dochodów z części
   gminnej i powiatowej
  Parametry
  ----------
  jst : pandas.DataFrame
    dataframe z danymi o jednostkach samorządu terytorialnego

  Returns
  -------
  dochody : dict
      slownik z kodem jednostki jako kluczem i wartością dochodu jako wartością (value)
  """
    if jst["code"][0] != jst["code"][1]:
        dochody = {jst["code"][i]: jst[11][i] for i in range(len(jst))}
    else:
        dochody = {jst["code"][i]: jst[11][i] + jst[11][i - 1] if jst["code"][i] == jst["code"][i - 1] else
        print("Niezgodne kody miasta dla ", jst[4][i])
                   for i in range(1, len(jst), 2)}
    return dochody


def porownaj_lata(jst1: dict, jst2: dict):
    """Funkcja przyjmuje słowniki zawierające nazwy i dochody poszczególnych jednostek i je porównuje.
    Zwraca słownik z różnicą nazwa: (jst1-jst2) dochodów.
  Parametry
  ----------
  jst1 : dict
    słownik z nazwami i wartościami dochodu jednostek samorządu terytorialnego

  jst2 : dict
    słownik z nazwami i wartościami dochodu jednostek samorządu terytorialnego

  Returns
  -------
  dochody : dict
      slownik z nazwą jednostki jako kluczem i różnicą w dochoddach jako wartością (value)
  """
    por = {key1: jst1[key1] - jst2[key1] if type(jst2[key1]) is not None else
    print("Niezgodne kody jednostek samorządu terytorialnego dla ", key1)
           for key1 in jst1}
    return por


def sr_dochod_opodatkowany(jst: pd.DataFrame):
    """Funkcja liczy średni dochód opodatkowany dla jednostek samorządu terytorialnego
  Parametry
  ----------
  jst : pandas.DataFrame
    dataframe z danymi o jednostkach samorządu terytorialnego

  Returns
  -------
  jst : pandas.DataFrame
      dataframe z dodatkową kolumną ze średnim dochodem opodatkowanym dla każdej z jednostek
  """
    # sprawdzam czy województwo
    if type(jst["1_x"][0]) == str:
        # sprawdzam czy gmina
        if type(jst["2_x"][0]) == str:
            jst["mean"] = [
                (float(jst.loc[i].iat[11]) * PROCPRAC * 10000) / (float(jst.loc[i].iat[17]) * PROCPODAT * PROCGMIN)
                for i in range(len(jst))]
        # sprawdzam czy nie miasto
        elif jst[4][0] != jst[4][1]:
            jst["mean"] = [
                (float(jst.loc[i].iat[11]) * PROCPRAC * 10000) / (float(jst.loc[i].iat[17]) * PROCPODAT * PROCPOW)
                for i in range(len(jst))]
        else:
            jst["mean"] = [(float(jst.loc[i].iat[11]) * PROCPRAC * 10000) / (
                        float(jst.loc[i].iat[17]) * PROCPODAT * PROCPOW) if i % 2
                           else (float(jst.loc[i].iat[11]) * PROCPRAC * 10000) / (
                        float(jst.loc[i].iat[17]) * PROCPODAT * PROCGMIN)
                           for i in range(len(jst[[11]]))]
    else:
        jst["mean"] = [
            (float(jst.loc[i].iat[11]) * PROCPRAC * 10000) / (float(jst.loc[i].iat[17]) * PROCPODAT * PROCWOJ)
            for i in range(len(jst))]
    return jst


def licz_war_i_sr(jst: pd.DataFrame):
    """Funkcja liczy wariancję dochodów i średnią ważoną gmin lub powiatów
  (w tym miast na prawie powiatu) dla odpowiednio powiatów lub województw,
  do których należą.
  Parametry
  ----------
  jst : pandas.DataFrame
    dataframe z danymi o podjednostkach terytorialnych

  Returns
  -------
  [war,sr] : [dict,dict]
      lista z dwoma słownikami - pierwszy zawiera wariacje dla podległych
      jednostek, drugi srednią ważoną tych jednostek
  """
    podlegle = collections.defaultdict(list)
    pod_lud = collections.defaultdict(list)
    sr = collections.defaultdict(list)
    if type(jst["2_x"][0]) == str:  # sprawdzam czy gmina
        for i in range(len(jst)):
            podlegle[jst.loc[i].iat[6]].append(jst.loc[i].iat[11])
            pod_lud[jst.loc[i].iat[6]].append(jst.loc[i].iat[17])
        war = {key: np.var(podlegle[key], ddof=0) for key in podlegle}
        # słowniki powinny być tej samej długości
        sr = {key: np.multiply(podlegle[key], pod_lud[key]) for key in podlegle}
        sr = {key: sum(sr[key]) / (sum(pod_lud[key])) for key in sr}
        return [war, sr]
    else:
        # jeśli powiat (miasto)
        if jst[4][0] != jst[4][1]:  # sprawdzam czy nie miasto
            for i in range(len(jst)):
                podlegle[jst.loc[i].iat[5]].append(jst.loc[i].iat[11])
                pod_lud[jst.loc[i].iat[5]].append(jst.loc[i].iat[17])
        else:  # miasta - tylko część powiatowa liczona z myślą o województwach
            # poniważ miasta same w sobie mają część gminną
            for i in range(0, len(jst), 2):
                podlegle[jst.loc[i].iat[5]].append(jst.loc[i].iat[11])
                pod_lud[jst.loc[i].iat[5]].append(jst.loc[i].iat[17])
        war = {key: np.var(podlegle[key], ddof=0) for key in podlegle}
        # słowniki powinny być tej samej długości
        sr = {key: np.multiply(podlegle[key], pod_lud[key]) for key in podlegle}
        sr = {key: sum(sr[key]) / (sum(pod_lud[key])) for key in sr}
        return [war, sr]


def porownaj_przewidywany(jst: pd.DataFrame, sr: dict):
    """Funkcja liczy wariancję dochodów i średnią ważoną gmin lub powiatów (w tym miast na prawie powiatu)
  dla odpowiednio powiatów lub województw, do których należą.
  Parametry
  ----------
  jst : pandas.DataFrame
    dataframe z danymi o podjednostkach terytorialnych

  sr: dict
    słownik z nazwami jednostek i średnią ważoną podległych im jednostek

  Returns
  -------
  por: dict
      słownik w postaci nazwa: różnica między spodziewanym dochodem, a średnią
      ważoną jednostek podległych
  """
    por = collections.defaultdict(float)
    por = {key: jst[11][i]-sr[key] for key in sr for i in range(len(jst)) if jst[4][i] == key}
    return por
