import redis
print('contact...')

r=redis.StrictRedis(host='192.168.15.110',port=6379)
r.set('abc','nnmmbbzz')
a1 = r.get('abc')
print('count:',a1)
print('END')