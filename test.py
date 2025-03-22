import time
import functools
from cachetools import TTLCache, cached
import diskcache as dcache

# Handmatige cache (dictionary-based)
manual_cache = {}

# TTLCache van cachetools (cache verloopt na X seconden)
ttl_cache = TTLCache(maxsize=10, ttl=10)

# Diskcache voor persistente caching op schijf
disk_cache = dcache.Cache('./cache_dir')

# Functie zonder caching (baseline)
def slow_function(n):
    time.sleep(2)  # Simuleert trage verwerking
    return n * 2

# Functie met lru_cache (In-memory caching)
@functools.lru_cache(maxsize=10)
def lru_cached_function(n):
    time.sleep(2)
    return n * 2

# Handmatige caching
def manual_cached_function(n):
    if n in manual_cache:
        return manual_cache[n]
    time.sleep(2)
    manual_cache[n] = n * 2
    return manual_cache[n]

# Cachetools TTLCache
@cached(ttl_cache)
def ttl_cached_function(n):
    time.sleep(2)
    return n * 2

# Diskcache (schijfopslag)
def disk_cached_function(n):
    if n in disk_cache:
        return disk_cache[n]
    time.sleep(2)
    disk_cache[n] = n * 2
    return disk_cache[n]

# Timer-functie om uitvoeringstijd te meten
def measure_time(func, n):
    start = time.time()
    result = func(n)
    end = time.time()
    print(f"{func.__name__}({n}) = {result} | Tijd: {end - start:.4f} sec")

# Testen van de functies
print("Eerste keer uitvoeren (zonder cache gevuld):")
measure_time(slow_function, 5)
measure_time(lru_cached_function, 5)
measure_time(manual_cached_function, 5)
measure_time(ttl_cached_function, 5)
measure_time(disk_cached_function, 5)

print("\nTweede keer uitvoeren (met cache):")
measure_time(slow_function, 5)  # Nog steeds traag
measure_time(lru_cached_function, 5)  # Snel
measure_time(manual_cached_function, 5)  # Snel
measure_time(ttl_cached_function, 5)  # Snel
measure_time(disk_cached_function, 5)  # Snel
