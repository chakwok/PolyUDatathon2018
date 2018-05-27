with open('ProvinceId.txt', 'r') as f, open('ProvinceId.csv', 'w') as o:
	ProvinceIdDict = {} 
	lines = f.readlines() 
	defaultList = [10,	8,	9,	0,	4,	11,	12,	1,	6,	5,	7,	3, 2]

	for line in lines :
		info = line.split('\t')
		if (info[0] not in ProvinceIdDict):
			ProvinceIdDict[info[0]] = [info[1].strip()]
		else:
			ProvinceIdDict[info[0]].append(info[1].strip())

	#(print(ProvinceIdDict))
	for key, value in ProvinceIdDict.items():
		if (len(value) != 13):
			for ele in defaultList: 
				if (str(ele) not in value):
					value.append(str(ele))


	o.write('ProvinceId_CityId, Rank_1, Rank_2, Rank_3, Rank_4, Rank_5, Rank_6, Rank_7, Rank_8, Rank_9, Rank_10, Rank_11, Rank_12, Rank_13\n')
	for key, value in ProvinceIdDict.items():
		str = ('{:s}, '.format(key))
		count = 0
		while (count != len(value) - 1):
			str = str + ('{:s}, '.format(value[count]))
			count +=1
		str = str + ('{:s} \n'.format(value[count]))

		o.write(str)