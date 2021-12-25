## Task
Insert numbers 15,4,1,11,and 12 in that order (that is,ﬁrst insert 15,then insert 4,···) into a hashtable of size 11 with hashfunction $h(x)=x~ mod ~11$
## Sollution
Standard structur
```
  [
    0 :
    1 : 
    2 : 
    3 : 
    4 : 
    5 : 
    6 : 
    7 : 
    8 : 
    9 : 
    10 : 
  ]

```
Efter insättning
```
  h(15) = 4
  h(4) = 4
  h(1) = 1
  h(11) = 0
  h(12) = 1
  [
    0 : 11
    1 : 1,12
    2 : 
    3 : 
    4 : 15,4
    5 : 
    6 : 
    7 : 
    8 : 
    9 : 
    10 : 
  ]

```