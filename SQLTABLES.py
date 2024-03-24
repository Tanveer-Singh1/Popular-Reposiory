import traceback
import pymysql as pm
conn=pm.connect(host='localhost',user='root',password='12345',database='students')
cur=conn.cursor()

def showtables(cur):
    try:
        table_list={}
        cur.execute("show tables")
        ShowTables=cur.fetchall()
        for index,offset in enumerate(ShowTables):
            for index1,offset1 in enumerate(offset):
                table_list[f"{index+1}"]=offset1
        for key,value in table_list.items():
            print(f"\n\tpress {key} for {value}.")
        choice=input("\t\nEnter your choice : ")
        while choice not in table_list:
            choice=input("\n\tEnter valid choice : ")
        ShowTables=table_list[choice]
        query=f"select * from {ShowTables}"
        cur.execute(query)
        data=cur.fetchall()
        for index in data:
            for offset in index:
                print(f"\t{offset}\t\t",end=' ')
            print()
    except Exception as error:
        error=traceback.format_exc()
        print("\n\tThere is an error!!  ",error)

def create_table(cur,conn):
    try:
        data_types={'1':'int','2':'varchar(20)','3':'float'}
        table_name=input("Enter table name : ")
        string=""
        string1=""
        while True:
            column=input("Enter column name : ")
            for key,values in data_types.items():
                print(f"\n\tPress {key} for {values}.")
            choice=input("\n\tEnter your choice : ")
            while choice not in data_types:
                choice=input("\n\tPlease enter the valid choice : ")
            data_Type=data_types[choice]
            string1+=f"{column} {data_Type}"
            string+=string1
            string1=", "
            option=input("\n\tWant to Enter another column [y/n] : " )
            if option.lower()=='n':
                print("\n\tTable Created.")
                break
        query=f"create table {table_name} ({string})"
        cur.execute(query)
    except Exception as error:
        error=traceback.format_exc()
        print("\n\tError in creating table.",error)
    else:
        print("\n\tTable created sucessfully.")
        conn.commit()

def insert_into_table(cur,conn):
    try:
        table_list={}   #dict to store columns in a table. 
        query_show_tables=f"show tables"
        cur.execute(query_show_tables)
        tables=cur.fetchall()
        for key,columns in enumerate(tables):
            for key1,columns1 in enumerate(columns):  
                table_list[f"{key+1}"]=columns1
        for key,values in table_list.items():
            print(f"\t\nPress {key} for {values}")
        choice=input("Enter your choice : ")
        while choice not in table_list:
            choice=input("\t\nPlease Enter valid choice : ")
        tables=table_list[choice]
        query=f"desc {tables}"
        cur.execute(query)
        details=cur.fetchall()
        table_details={}
        for key,value in enumerate(details):
            for key1,value1 in enumerate(value):
                table_details[value[0]]=value[1]

        column_values=[]
        for key,value in table_details.items():
            column_values.append(input(f"\t\nEnter value {key} of {value} : "))
        for index in column_values:
            min_result=[f"'{index}'" for index in column_values]
            result=",".join(min_result)
        insert_query=f"insert into {tables} values ({result})"
        cur.execute(insert_query)
        # conn.commit()

    except Exception as error:
        error=traceback.format_exc()
        print("\t\nError in inserting values into table.",error)
    else:
        print("\t\nValues inserted sucessfully.")
        conn.commit()
valid=['1','2','3','n','N']
while True:
    print("\t\nPress 1 to for details of tables.")
    print("\t\nPress 2 to create new table")
    print("\t\nPress 3 to insert values to the table")
    print("\t\nPress 'Y' to continue or Press 'N' to Quit : ")
    option=input("\n\tEnter your choice : ")
    if option in valid:
        if option.lower()=='n':
            print("\t\nThank you for using.")
            break
        elif option=='1':
            showtables(cur)
        elif option=='2':
            create_table(cur,conn)
        elif option=='3':
            insert_into_table(cur,conn)
    else:
        print("\n\t\t!! Please Enter valid choice !!")

cur.close()
conn.close()