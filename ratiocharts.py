# generation of "ratio" charts, such as histograms or pie charts

# counts the occurrence per value for certain attributes
# (like a histogram)

MULTIPLE=10000

# we get a list of fieldnames as input, so we scan the file
# only once.
def count(reader, fieldnames):
	print("displayed number is number of read rows /",MULTIPLE)
	print("the dot is a new value found")
	ret = {}
	for fieldname in fieldnames:
		ret[fieldname] = {}
	i = 0
	for row in reader:
		i += 1
		for fieldname in fieldnames:
			curr_val = row[fieldname]
			if curr_val not in ret[fieldname].keys():
				print('.',end="",flush=True)
				ret[fieldname][curr_val] = 1
			else:
				ret[fieldname][curr_val] += 1
			if (i % MULTIPLE) == 0:
				print(int(i / MULTIPLE))
	return ret

def create_charts(reader):
	print(count(reader,["visitor_location_country_id"]))
