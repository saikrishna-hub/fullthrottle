import operator


# Create your models here.
# copy word_search file to your project and access with open function


count = {}
words = []
with open('word_search.tsv') as datafile:
	for row in datafile:                     # Iterate through each line of datafile
		word, usage_frequency = row.split('\t')  # split word and frequency and save them in two variables
		count[word] = int(usage_frequency.strip())  # save them as key value pairs in dictionary
		words.append(word)


# Create new function to search each letter in word
def search_here(letter):
	results = []
	for word in words:
		if letter in word:
			results.append(word)
	return results

# The results from search_here function is passed as attribute
# search_results is written by taking each element from result_space upto 25 words


def constraints(results, pending_word):
	result_space = [(result, result.find(pending_word), count[result], len(result)) for result in results]
	result_space.sort(key=operator.itemgetter(1))
	result_space.sort(key=operator.itemgetter(3))
	search_results = [result_in[0] for result_in in result_space][:25]
	return search_results
