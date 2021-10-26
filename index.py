import psycopg2
import pandas as pd
from sqlalchemy import create_engine

def type_pop(tablename):
    # read source (postgres db table)
    q = f"SELECT table_name, column_name, data_type FROM information_schema.columns WHERE table_name = '{tablename}';"
    dbstr = pd.read_sql(q, eng)

    # read target (csv schema)
    csv = pd.read_csv(p)
    tabledf = csv[csv.Table==f"{tablename}"].copy()

    # create field:type dictionary
    typedict = dbstr.iloc[:,1:3].set_index('column_name').to_dict()
    typed = typedict['data_type']

    tabledf.Type = tabledf.Field.apply(lambda x: typed[x] if x in [i for i in typed.keys()] else pd.NA )
    return tabledf


def accum():
    store = {}
    comp = pd.read_csv(p)
    for i in [str(i) for i in comp.Table.unique() if (str(i).startswith('data')) or (str(i).startswith('geo') and not str(i).endswith('\xa0'))]:
        store[i] = type_pop(i)

    return pd.concat([j for i,j in store.items()], ignore_index=True)
