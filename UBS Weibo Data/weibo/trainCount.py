with open('train_label.txt', 'r') as f: 
	count = 0 
	data = f.readlines()
	for entry in data:
		count += 1
	print("Number of line: {:d}".format(count))