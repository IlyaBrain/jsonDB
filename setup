#!/usr/bin/env python
# -*- coding: utf-8 -*-

import portalocker
import time as tm
import json as j

class json(object):
	class a(object):
		def __init__(self, dir):
			i = 0
			while True:
				try:
					self.gDir = dir
					self.file = open(dir, 'r+')
					portalocker.lock(self.file, portalocker.LOCK_EX)
				except portalocker.exceptions.LockException:
					i += 1
					if i >= 5:
						break
				else:
					break
		
		def read(self):
			self.file = open(self.gDir, 'r')
			data = self.file.read()
			return j.loads(data)
			
		def save(self, data):
			with open(self.gDir, 'w') as self.file:
				j.dump(data, self.file, indent=4, ensure_ascii=False)
			
		def close(self):
			self.file.close()
				
	def save(dir, data):
		with open(dir, 'w') as file:
			j.dump(data, file, indent=4, ensure_ascii=False)
	
	def open(dir):
		return j.loads(open(dir, 'r').read())
		
class file:
	def save(dir, data):
		with open(dir, 'w') as file:
			file.write(data)
	
	def open(dir):
		return open(dir).read()
		
	class bin:
		def save(dir, data):
			with open(dir, 'wb') as file:
				file.write(data)
		
		def open(dir):
			return open(dir, 'rb').read()
