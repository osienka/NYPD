import pandas as pd
import os


def load_jst(fileDir: str):
    """Funkcja wczytuje plik excelowy z podanej w formie napisu ścieżki
  Parametry
  ----------
  fileDir : str
    ścieżka do pliku

  Returns
  -------
  data : pandas.DataFrame
      dataframe z danymi z pliku
  """
    if not os.path.exists(fileDir):
        raise FileExistsError(f"File '{fileDir}' doesn't exist")
    data = pd.read_excel(fileDir, usecols=[i for i in range(14)], skiprows=[0, 1, 2, 3, 4, 5, 6], header=None,
                         na_values=["NaN", '-'],
                         converters={0: str, 1: str, 2: str, 3: str, 4: str, 5: str, 6: str})
    data.dropna(how="all", inplace=True)
    data = data.where(pd.notnull(data), None)
    return data


def load_lud(fileDir: str):
    """Funkcja wczytuje plik excelowy z podanej w formie napisu ścieżki
  Parametry
  ----------
  fileDir : str
    ścieżka do pliku

  Returns
  -------
  data : pandas.DataFrame
      dataframe z danymi z pliku
  """
    if not os.path.exists(fileDir):
        raise FileExistsError(f"File '{fileDir}' doesn't exist")
    data = pd.read_excel(fileDir, usecols=[0, 1, 2], skiprows=[0, 1, 2, 3, 4, 5, 6, 7], header=None,
                         converters={0: str, 1: str})
    data.dropna(how="all", inplace=True)
    return data


def code_jst(jst: pd.DataFrame):
    """Funkcja tworzy pojedynczą kolumnę z kodem jednostki
  Parametry
  ----------
  jst : pandas.DataFrame
    dataframe z danymi o jednostkach samorządu terytorialnego

  Returns
  -------
  tabela : pandas.DataFrame
      dataframe z dodatkową kolumną z kodem jednostki
  """
    if jst[2][0] is not None:  # sprawdzam czy gmina czy powiat - miasto jak powiat
        jst['code'] = jst.apply(lambda row: str(str(row[0]) + str(row[1]) + str(row[2]) + str(row[3])), axis=1)
    else:
        jst['code'] = jst.apply(lambda row: str(str(row[0]) + str(row[1])), axis=1)
    return jst


def lacz(jst: pd.DataFrame, lud: pd.DataFrame):
    """Funkcja łączy dwa dataframy w jeden za pomocą kolumny "code" z kodami
  jednostek samorządu terytorialnego; miasta łączy się z powiatami; województwa na podstawie nazw
  Parametry
  ----------
  jst : pandas.DataFrame
    dataframe z danymi o jednostkach samorządu terytorialnego

  lud : pandas.DataFrame
    dataframe z danymi o ludności w jednostkach samorządu terytorialnego

  Returns
  -------
  tabela : pandas.DataFrame
      połączona tabela z danymi
  """
    if jst[1][1] is not None:
        lud["code"] = lud[[1]]
        jst = code_jst(jst)
        tabela = pd.merge(left=jst, right=lud, on=["code"], how="inner")
    else:
        lud["nazwa"] = [lud[0][i].lower() if i < 16 else i for i in range(len(lud))]
        jst["nazwa"] = jst[[4]]
        tabela = pd.merge(left=jst, right=lud, on=["nazwa"], how="inner")
    return tabela
