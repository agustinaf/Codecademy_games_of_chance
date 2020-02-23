# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 18:31:35 2020

@author: AgusF
"""

import random
my_money = 100

def heads_or_tails(money,call):
  if money <= 0:
    print("You need to bet money to play!")
    return 0
  elif call == "Heads" or call == "Heads!" or call == "heads" or call == "head":
    call = 1
  else:
    call = 0
  num = random.randint(0,1)
  if num == call:
    print("You won $" + str(money) + "!!!")
    return money
  else: 
    print("You lost, try again.")
    return -money 

def cho_han(money, prediction):
  num = random.randint(1,6) + random.randint(1,6)
  if num % 2 == 0:
    num = "Even"
  else:
    num = "Odd"
  if prediction == num:
    print("You won $" + str(money) + "!!!")
    return money
  else:
    print("You lost, try again.")
    return -money

def cards(money, prediction):
  you = random.randint(1,13)
  other = random.randint(1,13)
  if prediction == "y":
    call = 1
  else:
    call = 0
  if you > other and call == 1:
    print("You won $" + str(money) + "!!!")
    return money
  elif you > other and call == 0:
    print("You lost, try again.")
    return -money
  elif you < other and call == 0:
    print("You won $" + str(money) + "!!!")
    return money
  elif you < other and call == 1:
    print("You lost, try again.")
    return -money
  else:
    print("You lost, try again.")
    return -money
 

def roulette(money, oddoreven, number):
  num = random.randint(0,37)
  # 0 = 0 
  # 37 = 00
  if num % 2 == 0:
    num1 = "Even"
  else:
    num1 = "Odd"
    
  if num1 != "No" and number != -1:
    #if oddoreven == num1 and number != 0 or number != 37 and num = 0 or num == 37:
      #return "You lost, try again."
    if oddoreven == num1 and number == num:
      print("You won number and odds = $" + str(money * 2 + money * 35) + "!!!")
      return money * 2 + money * 35
    elif oddoreven == num1 and number != num:
      print("You won odds (not number) = $" + str(money) + "!!!")
      return money
    elif oddoreven != num1 and number == num:
      print("You won number (not odds) = $" + str(money * 35) + "!!!")
      return money * 35 
    else:
      print("You lost, try again.")
      return -money
  elif num1 == "No" and number != -1:
    if number == num:
      print("You won number = $" + str() + "!!!")
      return money * 35
    else:
      print("You lost, try again.")
      return -money
  elif num1 != "No" and number == -1:
    if oddoreven == num1:
      print("You won odds = $" + str(win) + "!!!")
      return money
    else:
      print("You lost, try again.")
      return -money

my_money += heads_or_tails(1,"Tails")
my_money += cho_han(10, "Odd")    
my_money += cards(10, "n")    
my_money += roulette(10, "Even", 16)
print("My money total: $" + str(my_money))