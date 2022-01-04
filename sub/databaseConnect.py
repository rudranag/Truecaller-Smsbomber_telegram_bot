import psycopg2
import os


class Database:

    def __init__(self):

        self.username=os.environ.get('username')
        self.password=os.environ.get('password')
        self.dbname=os.environ.get('dbname')
        self.host=os.environ.get('host')
        self.port=os.environ.get('port')


    def protect_number(self,chat_id, mobile_number):
        try:
            connection = psycopg2.connect(user=self.username,
                                          password=self.password,
                                          host=self.host,
                                          port=self.port,
                                          database=self.dbname)
            connection.autocommit = True
            cursor = connection.cursor()

            postgres_insert_query = """ INSERT INTO protected_list (chat_id, mobile) VALUES (%s,%s)"""
            record_to_insert = (chat_id,mobile_number)
            cursor.execute(postgres_insert_query, record_to_insert)


        except (Exception, psycopg2.Error) as error:
            print("Error in update operation", error)
            
        finally:
            if connection:
                cursor.close()
                connection.close()
                
    def unprotect_number(self,chat_id, mobile_number):
        try:
            connection = psycopg2.connect(user=self.username,
                                          password=self.password,
                                          host=self.host,
                                          port=self.port,
                                          database=self.dbname)
            connection.autocommit = True
            cursor = connection.cursor()

            postgres_delete_query = """ delete from protected_list where mobile=%s and chat_id=%s"""
        
            cursor.execute(postgres_delete_query, (mobile_number,chat_id))
            count = cursor.rowcount


        except (Exception, psycopg2.Error) as error:
            print("Error in update operation", error)
            
        finally:
            if connection:
                cursor.close()
                connection.close()
                

        return count

     

    def check_if_exists(self,chat_id,mobile_number):
        try:
            connection = psycopg2.connect(user=self.username,
                                          password=self.password,
                                          host=self.host,
                                          port=self.port,
                                          database=self.dbname)
            connection.autocommit = True
            cursor = connection.cursor()

            postgres_check_query = """ select * from protected_list where mobile=%s and chat_id=%s"""
        
            cursor.execute(postgres_check_query, (mobile_number,chat_id))
            count = cursor.rowcount


        except (Exception, psycopg2.Error) as error:
            print("Error in update operation", error)
            
        finally:
            if connection:
                cursor.close()
                connection.close()
                
        return count 
        
            

    
