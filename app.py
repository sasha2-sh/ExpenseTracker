#Copyright (c) 2026 Alexandra Folttinyová
#This program is free software under the terms of the GNU General Public License v3.
#See the LICENSE file in the project root for full terms


import json
import os
import time
import random
from datetime import date, datetime

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
    elif category == 'exit' or category == 'e':
      return
    else:
      clear()
      print('Please type a category.')
      time.sleep(2)

  while True:
    clear()
    print('Whats the amount?')
    amount = input('> ')
    if amount:
      if amount == 'exit' or amount == 'e':
        return
      else:
        try:
          amount = int(round(float(amount)*100))
          break
        except ValueError:
          clear()
          print('Please enter a valid amount.')
          time.sleep(2)
    else:
      clear()
      print('Please enter an amount.')
      time.sleep(2)


  while True:
    clear()
    print('Whats the description?')
    description = input('> ')
    if description:
      if description == 'exit' or description == 'e':
        return
      else:
        break
    else:
      clear()
      print('Please enter a description.')
      time.sleep(2)

  while True:
    clear()
    print('Whats the date of the transaction? (YYYY.MM.DD) (leave blank for today)')
    transaction_date = input('> ')
    if transaction_date:
      if transaction_date == 'exit' or transaction_date == 'e':
        return
      else:
        try:
          iso_date = datetime.strptime(transaction_date, '%Y.%m.%d').date().isoformat()
          break
        except ValueError:
          clear()
          print('Please provide a valid date.')
      
    else:
      iso_date = date.today().isoformat()
      break


  
  index = get_last_index(data) + 1

  expense = {
    'index': index,
    'date': iso_date,
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
      raw_date = item.get("date", "2026-01-01")
      transaction_date = datetime.strptime(raw_date, '%Y-%m-%d').strftime('%d.%b.%Y').upper()
      item_amount = item['amount'] * 0.01
      print(f'Index: {item["index"]}')
      print(f'Amount: {item_amount}')
      print(f'Date: {transaction_date}')
      print(f'Category: {item["category"]}')
      print(f'Description: {item["description"]}')
      print('--------------------------------')

    print('[N] Next Page | [P] Previous Page | [exit] Exit')
    uI = input('> ').strip().lower()

    if uI == 'n':
      current_page = (current_page + 1) % total_pages
    elif uI == 'p':
      current_page = (current_page - 1) % total_pages
    elif uI == 'exit' or uI == 'e':
      break
    else:
      clear()
      print('Invalid option. Try Again!')
      time.sleep(2)

def update_data():
  data = fetch_data()

  if not data:
    clear()
    print('There is no data on file.')
    time.sleep(3)
    return

  while True:
    while True:
      clear()
      print('Whats the index of the item you want to update? (Type "exit" to exit)')
      uI = input('> ').lower()

      if uI == 'exit' or uI == 'e':
        return

      try:
        working_index = int(uI)
        break
      except ValueError:
        clear()
        print('Invalid Input. Try Again!')
        time.sleep(2)

    for item in data:
      if item['index'] == working_index:
        working_data = item
        fetch_updates(working_data)
        save_data(data)
        return
    clear()
    print(f'There is no item with the index {working_index}')
    time.sleep(3)

def fetch_updates(working_data):

  clear()
  print(f'Current category: {working_data["category"]}')
  print('Whats the new category? (press "enter" to continue)')
  uI = input('> ')
  if uI:
    if uI == 'exit' or uI == 'e':
      return
    else:
      working_data['category'] = uI

  clear()
  print(f'Current description: {working_data["description"]}')
  print('Whats the new description? (press "enter" to continue)')
  uI = input('> ')
  if uI:
    if uI == 'exit' or uI == 'e':
      return
    else:
      working_data['description'] = uI


  while True:
    clear()
    raw_date = working_data.get("date", "2026-01-01")
    transaction_date = datetime.strptime(raw_date, '%Y-%m-%d').strftime('%d.%b.%Y').upper()
    print(f'Current Date: {transaction_date}')
    print('Whats the date of the transaction? (YYYY.MM.DD) (press "enter" to continue)')
    transaction_date = input('> ')
    if transaction_date:
      try:
        iso_date = datetime.strptime(transaction_date, '%Y.%m.%d').date().isoformat()
        working_data['date'] = iso_date
        break
      except ValueError:
        clear()
        print('Please provide a valid date.')
        time.sleep(2)
    else:
      break


  while True:
    clear()
    print(f'Current amount: {working_data["amount"]*0.01}')
    print('Whats the new amount? (press "enter" to continue)')
    uI = input('> ')
    if uI:
      if uI == 'exit' or uI == 'e':
        return
      else:
        try:
          uI = float(uI)
          uI = uI * 100
          uI = round(uI)
          uI = int(uI)
          working_data['amount'] = uI
          break
        except ValueError:
          clear()
          print('Wrong value. Try Again!')
          time.sleep(2)


    return working_data

def delete_data():
  data = fetch_data()

  if not data:
    clear()
    print('There is no data on file.')
    time.sleep(2)
    return

  while True:
    while True:
      clear()
      print('Whats the index of the item you want to delete? (Type "exit" to exit)')
      uI = input('> ').lower()

      if uI == 'exit' or uI == 'e':
        return

      try:
        working_index = int(uI)
        break
      except ValueError:
        clear()
        print('Invalid Input. Try Again!')
        time.sleep(2)

    for item in data:
      if item['index'] == working_index:
        data.remove(item)
        save_data(data)
        return
    clear()
    print(f'There is no item with the index {working_index}.')
    time.sleep(3)

def get_help():
    commands = """
"add"   => Add an expense
"read"  => Show list of items on file
"delete"=> Remove an expense
"update"=> Edit an expense
"exit"  => Use anywhere to go a step back
    """
    clear()
    print("List of valid commands:")
    print(commands)
    _ = input('Press Enter to continue...')

def about():
    about_text = """
Copyright (c) 2026 Alexandra Folttinyová
This program is free software under the terms of the GNU General Public License v3.
See the LICENSE file in the project root for full terms
    """
    clear()
    print(about_text)
    _ = input('Press Enter to continue...')

def main():
  clear()
  print('Loading...')
  time.sleep(random.randint(1,7))
  while True:
    clear()
    print('ExpenseTracker (c)')
    print('===============')
    print('Welcome to your expense tracker. :D')
    print('Start your tracking or type "help".')
    uI = input('> ')
    if uI == 'help':
      get_help()
    elif uI == 'exit' or uI == 'e':
      clear()
      print('Thank You for using ExpenseTracker (c)')
      time.sleep(3)
      break
    elif uI == 'add' or uI == 'a':
      add_expense()
    elif uI == 'read' or uI == 'r':
      read_data()
    elif uI == 'delete' or uI == 'd':
      delete_data()
    elif uI == 'update' or uI == 'u':
      update_data()
    elif uI == 'about':
      about()
    else:
      clear()
      print('Plase Enter a Valid Command.')
      time.sleep(3)




main()


