#Copyright (c) 2026 Alexandra Folttinyová
#This program is free software under the terms of the GNU General Public License v3.
#See the LICENSE file in the project root for full terms


import json
import os

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