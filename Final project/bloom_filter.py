# Python 3 program to build Bloom Filter
# Install mmh3 and bitarray 3rd party module first
# pip install mmh3
# pip install bitarray
from random import shuffle
import math
import mmh3
from bitarray import bitarray
import time
import sys

class BloomFilter(object):
    '''
    Class for Bloom filter, using murmur3 hash function
    '''
    
    # items_count - Number of items expected to be stored in the bloom filter
    # fp_prob - False Positive probability in decimal
    def __init__(self, items_count: int, fp_prob: float):
        # False posible probability in decimal
        self.fp_prob = fp_prob

        # Size of bit array to use
        self.size = self.get_size(items_count, fp_prob)

        # Number of hash functions to use
        self.hash_count = self.get_hash_count(self.size, items_count)

        # Bit array of given size
        self.bit_array = bitarray(self.size)

        # Initialize all bits as 0
        self.bit_array.setall(0)


    def add(self, item):
        digests = []
        for i in range(self.hash_count):
            # create digest for given item.
            # i work as seed to mmh3.hash() function
            # With different seed, digest created is different
            digest = mmh3.hash(item, i) % self.size
            digests.append(digest)

            # set the bit True in bit_array
            self.bit_array[digest] = True
    
    
    def check(self, item):
        for i in range(self.hash_count):
            digest = mmh3.hash(item, i) % self.size
            if self.bit_array[digest] == False:
                # if any of bit is False then,its not present
                # in filter
                # else there is probability that it exist
                return False
        return True


    @classmethod
    # n - Number of items expected to be stored in the filter
    # p - False Positive probability in decimal
    def get_size(self, n: int, p: float):
        # Returns the size of the bit array using the formula m = -(n * lg(p)) / (lg(2)^2)
        m = -(n * math.log(p)) / (math.log(2) ** 2)
        return int(m)


    @classmethod
    # m - Size of bit array
    # n - Number of items expected to be stored in the filter
    def get_hash_count(self, m: int, n: int):
        # Return the count of hash functions needed using the formula k = (m/n) * lg(2)
        k = (m / n) * math.log(2)
        return int(k)
    

n = 2 # no of items to add
p = 0.5 # false positive probability

bloomf = BloomFilter(n,p)
print(f"Size of bit array: {bloomf.size}")
print(f"False positive Probability: {bloomf.fp_prob} %")
print(f"Number of hash functions: {bloomf.hash_count}\n")

word_present = [
            "2s","3s","4s","5s","6s","7s","8s","9s","10s","Js","Qs","Ks","As"
            "2h","3h","4h","5h","6h","7h","8h","9h","10h","Jh","Qh","Kh","Ah"
            "2d","3d","4d","5d","6d","7d","8d","9d","10d","Jd","Qd","Kd","Ad"
            "2c","3c","4c","5c","6c","7c","8c","9c","10c","Jc","Qc","Kc","Ac"
           ]

word_absent = ['bluff','cheater','hate','war','humanity',
			'racism','hurt','nuke','gloomy','facebook',
			'geeksforgeeks','twitter']

print("#1")
t0 = time.perf_counter()
for item in word_present:
	bloomf.add(item)
t1 = time.perf_counter()
print(t1 - t0)


shuffle(word_present)
shuffle(word_absent)

test_words = word_present[:10] + word_absent
shuffle(test_words)
for word in test_words:
	if bloomf.check(word):
		if word in word_absent:
			print(f"{word} is a false positive!")
		else:
			print(f"{word} is probably present!")
	else:
		print(f"{word} is definitely not present!")


print("=" * 20)
print(sys.getsizeof(word_present))
print(sys.getsizeof(bloomf))

