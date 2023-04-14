

import pymysql
from pymysql import Connection as MysqlConn
# import psycopg2
# from psycopg2._psycopg import connection as PostgresConn

class Database:
  def __init__(self, db:str|None=None, host:str="localhost", user:str="root", password:str="1234") -> None:
    self.host = host
    self.user = user
    self.password = password
    self.db = db
    
  def Conn(self) -> MysqlConn:
    conn = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.db)
    # conn = psycopg2.connect(host=self.host, user=self.user, password=self.password, dbname=self.db)
    return conn
  
  def Exec(self, sql:str) -> bool:
    ok = False
    try:
      conn = self.Conn()
      cur = conn.cursor()
      cur.execute(sql)
      conn.commit()
      ok = True
    except pymysql.connect.Error as error:
      print("MYSQL Run Error: {}".format(error))
    finally:
      if conn.ping():
        cur.close()
        conn.close()
    return ok
  
  def getArray(self, sql:str) -> list[tuple]:
    conn = self.Conn()
    cur = conn.cursor()
    cur.execute(sql)
    res = cur.fetchall()
    cur.close()
    conn.close()
    return res