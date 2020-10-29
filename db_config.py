'''
#The purpose of this file is to make database connection
'''
import traceback
import psycopg2
import psycopg2.extras
import asyncpg
import logging
import gc
import pandas as pd
from sqlalchemy import create_engine
#Helper function
LOGGER = logging.getLogger('report_api')
LOGGER.setLevel(logging.INFO)


async def read_data_in_pandas(database, query):
    dbConnection = None
    cur = None
    # data = []
    try:
        #If read only host is availble then picking from readonly otherwise from default rds host
        rds_host = database.get("readonly_host","") if database.get("readonly_host","") else database.get("host","")
        con = await asyncpg.connect(user=database["user"], password=database["password"],\
            database=database["database"], host=rds_host)
        user = database["user"]
        password = database["password"]
        database = database["database"]
        engine = create_engine(f"postgresql+psycopg2://{user}:{password}@{rds_host}/{database}")
        dbConnection = engine.connect()
        LOGGER.info("Database connection successfully created")
        LOGGER.info(query)
        # cur = con.cursor()
        df = pd.read_sql_query(query, con=dbConnection)
        
        # records = await con.fetch(query)
        # LOGGER.info("Length of records: {0}".format(len(records)))
        # for record in records:
        #     data.append(dict(record))
        # await cur.close()
        # cur.close()
        # await con.close()
        dbConnection.close()
        LOGGER.info("Database connection successfully closed")
        # del records
        # gc.collect()
        return df
    except Exception as error:
        if dbConnection != None:
            dbConnection.close()
        # await con.close()
        LOGGER.error("After exception database connection successfully closed")
        LOGGER.error(f"L1: EXCEPTION OCCURED {str(error)}")
    return None

async def async_execute_select(database, query):
    ''' This function uses asyncpg for connection'''
    con = None
    data = []
    try:
        #If read only host is availble then picking from readonly otherwise from default rds host
        rds_host = database.get("readonly_host","") if database.get("readonly_host","") else database.get("host","")
        con = await asyncpg.connect(user=database["user"], password=database["password"],\
            database=database["database"], host=rds_host)
        LOGGER.info("Database connection successfully created")
        LOGGER.info(query)
        records = await con.fetch(query)
        LOGGER.info("Length of records: {0}".format(len(records)))
        for record in records:
            data.append(dict(record))
        await con.close()
        LOGGER.info("Database connection successfully closed")
        del records
        gc.collect()
    except Exception as error:
        await con.close()
        LOGGER.error("After exception database connection successfully closed")
        LOGGER.error(f"L1: EXCEPTION OCCURED {str(error)}")
    return data

#Connecting to the database
def make_connection(database):
    # pylint: disable-msg=W0703
    '''
    Input  -
       params: database - The name of the database to be connected
    Output - Connected to the database
    '''
    conn = None
    #Checking if the database exist
    try:
        #If read only host is availble then picking from readonly otherwise from default rds host
        rds_host = database.get("readonly_host","") if database.get("readonly_host","") else database.get("host","")
        conn = psycopg2.connect(database=database["database"], user=database["user"],
                                password=database["password"], host=rds_host,
                                port=database["port"])
        LOGGER.info("Database connection successfully created")
    except Exception as error:
        LOGGER.error(f"L1: EXCEPTION OCCURED {str(error)}")
    return conn

#Helper function
#Closing the database connection
def close_connection(conn):
    # pylint: disable-msg=W0703
    '''
    Input -
       params: conn - Connection object
    Output - The connection to the database is closed
    '''
    try:
        conn.close()
        LOGGER.info("Database connection successfully closed")
    except Exception as error:
        LOGGER.error(f"L1: EXCEPTION OCCURED {str(error)}")

#Helper function
#Creating cursor object
def get_cursor(conn):
    # pylint: disable-msg=W0703
    '''
    Input  -
       params: conn - Connection object
    Output - Cursor object is created
    '''
    cursor = None
    try:
        cursor = conn.cursor()
    except Exception as error:
        LOGGER.error(f"L1: EXCEPTION OCCURED  {str(error)}")
    return cursor

def get_cursor_with_dict(conn):
     # pylint: disable-msg=W0703
    '''
    Input  -
       params: conn - Connection object
    Output - Dict cursor object is created
    '''
    cursor = None
    try:
        cursor = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    except Exception as error:
        LOGGER.error(f"L1: EXCEPTION OCCURED {str(error)}")
    return cursor

# execute select query
def execute_selectquery(query, cursor):
   # pylint: disable-msg=W0703
    '''
    Input  -
       params: query - The query to be executed
       params: cursor - Cursor object
    Output - The single record is fetched based on the query
    '''
    data = ()
    try:
        cursor.execute(query)
        data = cursor.fetchone()
    except Exception as error:
        LOGGER.error(f"L1: EXCEPTION OCCURED {str(error)}")
    return data

def execute_all_selectquery(query, cursor, tuple_data=None):
     # pylint: disable-msg=W0703
    '''
    Input  -
        params: query - The query to be executed
       params: cursor - cursor object
       params: tuple_data:
       Output - All the records are fetched
    '''
    data = ()
    try:
        if not tuple_data:
            cursor.execute(query)
        else:
            cursor.execute(query, tuple_data)
        data = cursor.fetchall()
    except Exception as error:
        LOGGER.error(f"L1: EXCEPTION OCCURED {str(error)}")
        traceback.print_exc()
    return data

def exist_conn_closed(conn):
    '''
        checking if connection is not closed then closed the connection
        Input -
        param: conn - Database connection object
    '''
    if conn and conn.closed == 0:
        conn.close()
        LOGGER.info("After exception database connection successfully closed")

def exist_cur_conn_closed(conn, cursor):
    '''
    closing database connection and cursor
    Input -
        params: conn - Database connection object
        params: cursor -Database cursor object
    '''
    cursor.close()
    conn.close()
    LOGGER.info("Database connection successfully closed")

DEFAULT_CONFIG_PATH = "bucket_config.json"
