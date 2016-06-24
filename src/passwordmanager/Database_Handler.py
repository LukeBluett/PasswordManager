#!/usr/bin/env python3.4

import sqlite3

class Database_Handler:

   __sqlite_file = ''
   __table_name = ''
   __field_id = 'id'
   __field_password = 'password'
   __field_account = 'account'
   __field_description = 'description'
   __type_text = 'TEXT'
   __type_int = 'INTEGER'
	
   def __init__(self, file_location, table_name):
      self.__sqlite_file = file_location
      self.__table_name = table_name
		
   def open_connection(self)
      conn = sqlite3.connect(self.sqlite_file)
      c = conn.cursor()
		
   def close_connection(self):
      conn.commit()
      conn.close()
		
   def insert_information(self, password, account, description):
      try:
         c.execute("INSERT INTO " + self.table_name + " VALUES (?,?,?)", (password, account, description))
      except:
         print('ERROR: Something went wrong with insertion')
    		
   def create_table(self):
      c.execute("CREATE TABLE " + self.table_name + "(id INTEGER PRIMARY KEY, password TEXT, account TEXT, description TEXT)")
