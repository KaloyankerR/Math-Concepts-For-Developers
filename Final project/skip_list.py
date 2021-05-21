import random


class Node(object):
	def __init__(self, key, level):
		self.key = key
		self.forward = [None]*(level+1) # list to hold references to node of different level


class SkipList(object):
	def __init__(self, max_lvl, P):
		self.MAXLVL = max_lvl 		# Maximum level for this skip list
		self.P = P # P is the fraction of the nodes with level i references also having level i+1 references
		self.header = self.createNode(self.MAXLVL, -1) # create header node and initialize key to -1
		self.level = 0 # current level of skip list
    
    
	def createNode(self, lvl, key): # creates a new node
		n = Node(key, lvl)
		return n
	
	
	def randomLevel(self): # creates random level for node
		lvl = 0
		while random.random() < self.P and lvl < self.MAXLVL:lvl += 1
		return lvl


	def insertElement(self, key): # inserts given key in the skip list
		update = [None]*(self.MAXLVL+1) # create update array and initialize it
		current = self.header
        
		for i in range(self.level, -1, -1):
			while current.forward[i] and \
				current.forward[i].key < key:
				current = current.forward[i]
			update[i] = current

		current = current.forward[0]

		if current == None or current.key != key:
			# generates a random level for node
			rlevel = self.randomLevel()

			if rlevel > self.level:
				for i in range(self.level+1, rlevel+1):
					update[i] = self.header
				self.level = rlevel

			n = self.createNode(rlevel, key) # create new node with random level generated
            
            # inserts the node by rearranging references
			for i in range(rlevel+1):
				n.forward[i] = update[i].forward[i]
				update[i].forward[i] = n
			# print(f"Successfully inserted key {key}")
            
                    
	def deleteElement(self, search_key):
		update = [None]*(self.MAXLVL+1) # creates an update array and initialize it
		current = self.header

		for i in range(self.level, -1, -1):
			while(current.forward[i] and \
				current.forward[i].key < search_key):
				current = current.forward[i]
			update[i] = current

		current = current.forward[0]

		# If current node is target node
		if current != None and current.key == search_key:
			for i in range(self.level+1):
				if update[i].forward[i] != current:
					break
				update[i].forward[i] = current.forward[i]

			# Removes levels having no elements
			while(self.level>0 and\
				self.header.forward[self.level] == None):
				self.level -= 1
			print("Successfully deleted {}".format(search_key))

	def searchElement(self, key):
		current = self.header
        
		for i in range(self.level, -1, -1):
			while(current.forward[i] and\
				current.forward[i].key < key):
				current = current.forward[i]

		# reached level 0 and advance reference to
		# right, which is prssibly our desired node
		current = current.forward[0]

		# If current node have key equal to
		# search key, we have found our target node
		if current and current.key == key:
			print("Found key ", key)
   

	# Display skip list level wise
	def displayList(self):
		print("\n*****Skip List******")
		head = self.header
		for lvl in range(self.level+1):
			print("Level {}: ".format(lvl), end=" ")
			node = head.forward[lvl]
			while(node != None):
				print(node.key, end=" ")
				node = node.forward[lvl]
			print("")
