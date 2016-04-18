#!/usr/bin/python  
import json
import sys
import unicodedata
# Read all lines from stdin
for line in sys.stdin:
	try:
		# Parse the JSON
		data = json.loads(line)
		# Emit every field
		for field in data.keys():
			# Emit every field and subfields
			real = field
			print "%s" % (real) 
			if type(data[field]) is dict:
				for subfield in data[field]:
					subreal = subfield
					print "%s:%s" % (real, subfield)
					if type(data[field][subfield]) is dict:
						for subsubfield in data[field][subfield]:
							print "%s:%s:%s" % (real, subfield, subsubfield)
							if type(data[field][subfield][subsubfield]) is unicode:
								print "%s:%s:%s:%s" % (real, subfield, subsubfield, data[field][subfield][subsubfield])
					elif type(data[field][subfield]) is unicode: 
						print "%s:%s:%s" % (real, subfield, data[field][subfield])
			elif type(data[field]) is int:
				print "%s:%s" % (real, data[field])
			elif type(data[field]) is float:
				print "%s:%s" % (real, round(data[field]))
			elif type(data[field]) is bool:
				print "%s:%s" % (real, data[field])
			elif type(data[field]) is list:
				print "%s:%s" % (real, data[field])
			elif type(data[field]) is unicode:
				if field == 'city':
					print "%s:%s" % (real,unicodedata.normalize('NFKD', data[field]).encode('ascii', 'replace'))
				if field == 'full_address':
					pass #on n'utilise pas l'adresse car ville et latiude / longitude suffit
				if field == 'state':
					print "%s:%s" % (real,data[field])
				if field == 'type':
					print "%s:%s" % (real,data[field])
	except ValueError:
		# Log the error so we can see it
		sys.stderr.write("%s\n" % line)
		exit(1)
