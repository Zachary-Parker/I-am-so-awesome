# def func():
#   print('this is for the test of t1')
#
# func()
# #
#
# def do(request):
# 	print('done at home')
# do()
#
#
# sdfsfdsdfsf
#
#
# def func2():
#     print(1111)
# func2()
#
# sdfsdfsdfsdffsdf
#
#
# def func3():
#
# 	pass
import redis
pool = redis.ConnectionPool(host='127.0.0.1', port=6379, decode_responses=True)
h = redis.Redis(connection_pool=pool)
h.hset('id','name','Parker')
h.hset('id','age',15)
print(h.hkeys('id'))
print(h.hget('id','name'))
