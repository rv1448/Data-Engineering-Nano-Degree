## introduction

	- 

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
	- intersection set - set1 & set2
	- intersection set - set1.intersection(set2)
	- difference set - set1 - set2 
	- difference set - set1.difference(set2)

## Numpy
``` import numpy as np
```
* ndarrays
[numpybasics](https://docs.scipy.org/doc/numpy/user/basics.types.html)
[magiccommands](https://ipython.readthedocs.io/en/stable/interactive/magics.html)
	- datatype of the array - array.dtype
	- number of dimension - array.ndim
	- shape of the array - array.shape
	- rows vs  columns - array.shape
	- size of each element - array.itemsize
	- size of the array rows * col - array.size
	- range in array - array.arange(5) or arange(5,10)
	- floating point range - np.linspace(0.0,1,num=5)
	- reshaping a array - np.arange(1,21).reshape(4,5)
``` python
#create an array of 20 even numbers from 2 through 40 and reshape into (4,5) array
np.arange(2,41,2).reshape(4,5)

#list vs array

```
* pandas 
	- one dimensional - Series 
	- two dimension - Pandas 

```
np.array([1,2,3,4,5,6,7])
np.array([[1,2,3],[4,5,6]])
```


## Dynamic Visualization
* FuncAnimation
* scriptname: `scriptname`

## visualization 
``` import seaborn as sns
    import matplotlib.pyplot as plt 
```
	- set white grid stylefor the plot - sns.set_style('whitegrid')
	- 
## Special notes 
```import sys
```
	- find the space seperated values - sys.argv[n]
	- 

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


