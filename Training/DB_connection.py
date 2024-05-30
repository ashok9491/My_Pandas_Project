import snowflake.connector as db
import pandas as pd
connection  = db.connect(user = 'ASHOK',password = 'Bluebird@01',account = 'ut54117.ap-southeast-1')
cursor = connection.cursor()
cursor.execute('Select * from SAMPLEDB.PUBLIC.EMPLOYEES')
data1 = cursor.fetchall()
df1 = pd.DataFrame(data1)
cursor.execute('Select * from SAMPLEDB.PUBLIC.EMPLOYEES_TARGET')
data2 = cursor.fetchall()
df2 = pd.DataFrame(data2)
#df.to_csv("C:\\Python_SF\\SNOWLAKE_CONNECTION_SETUP\\Output_report\\mydata.csv")
print(df1)
print(df2)


