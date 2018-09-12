import jsonDB as db
import os

if __name__ == '__main__':
	dir = os.getcwd()
	
	# connect to db
	base = db.json.a(dir + '//data.db')
	
	# getting the db
	data = base.read()
	
	# changing the db
	data['data'].append('This is')
	data['data'].append('jsonDB')
	data['New data'] = 'added'
	
	base.save(data)	
	base.close()
