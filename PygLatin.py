# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 16:04:46 2018

@author: tbieleni
"""

pyg = 'ay'

original = input('Enter a word:')

if len(original) > 0 and original.isalpha():
  word = original.lower()
  first = word[0]
  new_word = word + first + pyg
  new_word = new_word[1:len(new_word)]
  print(new_word)
else:
  print('empty')