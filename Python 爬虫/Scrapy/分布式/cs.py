import redis
print('contact...')

r=redis.StrictRedis(host='192.168.15.110',port=6379)
a1 = r.get('key1')
print('count:'+a1)
print('END')