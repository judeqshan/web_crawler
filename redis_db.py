#!/usr/bin/python


import redis
import datetime

class DataBase(object):
    def __init__(self):
	self.addr = 'localhost'
	self.port = 6379
	self.writepool = {}

    def write(self, website, city, year, month, day, deal_num):
	try:
		key = "_".join([website, city, str(year), str(month), str(day)])
		val = deal_num
		r = redis.StrictRedis(host=self.addr, port=self.port)
		r.set(key, val)
	except Exception, e:
		print e
    def add_write(self, website, city, year, month, day, deal_num):
	try:
		key = "_".join([website, city, str(year), str(month), str(day)])
		self.writepool[key] = deal_num
	except Exception, e:
		print e
			
    def read(self, website, city, year, month, day):
	try:
		key = "_".join([website, city, str(year), str(month), str(day)])
		r = redis.StrictRedis(host=self.addr, port=self.port)
		val = r.get(key)
		print val
	except Exception, e:
		print e
    def batch_write(self):
	try:
		r = redis.StrictRedis(host=self.addr, port=self.port)
		r.mset(self.writepool)
	except Exception, e:
		print e

	
def batch_write():
    db = DataBase()
    beg = datetime.datetime.now()
    for i in range(1, 10001):
	db.add_write("meitun", "shenzhen", 2014, 8, 26, i)
    db.batch_write()
    end = datetime.datetime.now()
    print "batch time = ", end-beg

def single_write():
    db = DataBase()
    beg = datetime.datetime.now()
    for i in range(1, 10001):
        db.write('meitun', "shenzhen", 2014, 8, 26 ,i)
    end = datetime.datetime.now()
    print "single tiem = ", end-beg			
if __name__ == "__main__":
#	db = DataBase()
#	db.write('www.meitun.com', 'shenzhen', 2014, 8, 25, 123456)
#	db.read('www.meitun.com', 'shenzhen', 2014, 8, 25)
	batch_write()
	single_write()
	  

