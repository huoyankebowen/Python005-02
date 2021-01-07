# 操作zset
import redis

client = redis.Redis(host='192.168.56.101', password='testpass')

client.zadd('rank', {'a': 4, 'b': 3, 'c': 1, 'd': 2, 'e': 5})

client.zincrby('rank', -2, 'e')

# print(client.zrangebyscore('rank', 1, 5))

# zrevrank  从大到小

# 基card
print(client.zcard('rank'))

# # 显示评分
print(client.zrange('rank', 0, 5, withscores=True))

print(client.zrevrange('rank', 0, 2, withscores=True))

