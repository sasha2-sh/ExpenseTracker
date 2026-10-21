#Copyright (c) 2026 Alexandra Folttinyová
#This program is free software under the terms of the GNU General Public License v3.
#See the LICENSE file in the project root for full terms


import json

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

  print('Whats the expense category?')
  category = input("> ")
  print('Whats the amount?')
  amount = int(round(float(input('> '))*100))
  print('Whats the description?')
  description = input('> ')
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
    print('No data on file.')
    return

  print('---Your Expenses---')
  for item in data:
    item_amount = item['amount'] * 0.01
    print(f'Index: {item["index"]}')
    print(f'Amount: {item_amount}')
    print(f'Category: {item["category"]}')
    print(f'Description: {item["description"]}')
    print('--------------------------------')
  return

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
  commands = '"add" => Add an expense' \
  '"read" => Show list of ' \
  '"remove" => Remove an expense' \
  '"edit" => Edit an expense'
  print('List of valid commands:')
  print(commands)

def main():
  while True:
    print('EXPENSE TRACKER')
    print('===============')
    print('Welcome to your expense tracker')
    print('Start your tracking or type "help" for help.')
    uI = input('> ')
    if uI == 'help':
      get_help()





