import redis

redis_client = redis.Redis()

redis_client.sadd("fruits", "apple")
redis_client.sadd("fruits", "banana")
redis_client.sadd("fruits", "orange")
redis_client.sadd("fruits", "lemon")

fruits = redis_client.smembers("fruits")
print(fruits)