import pandas as pd
from datetime import datetime


treino = pd.read_csv("data/treino.csv",parse_dates=True,index_col="index")

test = pd.read_csv("data/teste.csv",parse_dates=True,index_col="index")


print(treino["falha"].unique())



erros = pd.read_csv("data/erros.csv",parse_dates=True,)
'''

erros["data"] = erros["data"].apply(lambda x: datetime.strptime(x, '%Y-%m-%d %H:%M:%S'))

print(erros["data"].describe())

erros["time"] =  erros["data"].apply(lambda x: x.time())

erros["data"] =  erros["data"].apply(lambda x: x.date())
'''

print(treino["falha"].unique())


info_uso = pd.read_csv("data/info_uso.csv",parse_dates=True)

maquinas = pd.read_csv("data/maquinas.csv",parse_dates=True)


# Merge df

merge_err_maqu = pd.merge(erros, maquinas, on='maquina')

merge_err_maqu_info = pd.merge(merge_err_maqu, info_uso, on=['maquina','data'])
