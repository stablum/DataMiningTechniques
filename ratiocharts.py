# generation of "ratio" charts, such as histograms or pie charts

# libraries imports
import pylab

MULTIPLE=10000

# 1% : counter's entries that are below this are collapsed into "other"
INSIGNIFICANT_TRESHOLD=0.01

# fields to be plotted as pies
PLOTFIELDS = [
	"visitor_location_country_id",
	"prop_country_id",
	"srch_destination_id",
	"promotion_flag",
	"price_usd",
	"srch_length_of_stay",
	"price_usd"
]

# we get a list of fieldnames as input, so we scan the file
# only once.

# counts the occurrence per value for certain attributes
# (like a histogram)
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
				# found this value for the first time! print dot.
				print('.',end="",flush=True)
				ret[fieldname][curr_val] = 1
			else:
				# have found this value before, increment its counter
				ret[fieldname][curr_val] += 1
		if (i % MULTIPLE) == 0:
			# let's give an idea of how many rows are being processed
			print(int(i / MULTIPLE))
	return ret

# total count (actually, it should be simply the number of rows)
def calculate_total(counter):
	ret = 0
	for field_value, count in counter.items():
		ret += count
	return ret

# to calculate the 'others' slice that is typical of pie charts
def collapse_insignificant(counter):
	total = calculate_total(counter)
	ret = counter.copy()
	others = 0
	for field_value, count in counter.items():
		frac = count/total
		print(field_value,"is insignificant, with count:",count,"and fraction:",frac)
		if frac < INSIGNIFICANT_TRESHOLD:
			# it's insignificant, let's add it to the 'others' category
			others += count
			del ret[field_value] # let's get rid of it
	if others > 0:
		ret['others'] = others
	return ret

def plot_pie(counter, title, filename):

	counter = collapse_insignificant(counter)
	print("counter for",title,"has number of keys:",len(counter.keys()))
	# make a square figure and axes
	pylab.figure(1, figsize=(6,6))
	ax = pylab.axes([0.1, 0.1, 0.8, 0.8])

	# The slices will be ordered and plotted counter-clockwise.
	labels = counter.keys()
	fracs = [ count for field_value,count in counter.items() ]

	pylab.pie(fracs, labels=labels,
	                autopct='%1.1f%%', shadow=False, startangle=90)
	                # The default startangle is 0, which would start
	                # the Frogs slice on the x-axis.  With startangle=90,
	                # everything is rotated counter-clockwise by 90 degrees,
	                # so the plotting starts on the positive y-axis.

	pylab.title(title, bbox={'facecolor':'0.8', 'pad':5})
	pylab.savefig(filename, bbox_inches='tight')
	pylab.close()

def create_charts(reader):
	aggregates = count(reader,PLOTFIELDS)
	for fieldname in aggregates.keys():
		filename = "pie_"+fieldname+".png"
		plot_pie(aggregates[fieldname],fieldname,filename)
