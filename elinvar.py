import re, sqlite3
import parameters
import tables 


#Connection to the database
conn = sqlite3.connect('elinvarDatabase.db')
c = conn.cursor()

tables.database()

file_path = r"test.log"
regex_service = parameters.serviceValues()
regex_date = parameters.dateTime()
regex_timeType = parameters.timeType()


with open(file_path, "r") as file:
    for line in file:
        print(line)
        
        for match in re.finditer(regex_service, line, re.S):
            #print(match)
            match_text = match.group()
            final_text = match_text.split(":")
            

            match1 = re.search(regex_date, line, re.S)
            date = match1.group()

            match_date = date.replace(",",".")
            
        #match2 = re.search(regex_timeType, line, re.S)
        #match_time = match2.group()        
            print("\n" + "Service Name is " + final_text[0] + " and service id is " + final_text[1] + " and Date is " + match_date)

            def_val = c.execute('Select count(*) from SERVICE_DATA where RequestId = ?', (final_text[1],))
        
            if def_val.fetchall()[0][0] == 0:
                c.execute('INSERT OR REPLACE INTO SERVICE_DATA (ServiceName, RequestId, EntryTime, ExitTime, RequestExecTime) values (?,?,?,?,?)',(final_text[0],final_text[1], match_date, "" , ""))

            else :
                c.execute('UPDATE SERVICE_DATA SET ExitTime = ? where RequestId = ?', (match_date,final_text[1]))
                reqExecutionTime = c.execute('SELECT (julianday(ExitTime)-julianday(EntryTime))*8640 from SERVICE_DATA where RequestId = ?',(final_text[1],))
                c.execute('UPDATE SERVICE_DATA SET REquestExecTime = ? where RequestId = ?', (reqExecutionTime.fetchall()[0][0],final_text[1]))


actual_query = c.execute('Select * from SERVICE_INFO')

print(actual_query.fetchall())


conn.commit()     
