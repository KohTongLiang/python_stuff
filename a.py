import Queue
from random import randint
# from decimal import Decimal

# instantiate queue
q = Queue.Queue()
no_answer_q = Queue.Queue()

# ask for names
answer_count = 0
no_answer_count = 0
correct = 0
wrong = 0

num = 1
for x in range(5):
	shopper_name = raw_input("Shopper " + str(num) + ":\n")

	# shopper's queue in first come first serve basis
	q.put(shopper_name)
	num += 1

# print queue name
print("\n")

num = 1
while not q.empty():
	# print shoppers name, at the same time de-queue the shopper
	shopper = q.get()
	print "Shopper " + str(num) + ": " + shopper + "\n"
	num += 1
	# status of phonecall
	status = randint(1,2)
	if status == 1:
		answer_count += 1
		answer_given = randint(1,2)

		# check if shopper answered correctly
		if answer_given == 1:
			print("\n" + shopper + " answered correctly.")
			correct += 1
		elif answer_given == 2:
			print("\n" + shopper + " answered incorrectly.")
			wrong += 1

	elif status == 2:
		# shopper rejoins queue
		no_answer_q.put(shopper)


# print final statistics
print("\nAll shoppers who failed to answer the call and are still in queue:")
no_answer = 0
while not no_answer_q.empty():
	print "\n" + no_answer_q.get()
	no_answer += 1

print("\n\nNumber of shoppers who failed to answer:")
print(str(no_answer))

total = correct + wrong

correct = int(correct)
wrong = int(wrong)

print("\n\nNumber of shoppers who picked up call and answered correctly:")
print(str((correct * 100) / total) + "%")

print("\n\nNumber of shoppers who picked up call and answered incorrectly:")
print(str((wrong * 100) / total) + "%")

