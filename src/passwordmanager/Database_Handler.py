#!/usr/bin/env python3.4

import sqlite3

class Database_Handler:

	__sqlite_file = ''
	__table_name = ''
	__field_id = 'id'
	__field_password = 'password'
	__field_account = 'account'
	__field_description = 'description'
	__type_string = 'STRING'
	__type_int = 'INTEGER'
	
	def __init__(self):
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
