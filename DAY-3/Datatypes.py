Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a = 12
type(a)
<class 'int'>
b= 13.4
type(b)
SyntaxError: multiple statements found while compiling a single statement
b= 13.4
type(b)
<class 'float'>
c= 12 +4j
type(c)
<class 'complex'>
s = 'Codegnan'
id(s)
1904716291376
s +='Python'
s
'CodegnanPython'
id(s)
1904679599664
1904679599664
1904679599664
s = 'aaaaaaa'
type(s)
<class 'str'>
l = [1,2,3,4,5,5,6,]
type(l)
<class 'list'>
id(l)
1904713561728
l.append(12)
l
[1, 2, 3, 4, 5, 5, 6, 12]
id(l)
1904713561728
l = [1,12.3, 'str', [1,23]]
l
[1, 12.3, 'str', [1, 23]]
t = (l,l,l,l,l)
t
([1, 12.3, 'str', [1, 23]], [1, 12.3, 'str', [1, 23]], [1, 12.3, 'str', [1, 23]], [1, 12.3, 'str', [1, 23]], [1, 12.3, 'str', [1, 23]])
t=(1,1,1,1)
t
(1, 1, 1, 1)
t =( 1, 1.5, 'Number')
t
(1, 1.5, 'Number')
set = { 80, 20, 70, 14, 24,25, 78}
id(s)
1904716133456
a={ 1,12.3, "set"}
a
{1, 'set', 12.3}
set(s)
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    set(s)
TypeError: 'set' object is not callable
set(set)
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    set(set)
TypeError: 'set' object is not callable
se = {80, 20, 70, 14, 24,25, 78}
id(se)
1904715769312
set(se)
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    set(se)
TypeError: 'set' object is not callable
set(a)
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    set(a)
TypeError: 'set' object is not callable
se
{80, 20, 70, 25, 24, 78, 14}
student = {
"name": "Rohit",
"age": 21,
"course": "Python"
}
type(student)
<class 'dict'>
E = { "name" : "java",
      "workingdays" : 45,
      "assement": "grandtest"}
E = { "name" : "java",
      "workingdays" : 45,
      "assement": "grandtest"}
e
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    e
NameError: name 'e' is not defined. Did you mean: 'E'?
E
{'name': 'java', 'workingdays': 45, 'assement': 'grandtest'}
Log_in = true
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    Log_in = true
NameError: name 'true' is not defined. Did you mean: 'True'?
Log_in = True
type(Log_in)
<class 'bool'>
<class 'bool'>
SyntaxError: invalid syntax
T = frozenset(["Fare", "Well"])
T
frozenset({'Well', 'Fare'})
type(T)
<class 'frozenset'>
tracking_id = None
type(tracking_id)
<class 'NoneType'>
a = 10
float(a) #conversion into float
10.0
str(a)  #conversion into str
'10'
complex(a) #conversion into complex

(10+0j)
bool(a) #conversion into Boolean
True
list(a) #conversion into list
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    list(a) #conversion into list
TypeError: 'int' object is not iterable
set(a) #conversion into set
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    set(a) #conversion into set
TypeError: 'set' object is not callable
dict(a) #conversion into dictionary
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    dict(a) #conversion into dictionary
TypeError: 'int' object is not iterable
>>> b= 10.3
>>> float(b) #conversion into int
10.3
>>> int(b) #conversion into int
10
>>> complex(b) #conversion into complex
(10.3+0j)
>>> bool(b) #conversion into Boolean
True
>>> list(b) #conversion into list
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    list(b) #conversion into list
TypeError: 'float' object is not iterable
>>> set(b) #conversion into set
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    set(b) #conversion into set
TypeError: 'set' object is not callable
>>> dict(b) #conversion into dictionary
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    dict(b) #conversion into dictionary
TypeError: 'float' object is not iterable
>>> int(c) #conversion into int
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    int(c) #conversion into int
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
>>> c = 30 + 5j
>>> int(c) #conversion into int
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    int(c) #conversion into int
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
>>> float(c) #conversion into float
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    float(c) #conversion into float
TypeError: float() argument must be a string or a real number, not 'complex'
>>> boolean(c) #conversion into Boolean
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    boolean(c) #conversion into Boolean
NameError: name 'boolean' is not defined
>>> KeyboardInterrupt
>>> KeyboardInterrupt
>>> str(c) #conversion into string
'(30+5j)'
>>> list(c) # conversion into list
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    list(c) # conversion into list
TypeError: 'complex' object is not iterable
>>> dict(c) #conversion into dictionary
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    dict(c) #conversion into dictionary
TypeError: 'complex' object is not iterable
>>> set(a) #conversion into set
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    set(a) #conversion into set
TypeError: 'set' object is not callable
