class PriorityQueue:

	def __init__(self):
		self.first = []
		self.business = []
		self.economy = []

	def isEmpty(self):
		return self.items == []

	def enqueue(self, item, priority):
		self.priority = priority
		if self.priority == '1':
			self.first.append(item)
		elif self.priority == '2':
			self.business.append(item)
		elif self.priority == '3':
			self.economy.append(item)

	def dequeueAll(self):
		while (self.first != []):
			print(self.first.pop(), end = '')
		while (self.business != []):
			print(self.business.pop(), end = '')
		while (self.economy != []):
			print(self.economy.pop(), end = '')

	def dequeueFirstClass(self):
		return self.first.pop()

	def dequeueBusinessClass(self):
		return self.business.pop()
	
	def dequeueEconomyClass(self):
		return self.economy.pop()

def main():
	AirFlightReservation = PriorityQueue()

	while(True):
		passenger = input()
		if (passenger == "done"):
			break
		else:
			AirFlightReservation.enqueue(passenger, passenger[-2])

	AirFlightReservation.dequeueAll()

main()
input("\nEnter a key to exit.\n")