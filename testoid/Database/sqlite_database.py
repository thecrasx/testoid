import sqlite3
from typing import Any




class SQLiteDB:
    def __init__(self, database) -> None:
        
        self.__conn = sqlite3.connect(database)
        self.__cursor = self.__conn.cursor()


    @property
    def connection(self) -> sqlite3.Connection:
        return self.__conn
    
    @property
    def cursor(self) -> sqlite3.Cursor:
        return self.__cursor


    def close(self) -> None:
        self.__conn.close()

    def commit(self) -> None:
        self.__conn.commit()


    def commitOnExecutionSuccess(self, success: bool) -> bool:
        if success:
            self.commit()
            return True
        else:
            return False


    def execute(self, command) -> bool:
        try:
            self.__cursor.execute(command)
            return True
        except Exception as e:
            print("SQLiteError: ", e)
            return False




    def fetchOne(self) -> Any:
        return self.__cursor.fetchone()

    def fetchMany(self, size: int) -> Any:
        return self.__cursor.fetchmany(size)

    def fetchAll(self) -> Any:
        return self.__cursor.fetchall()

    def recordExists(self):
        if self.fetchOne():
            return True
        else:
            return False


    
    def isExecutedSuccessfully(self, executionSuccess, commitOnSuccess=False) -> bool:
        if executionSuccess:
                if commitOnSuccess:
                    self.commit()
                return True
        else:
            return False






