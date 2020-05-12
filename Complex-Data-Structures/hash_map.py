# Define a Hash Map Class
class HashMap:
	def __init__(self, array_size):
		self.array_size = array_size
		# Create an instance variable called .array, which is a list of size array_size
		self.array = [None for i in range(self.array_size)]

	# hashing function takes a key and returns an index into the underlying array.
	def hash(self, key, number_collisions=0):
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
		current_array_value = self.array[array_index]

		if current_array_value is None:
			  self.array[array_index] = [key, value]
			  return

		if current_array_value[0] == key:
			  self.array[array_index] = [key, value]
			  return

		# Collision!

		number_collisions = 1

		while(current_array_value[0] != key):
			  new_hash_code = self.hash(key, number_collisions)
			  new_array_index = self.compressor(new_hash_code)
			  current_array_value = self.array[new_array_index]

			  if current_array_value is None:
				  self.array[new_array_index] = [key, value]
				  return

			  if current_array_value[0] == key:
				  self.array[new_array_index] = [key, value]
				  return

			  number_collisions += 1

			  return

	# Getter function that retrieves value
	def retrieve(self, key):
		array_index = self.compressor(self.hash(key))
		possible_return_value = self.array[array_index]
		
		if possible_return_value is None:
			return None

		if possible_return_value[0] == key:
			return possible_return_value[1]

		retrieval_collisions = 1

		while (possible_return_value != key):
			new_hash_code = self.hash(key, retrieval_collisions)
			retrieving_array_index = self.compressor(new_hash_code)
			possible_return_value = self.array[retrieving_array_index]

		if possible_return_value is None:
			return None

		if possible_return_value[0] == key:
			return possible_return_value[1]

		retrieval_collisions += 1

		return
