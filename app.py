#Copyright (c) 2026 Alexandra Folttinyová
#This program is free software under the terms of the GNU General Public License v3.
#See the LICENSE file in the project root for full terms


import json
import os
import time
import random

def clear():
  os.system('clear')

def fetch_data():
  try:
    with open('data.json', 'r') as file:
      return json.load(file)
  except FileNotFoundError:
    return []

def get_last_index(data):
  if not data:
    return 0
  return max(item['index'] for item in data)

def save_data(data):
  with open('data.json', 'w') as file:
    json.dump(data, file, indent=4)
    return 0

def add_expense():
  data = fetch_data()

  while True:
    clear()
    print('Whats the expense category?')
    category = input("> ")
    if category:
      break
    else:
      clear()
      print('Please type a category.')

  while True:
    clear()
    print('Whats the amount?')
    amount = input('> ')
    if amount:
      try:
        amount = int(round(float(amount)))
        break
      except ValueError:
        clear()
        print('Please enter a VALID amount.')
    else:
      clear()
      print('Please enter an amount.')


  while True:
    clear()
    print('Whats the description?')
    description = input('> ')
    if description:
      break
    else:
      clear()
      print('Please enter a description.')

  
    index = get_last_index(data) + 1

  expense = {
    'index': index,
    'category': category,
    'description': description,
    'amount': amount
  }

  data.append(expense)
  save_data(data)
  return

def read_data():

  data = fetch_data()
  if not data:
    clear()
    print('No data on file.')
    time.sleep(2)
    return


  page_size = 3
  total_items = len(data)
  total_pages = (total_items + page_size -1 ) // page_size
  current_page = 0

  while True:
    clear()
    print(f'=== Your Expenses (Page: {current_page + 1} of {total_pages}) ===\n')

    start_index = current_page * page_size
    end_index = start_index + page_size
    current_slice = data[start_index:end_index]

    for item in current_slice:
      item_amount = item['amount'] * 0.01
      print(f'Index: {item["index"]}')
      print(f'Amount: {item_amount}')
      print(f'Category: {item["category"]}')
      print(f'Description: {item["description"]}')
      print('--------------------------------')

    print('[N] Next Page | [P] Previous Page | [exit] Exit')
    uI = input('> ').strip().lower()

    if uI == 'n':
      current_page = (current_page + 1) % total_pages
    elif uI == 'p':
      current_page = (current_page - 1) % total_pages
    elif uI == 'exit':
      break
    else:
      clear()
      print('Invalid option. Try Again!')
      time.sleep(2)

def update_data():
  data = fetch_data()

  if not data:
    print('There is no data on file.')
    return

  while True:
    while True:
      print('Whats the index of the item you want to update? (Type "exit" to exit)')
      uI = input('> ').lower()

      if uI == 'exit':
        return

      try:
        working_index = int(uI)
        break
      except ValueError:
        print('Invalid Input. Try Again!')

    for item in data:
      if item['index'] == working_index:
        working_data = item
        fetch_updates(working_data)
        save_data(data)
        return
    print(f'There is no item with the index {working_index}')

def fetch_updates(working_data):

  print(f'Current category: {working_data["category"]}')
  print('Whats the new category? (press "enter" to continue)')
  uI = input('> ')
  if uI:
    working_data['category'] = uI

  print(f'Current description: {working_data["description"]}')
  print('Whats the new description? (press "enter" to continue)')
  uI = input('> ')
  if uI:
    working_data['description'] = uI

  while True:
    print(f'Current amount: {working_data["amount"]}')
    print('Whats the new amount? (press "enter" to continue)')
    uI = input('> ')
    if uI:
      try:
        uI = float(uI)
        uI = uI * 100
        uI = round(uI)
        uI = int(uI)
        working_data['amount'] = uI
        break
      except ValueError:
        print('Wrong value. Try Again!')


  return working_data

def delete_data():
  data = fetch_data()

  if not data:
    print('There is no data on file.')
    return

  while True:
    while True:
      print('Whats the index of the item you want to delete? (Type "exit" to exit)')
      uI = input('> ').lower()

      if uI == 'exit':
        return

      try:
        working_index = int(uI)
        break
      except ValueError:
        print('Invalid Input. Try Again!')

    for item in data:
      if item['index'] == working_index:
        data.remove(item)
        save_data(data)
        return
    print(f'There is no item with the index {working_index}.')

def get_help():
    commands = """
"add"   => Add an expense
"read"  => Show list of items on file
"remove"=> Remove an expense
"edit"  => Edit an expense
"exit"  => Use anywhere to go a step back
    """
    clear()
    print("List of valid commands:")
    print(commands)
    _ = input('Press Enter to continue...')

def main():
  clear()
  print('Loading...')
  time.sleep(random.randint(2,10))
  while True:
    clear()
    print('ExpenseTracker (c)')
    print('===============')
    print('Welcome to your expense tracker. :D')
    print('Start your tracking or type "help".')
    uI = input('> ')
    if uI == 'help':
      get_help()
    elif uI == 'exit':
      clear()
      print('Thank You for using ExpenseTracker (c)')
      time.sleep(3)
      break
    elif uI == 'add':
      add_expense()
    elif uI == 'read':
      read_data()
    elif uI == 'remove':
      delete_data()
    elif uI == 'edit':
      update_data()
      



main()


