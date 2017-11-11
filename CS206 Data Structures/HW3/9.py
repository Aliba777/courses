counter = 1
def move_tower(height, from_pole, to_pole, temp_pole):
	global counter
	if height >= 1:
		move_tower(height - 1, from_pole, temp_pole, to_pole)
		print(counter, end = ' ')
		move_disk(from_pole, to_pole)
		counter += 1
		move_tower(height - 1, temp_pole, to_pole, from_pole)
def move_disk(fp, tp):
	print("moving disk from", fp, "to", tp)
n = int(input("Please, enter the number of disks: "))
move_tower(n, "Original Pole", "Final pole", "Temporary pole")

input("Please, press Enter to continue")