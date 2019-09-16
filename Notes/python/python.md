## introduction

	- Test the compiler

## Dictionary
 	- new value = dict[key] = value
	- update dict = dict.update({key:value})
	- del value = del dict[key] 
	- pop value = dict.pop(key)
	- iterate with tuples = dict.items()
	- iterate on keys views  = dict.keys()
	- iterate on value views = dict.values()
	- get value with None default = dict.get(key)
	- get value with custom value = dict.get(key,custom)
	- compare dictionarys = dict1 == dict2
	- check it key in dictionary = key in dict
	- sort the tuples of key, value = sorted(dict.items())
	
## Collections 
	- count hashable objects - Counter

## Sets 
	- unordered collection of unique values 
	- len of the set - len(set)
	- in to verify contains - val in set 
	- can be initiated - Set(iterable)
	- empty set - Set()
	- only immutable objects are hashable 
	- Comparing sets - set1 == set2
	- check subset - setl.issubset(set2)
	- union set - set1 | set2
	- union set - set1.union(set2)

```python 
#Dictionary example
ipython gradesdict.py

test = ( 'hello world'
	'python 3')
# Above is a single string 

from collections import Counter 
counter = Counter(text.split())
# summarized dictionarys with key and value 
for word,count in sorted(counter.items()):
	print(f'{word:<12}{count}')

#spaces in print with left 4 characters   
print(f'{key:<4}{count}')

#Sets syntax 
colours = {'red','orange','yellow','green','red'}
```


