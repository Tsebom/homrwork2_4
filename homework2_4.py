import operator
import os

def file_sql(list_file):
	"""Возвращает список фаилов с расширением .sql, аргумент - (исходный список фаилов)"""
	file_list_sql = []
	for name in list_file:
		if operator.__eq__(os.path.splitext(name)[1], '.sql'):
			file_list_sql.append(name)
	return file_list_sql

def input_str():
	"""Запрашивет искомую строку"""
	search_string = input('Введите строку: ')
	return search_string.strip()

def open_file(file, search, directory):
	"""Открывает фаил и проверяет вхождение искомой строки, аргументы - (имя фаила, искомая строка, директория с фаилами)""" 
	with open(os.path.join(directory, file)) as f:
		data = f.read()
		if not search in data:
			return False
		return True

def list_search_file(list_, directory):
	"""Возвращает список фаилов удовлетворивших поискову запрос, аргумент - (исходный список, директория с фаилами)"""
	list_file = []
	search_str = input_str()
	for name in list_:
		if open_file(name, search_str, directory):
			list_file.append(name)
	print('\n'.join(list_file))
	print('Всего: {}'.format(len(list_file)))
	return list_file

def main():
	directory_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Migrations')
	list_file = os.listdir(directory_file)
	list_file_sql = file_sql(list_file)# Список фаилов с расширением *.sql
	while operator.__gt__(len(list_file_sql), 1):
		list_file_sql = list_search_file(list_file_sql, directory_file)

main()