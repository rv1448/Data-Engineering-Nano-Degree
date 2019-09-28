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
	- random array in numpy - np.random.randint(1,7,600000)
	- function on arrays - np.array().sum(), mean(),min()
	- mean across columns - np.array().mean(axis=0)
	- square root of the array - np.sqrt()
	- View to create a copy - array.view
	- physical copy(shallow) of the data - array.copy()
	- physical copy(deep) of the data - array.deepcopy()
	-
* Numpy array generation 
```python
## Generate randome ints between 10 and 60 and total of 5
np.random.randint(10,60,5)
## Generate floats between 1.1 and 5.5 
np.linspace(1.1,5.5,5)
## Generate range of numbers 
np.arange(10,40,2)
```

* Indexing and slicing in numpy 
```
grades =[[95 96 93]
 	[93 90 90]
 	[90 95 95]
 	[98 96 92]]
grades[0,1] ==> r:0,c:1
grades[1]   ==> r:1
grades[0:2] ==> r:0,1
grades[:,1] ==> all rows and 1 column
# continuous no square brackets
```
* re-sizing array
	- to make permanent changes - array.resize()
	- to flatten(deep copy) the array to one dimension - array.flatten()/ravel()
	- tranpose an array - array.T

* pandas 
	*one dimensional - Series* 
	*two dimension - Pandas*
series
------
[series](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.html)
	- count of the series - series.count()
	- mean of the series - series.mean()
	- all the descriptive stats - series.describe()
```python
import pandas 
grades = pd.Series([70,89,90])
grades = pd.Series([70,89,90],index=['1','2','3'])
```

** dictionary
``` 
grades_dict = {'willy':[90,87,65],'roe':[98,76,62]}
data = pd.DataFrame(grades_dict)
print(data)
```
	- select values for named indices of the row - DataFrame.loc['nameofrow'] 
	- iloc and loc brings the rows 
	- iloc uses number/integer rows and loc used named indexes
	- Change a value at a index - DataFrame.iat[2,0]
	- Change a value at a named index - DataFrame.at['idx','eva']
	- Set options to the DataFrame - pd.set_option('precision',2)
	- Sort dataFrame using index - DataFrame.sort_index(ascending=False)
	- Sort dataFrame using values - DataFrame.sort_value(by='test1',ascending=False) 
```python
#inplace Sort
grades.sort_values(by='test1',ascending=False,inplace=True)
#self check: 
Convert dictionary to DataFrame 
Select only column name mon and tues
Using row index select low tempuratues of each day 
set floating point precision to 2, Then caliculate the average temp of the day 
Calculate average High and low
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
	- find the function definition in ipython - ??  

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

* Strings
[String formating](https://docs.python.org/3.4/library/string.html#string-formatting)

```python
#String formatting 
print(f'{17.98:.2f}')
f'{10:d}'
f'{65:c}{97:c}'
#if no format is specified it is treated as string
f'{37:10d}'
f'{12334556:,d}'

#Old code 
':.2f'.format(17.489)
'{} {}'.format('Amanda','Cyan')
'{0},{0},{1}'.format('happy','world!')
```
	- count number of occurances a word occurs in string - 'string'.count()/'string'.count('',int)
	- get the index of a character in a string - 'string'.index()
	- get the right index - 'string'.rindex('at')
	- check if string starts with character - 'string'.startswith('')
	- replace a character in string - 'string'.replace('\t',',')
	- split the letters by a character - 'string'.split(', ') ==> return list
	- join using a char for every element in the Sequence - ', '.join([seq])
[String functions](https://docs.python.org/3/library/stdtypes.html)

Regex
-----

`REGEX: [] {} () \ * + ^ $ ? . |`
#### * - Zero or more occurances of a character
#### + - atleast one 
#### ^ is the start of the string $ is the end of the string 
#### + and * are Greedy quantifiers 
	- replace a character in a string - re.sub()
	- remove Zero or more space re.split(r',\s*',',','1,    5,6, 6,   9,   0')
	- Find all that matches to the pattern - re.findall(pattern,String)
	- Iterate through all the matches - re.iter()

* Files
```python
with open('accounts.txt',mode='w') as accounts:
with open('account.txt',mode='r') as accounts: 
```
[DataSets](http://vincentarelbundock.github.io/Rdatasets/datasets.html)

