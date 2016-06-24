#! /usr/bin/env python3.4


class Account_Information:

   __password = ''
   __account = ''
   __description = ''

   def __init__(self, password, account, description):
      self.__password = password
      self.__account = account
      self.__description = description

   def get_password(self):
      return self.__password
      
   def get_account(self):
      return self.__account
      
   def get_description(self):
      return self.description

   def to_string(self):
      return 'Password: ' + self.__password + '\nAccount: ' + self.__account + '\nDescription: ' + self.__description


