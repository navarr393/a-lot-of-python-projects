 
States = [
		{'name': 'California',
		'rate' : 0.015674, \
 		'counties': [	3_175_642, 	# orange
 		 				10_039_107, # los angeles
						135_544, 	# humboldt
						137_744, 	#napa
						3_338_330 	#san diego
						 ]
		},

		{'name': 'Alaska',
		'rate' : 0.234678, \
 		'counties': [	291_826, 	# anchorage
 		 				10_039_107, # los angeles
						97_551, 	# fairbanks north
						31_276, 	# juneau
						662		 	# yakutat city and borough
						 ],
		},

		{'name': 'Debug',
		'rate' : 0.100000, \
 		'counties': [	50_000,
 		 				50_000,
						 ],
		}

]

for city in States:
	sum=0 
	for i in city['counties']:
    		sum +=i
	grant=sum*city['rate']
	f_grant="${:,.2f}".format(grant)
	print(f"Federal Grant for the state of {city['name']} is {f_grant}\n")


