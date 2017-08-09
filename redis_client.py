__author__ = 'root'

import redis

r_server = redis.Redis('localhost') #this line creates a new Redis object and
                                    #connects to our redis server
r_server.set('test_key', 'test_value') #with the created redis object we can
                                        #submits redis commands as its methods

print 'previous set key ' + r_server.get('test_key') # the previous set key is fetched