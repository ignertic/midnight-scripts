from itertools import combinations
from functools import reduce

"""
 I created this script to calculate all possible shapes a Numpy array could  by taking the np.array.size argument
 **You can also specify how many combinations you want by parsing the  n_coms arg -> number of combinations

"""

#a generator could work
def find_factors(n, start=2):
	factors = []
	factor=start #use 1 just in case you need it

	while factor < n:
		res = n % factor
		if res == 0:
			factors.append(factor)
		factor +=1
	return factors

def get_combinations(n_com, product):
	valid_combinations = []

	list_of_factors = find_factors(product)
	#print(f"Found {list_of_factors}")
	comns = combinations(list_of_factors, n_com)

	try:
		while True: #to exhaust all options
			factors = list(next(comns))
			product_factors = reduce((lambda x, y : x*y), factors)
			#print(valid_combinations)
			if product_factors == product:
				#using yield can turn this into generator !!Experiment
				valid_combinations.append(factors)
	except StopIteration:
		print("StopIteration")
		return valid_combinations

print(get_combinations(2, 800)) #2->Number of combinations expected as output
#800 -> Product
