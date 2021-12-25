## Task
Insert numbers 15,4,1,11,and 12 in that order (that is,ﬁrst insert 15,then insert 4,···) into a avl tree
## Sollution
```
  15
------------
  15
 /
4
------------
        15
      /
    4
  /
1
------------
Rotating
    4
  /   \
1       15
------------
    4
  /   \
1      15
      /
    11
------------
    4
  /   \
1      15
      /
    11
      \
        12
-----------
Rotating around 15
    4
  /   \
1      12
      /  \
    11    15
------------
Rotating around 4
        12
      /   \
    4      15
  /  \    
1     11      

```
