# Define a Hash Map Class
class HashMap:
    def __init__(self, array_size):
        self.array_size = array_size
        # Create an instance variable called .array, which is a list of size array_size
        self.array = [None for i in range(self.array_size)]

    # hashing function takes a key and returns an index into the underlying array.
    def hash(self, key):
        # .encode() is a string method that converts a string into bytes  as list-like object with the numerical representation of each character in the string.
        key_bytes = key.encode()
        hash_code = sum(key_bytes)
        return hash_code
    
    # compression function uses modular arithmetic to calculate an array index for a hash map when given a hash code.
    def compressor(self, hash_code):
        return hash_code % self.array_size

    # Setter function that assigns value to an index based off key
    def assign(self, key, value):
        array_index = self.compressor(self.hash(key))
        self.array[array_index] = value

    # Getter function that retrieves value 
    def retrieve(self, key):
        array_index = self.compressor(self.hash(key))
        return self.array[array_index]

