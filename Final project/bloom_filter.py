# Install mmh3 and bitarray 3rd party module first
# How to install mmh3 -> pip install mmh3
# How to install bitarray 3rd party module -> pip install bitarray
from random import shuffle
import math
import mmh3
from bitarray import bitarray
import time
import sys
import matplotlib.pyplot as plt

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
    
    
    def add_items_from_list(self, list_items: list):
        for item in list_items:
            self.add(item)
    
    
    def check(self, item):
        for i in range(self.hash_count):
            digest = mmh3.hash(item, i) % self.size
            if self.bit_array[digest] == False:
                # if any of the bits is False then,its not present in the filter
                # else there is probability that it exist
                return False
        return True
    
    
    def plot_sizeof_data_structures_compared_to_a_normal_list(self, list_items: list):
        list_structure = []
        bloom_filter_structure = BloomFilter(len(list_items), self.fp_prob)
        
        for item in list_items:
            list_structure.append(item)
            bloom_filter_structure.add(item)
        
        bloom_filter_size = sys.getsizeof(bloom_filter_structure)
        list_strucutre_size = sys.getsizeof(list_structure)
        
        data_structures = ["Bloom Filter", "Normal list"]
        height = [bloom_filter_size, list_strucutre_size]
        
        plt.bar(data_structures, height, width = 0.8, color = ['red', 'green'])
        plt.xlabel('Data Structures')
        plt.ylabel('Bytes')
        plt.title('Space usage')
        plt.show()
    
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
    
    
    def __repr__(self):
        representation = f"Size of bit array: {self.size}\nFalse positive Probability: {self.fp_prob} %\nNumber of hash functions: {self.hash_count}\n"
        return representation
