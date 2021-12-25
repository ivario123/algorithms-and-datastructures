## Task
Insert numbers 15,4,1,11,and 12 in that order (that is,ﬁrst insert 15,then insert 4,···) into a hashtable of size 11 with hashfunction $h(x, i)=(x~mod~11 + i\cdot(1 + x~mod~10))~mod~11$
## Sollution
Standard structur
> Innan insättning
```M
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
> Efter insättning
```M
  h(15,0) = 4
  h(4,0) = 1 > Kollision
  h(4,1) = 9
  h(1,0) = 1
  h(11,0) = 0
  h(12,0) = 1 > Kollision
  h(12,1) = 4 > Kollision
  h(12,2) = 7

  [
    0 : 11
    1 : 1
    2 : 
    3 : 
    4 : 15
    5 : 
    6 : 
    7 : 12
    8 : 
    9 : 4
    10 : 
  ]

```
