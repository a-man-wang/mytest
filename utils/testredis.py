import redis

conn = redis.Redis(host='127.0.0.1',port=6379,encoding='utf-8')
# conn.set('15235991939', 6666, ex=100)
value = conn.get('15235991939')
print(value)