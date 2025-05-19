from sqlalchemy import create_engine
from sqlalchemy.sql import text
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.colors import LogNorm


def postgres_session():
    """
    __copyright__ = "© Ludwig Hülk"
    __license__ = "GNU Affero General Public License Version 3 (AGPL-3.0)"
    __url__ = "https://www.gnu.org/licenses/agpl-3.0.en.html"
    __author__ = "Ludee;"
    __version__ = "v0.0.1"

    SQLAlchemy session object with valid connection to local database
    Inputs
    -------
    port : int
        Database port
    password : str
        Database password
    Returns
    -------
    con : connection
        SQLAlchemy connection object.
    """

    print('new_connection_to_PostgreSQL (check/change password in def or settings doc)')
    host = 'localhost'  # input('host (default 127.0.0.1): ')
    port = int(5432)  # port = '5435'
    database = 'sonnja_db'  # input("database name (default 'sonnja_db'): ")
    user = 'sonnja'  # input('user (default postgres): ')
    password = 'sonnja'
    # password = getpass.getpass(prompt='password: ',
    #                            stream=sys.stderr)
    con = create_engine(
        'postgresql://' + '%s:%s@%s:%s/%s' % (user,
                                              password,
                                              host,
                                              port,
                                              database)).connect()
    print('Password correct! Database connection established.')
    return con

def query_database(con, schema_name, table_name):
    '''
    __copyright__ = "© Ludwig Hülk"
    __license__ = "GNU Affero General Public License Version 3 (AGPL-3.0)"
    __url__ = "https://www.gnu.org/licenses/agpl-3.0.en.html"
    __author__ = "Ludee;"
    __version__ = "v0.0.1"
    '''
    sql_query = text(f"""
            SELECT  *
            FROM    {schema_name}.{table_name}
            """)
    df = pd.read_sql_query(sql_query, con)
    #df = df.set_index('timestamp')
    print(f'Query database {schema_name}.{table_name}')
    con.close()

    return df

def compact_df(df_l_vs_c_raw):  # hier summiere ich einfach immer 2 Spalten zusammen und berechne, wie viel es insgesamt gibt von der Leistungsklasse
    compact_df_l_vs_c_list = {}
    for i in range(1, len(df_l_vs_c_raw.columns) - 1, 2):  # Start bei Spalte 1, in 2er-Schritten gehen
        col_num = 9+i
        col_name = f"count_sum_{col_num}"
        compact_df_l_vs_c_list[col_name] = df_l_vs_c_raw.iloc[:, i] + df_l_vs_c_raw.iloc[:, i + 1]
    df_l_vs_c_compact = pd.DataFrame(compact_df_l_vs_c_list)
    df_l_vs_c_compact.rename(columns={df_l_vs_c_compact.columns[-1]: 'count_24+'}, inplace=True)
    df_l_vs_c_compact['gesamt'] = df_l_vs_c_raw.sum(axis=1)
    return df_l_vs_c_compact


