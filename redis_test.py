import time
import redis
import pickle  # Om complexe data te serialiseren

# Verbinden met Redis (zorg ervoor dat Redis draait!)
redis_client = redis.Redis(host='localhost', port=6379, db=0)

# Trage functie zonder caching
def slow_function(n):
    time.sleep(2)  # Simuleert trage verwerking
    return n * 2

# Functie met Redis caching
def redis_cached_function(n):
    cache_key = f"cache:{n}"
    
    # Check of de waarde al in Redis staat
    cached_result = redis_client.get(cache_key)
    if cached_result:
        return pickle.loads(cached_result)  # Ontcijfer de data
    
    # Anders: berekenen en opslaan in Redis (met 10 sec TTL)
    result = slow_function(n)
    redis_client.setex(cache_key, 10, pickle.dumps(result))  # 10 sec cache
    return result

# Timer-functie om tijd te meten
def measure_time(func, n):
    start = time.time()
    result = func(n)
    end = time.time()
    print(f"{func.__name__}({n}) = {result} | Tijd: {end - start:.4f} sec")

# Test zonder cache vs. met Redis cache
print("Eerste keer uitvoeren (zonder cache):")
measure_time(redis_cached_function, 5)

print("\nTweede keer uitvoeren (met Redis cache):")
measure_time(redis_cached_function, 5)  # Dit zou snel moeten zijn!
