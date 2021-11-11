class HashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 10000
        self.hash_map = [[] for _ in range(self.size)]
    
    def _hash(self, key):
        return hash(key) % self.size
    

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        hash_value = self._hash(key)

        bucket = self.hash_map[hash_value]

        found = False
        for i , v in enumerate(bucket):
            k , val = v

            print("k: %s , v: %s".format(str(k), str(val)))
            if key == k:
                found = True
                break

        if found:
            bucket[i] = (key , value)
        else:
            bucket.append((key,value))




    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        hash_value = self._hash(key)

        bucket = self.hash_map[hash_value]

        for i , v in enumerate(bucket):

            _key , _value = v

            if _key == key:
                return _value
        
        return -1


    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """

        hash_value = self._hash(key)

        bucket = self.hash_map[hash_value]

        found = False

        for i , v in enumerate(bucket):

            _key , _val = v

            if _key == key:
                bucket.pop(i)


# Your MyHashMap object will be instantiated and called as such:
obj = HashMap()
obj.put(1,2)
obj.put(1,6)
param_2 = obj.get(1)
print(param_2)
obj.remove(1)

print(obj.get(1))
