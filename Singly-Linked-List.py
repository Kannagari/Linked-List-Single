from random import randint


#Node class defining the structure of a single node of the linked list
#Assigns the passed data value to the Node being created
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

#Singly Linked List class, containing constructor and various member functions
class SLL:
	#Constructor which initializes the head to point to Null, and the size of the list to be 0
	def __init__(self):
		self.head = None
		self.size = 0

	#Print Helper function to display the contents of the list
	def printList(self):
		if self.head == None: #If the list is empty, simply return because there is nothing to print
			return
		temp = self.head #Otherwise, create a walker and point it at the head of the list
		while temp is not None: #While the walker is not pointing at null
			print(temp.data, end="->") #Print the current nodes data
			temp = temp.next #Walk the walker forward
		print("Null", end='\n\n') #Print Null once the end of the list is reached

	#Function to insert at the beginning of the list
	def insertAtBeginning(self, data):
		print("Inserting a node with value", data, "at the beginning of the list.")
		if self.head is None: #If the list is currently empty
			newNode = Node(data) #Create a new node with the passed data value
			self.head = newNode #Declare the new node to be the head of the list
		else:
			newNode = Node(data) #Otherwise, create a new node with the passed value
			newNode.next = self.head #Assign newNode's next to be head's current position
			self.head = newNode #Update head's location to the newly created node
		self.size = self.size + 1 #Increase size of the list

	#Function to insert in the middle of the list
	def insertInMid(self, data):
		print("Inserting a node with value", data, "in the middle of the list.")
		if self.head is None: #Check if the list is empty, starting the list if it is
			newNode = Node(data)
			self.head = newNode
		else:
			steps = (self.size) // 2 #Otherwise, divide the size of the list by 2 (rounding down) to find the middle
			temp = self.head #Create a walker, point it at the head of the list
			i = 0 #Variable for counting steps
			while i < steps - 1: #steps - 1 because we want to be one node *before* the location we want to insert at
				temp = temp.next #Walk the walker along, incrementing i as it walks
				i = i + 1
			newNode = Node(data) #Create a new node with the data passed
			newNode.next = temp.next #Insert the new node after the walker, essentially taking the walkers place
			temp.next = newNode #Make the walker point to the newly added node
		self.size = self.size + 1 #Increase size of the list

	#Function for inserting at the end of the list
	def insertAtEnd(self, data):
		print("Inserting a node with value", data, "at the end of the list.")
		if self.head is None: #Check if the list is empty, starting it if it is
			newNode = Node(data)
			self.head = newNode
		else:
			temp = self.head #Otherwise, create a walker, point it at the head of the list
			while temp.next: #While temp.next exists
				temp = temp.next #Walk along the list, this will leave us at the last node in the list
			newNode = Node(data) #Create a new node with the passed data
			temp.next = newNode #Insert it after temp
		self.size = self.size + 1 #Increase the size of the list

	#Function for finding a node with the passed data value, and deleting it, if found
	def delete(self, data):
		print("Attempting to delete node with value", data)
		prev = None #Create a pointer for the previous node, initializing it to null
		temp = self.head #Create a walker and point it at the head of the list
		if self.head is None: #If the list is empty, there is nothing to delete, so return
			print("The list is empty!", end='\n\n')
			return
		while temp: #While temp is not null
			if temp.data == data: #If we find the node with the data we are looking for
				if prev: #If prev exists, we know the node we want to delete is not the head
					prev.next = temp.next #So prev.next is set = to temp.next, essentially deleting temp's current node from the list
					self.size = self.size - 1 #Reduce the size of the list
					print("Successfully deleted")
					return
				else: #Otherwise, if prev is still null, we know the node we want to delete is the head
					self.head = temp.next #So we move head to the next node in the list
					self.size = self.size - 1 #Reduce the size of the list
					print("Successfully deleted")
					return
			prev = temp #Move prev up to the current location of temp
			temp = temp.next #Move temp onto the next node

		print(data, "was not found in the list!") #If we make it through all the checks and don't find our value, then we can say it was not in the list

	#Function to remove duplicate values from the list
	def removeDup(self):
		print("Attempting to remove duplicates from the list")
		if self.head is None or self.size == 1: #If the size of the list is < 1, it cannot have duplicates
			print("The list is not big enough to contain duplicates!", end='\n\n') #So we print that and return
			return
		Uni = [] #Create a list to hold unique values
		prev = None #Create a pointer and initialize to null
		temp = self.head #Create a walker and initialize to the head of the list
		while temp: #While the walker is on a node that is not null
			if temp.data in Uni: #If the current nodes data is already in the list of unique values
				prev.next = temp.next #We remove that node from the list
				self.size = self.size - 1 #Decrease the size
			else:
				Uni.append(temp.data) #Otherwise, we add this nodes value to the list of unique values
			prev = temp #Update the prev pointer
			temp = temp.next #Update the walker
		print("Duplicates successfully removed")



def main():
	List = SLL() #Create an instance of the SLL class

	print("The current size of the list is", List.size)
	List.removeDup() #Show that no duplicates can be removed from an empty list
	List.delete(6) #Show that nothing can be deleted from an empty list

	for i in range(0, 5): #Generate 5 random number between 0 and 100
		List.insertAtBeginning(randint(0, 100)) #Insert the random numbers at the beginning of the list
		List.printList() #Print the list to watch it grow

	print("The current size of the list is", List.size, end='\n\n')


	for i in range(0, 5):
                List.insertInMid(randint(0, 100)) #Again, generate 5 random numbers, this time inserting in the middle of the list
                List.printList() #Print list to observe growth

	print("The current size of the list is", List.size, end='\n\n')


	for i in range(0, 5):
                List.insertAtEnd(randint(0, 100)) #Lastly, generate 5 random numbers, inserting at the end of the list
                List.printList() #Print list to observe growth


	print("The current size of the list is", List.size, end='\n\n')


	List.delete(300) #Try to delete a value we know will not be in the list, to prove our function will not delete what is not there 
	List.printList() #Print list to observe effect

	print("The current size of the list is", List.size, end='\n\n')


	List.insertInMid(125) #Insert a known value so we can test a successful deletion case
	List.printList()

	print("The current size of the list is", List.size, end='\n\n')


	List.delete(125) #Attempt to delete known value
	List.printList()

	print("The current size of the list is", List.size, end='\n\n')


	#Insert two identical values to test removeDup method
	List.insertAtBeginning(200)
	List.printList()
	List.insertAtEnd(200)
	List.printList()

	print("The current size of the list is", List.size, end='\n\n')


	List.removeDup()
	List.printList()

	print("The current size of the list is", List.size, end='\n\n')


if __name__ == '__main__':
	main()
