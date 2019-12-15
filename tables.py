import sqlite3

def database():
    conn = sqlite3.connect('elinvarDatabase.db')
    c = conn.cursor()


    c.execute('DROP TABLE IF EXISTS SERVICE_DATA')
    c.execute('CREATE TABLE IF NOT EXISTS SERVICE_DATA(ServiceName text NOT NULL, RequestId text NOT NULL, EntryTime text NOT NULL, ExitTime text NOT NULL, RequestExecTime text NOT NULL)')

    c.execute('CREATE VIEW SERVICE_INFO as select ServiceName as "Service Name",RequestId, count(serviceName) as "Number of Requests", max(RequestExecTime) as "Max req execution time" from SERVICE_DATA group by ServiceName')

    print ("succesful")
    conn.commit()