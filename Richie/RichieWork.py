import pyodbc

class DatabaseManagement:
    def connect_to_database(self):
        '''
        Connect to our SQL Server instance
        @return the connection object or none on failure
        '''
        try:
            conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=lcb-sql.uccob.uc.edu\\nicholdw;'
                      'Database=IS4010;'
                      'uid=IS4010Login;'
                      'pwd=P@ssword2;')
        except:
            return None

            return conn
