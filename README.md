# Fiels 
   file    |   content
------ | -----
exercise2.py | Conatains realisation of Lamport’s Clock
assigment.py | Conatains realisation of Vector Clock

# Possible outputs
"Possible" because of slightly different latency of print commands
## exercise2.py (Lamport’s Clock)
```
Event in proc            1 (3700)   (LAMPORT_TIME=1, LOCAL_TIME=2020-09-26 23:26:30.636124)!
Msg sent from proc       1 (3700)   (LAMPORT_TIME=2, LOCAL_TIME=2020-09-26 23:26:30.637132)
Event in proc            1 (3700)   (LAMPORT_TIME=3, LOCAL_TIME=2020-09-26 23:26:30.637132)!
Message recv at proc     2 (11592)  (LAMPORT_TIME=3, LOCAL_TIME=2020-09-26 23:26:30.702130)
Msg sent from proc       2 (11592)  (LAMPORT_TIME=4, LOCAL_TIME=2020-09-26 23:26:30.703131)
Message recv at proc     1 (3700)   (LAMPORT_TIME=5, LOCAL_TIME=2020-09-26 23:26:30.703131)
Event in proc            1 (3700)   (LAMPORT_TIME=6, LOCAL_TIME=2020-09-26 23:26:30.704118)!
Message recv at proc     3 (3488)   (LAMPORT_TIME=6, LOCAL_TIME=2020-09-26 23:26:30.709113)
Msg sent from proc       3 (3488)   (LAMPORT_TIME=7, LOCAL_TIME=2020-09-26 23:26:30.710131)
Msg sent from proc       2 (11592)  (LAMPORT_TIME=5, LOCAL_TIME=2020-09-26 23:26:30.703131)
Message recv at proc     2 (11592)  (LAMPORT_TIME=8, LOCAL_TIME=2020-09-26 23:26:30.727124)
```
## assigment.py (Vector Clock)
```
Msg sent from proc       A [0, 0, 0] -> [1, 0, 0]
Msg sent from proc       A [1, 0, 0] -> [2, 0, 0]
Event in proc            A [2, 0, 0] -> [3, 0, 0]
Message recv at proc     B [0, 0, 0] -> [1, 1, 0]
Message recv at proc     B [1, 1, 0] -> [2, 2, 0]
Msg sent from proc       B [2, 2, 0] -> [2, 3, 0]
Message recv at proc     A [3, 0, 0] -> [4, 3, 0]
Event in proc            A [4, 3, 0] -> [5, 3, 0]
Event in proc            A [5, 3, 0] -> [6, 3, 0]
Msg sent from proc       C [0, 0, 0] -> [0, 0, 1]
Message recv at proc     B [2, 3, 0] -> [2, 4, 1]
Event in proc            B [2, 4, 1] -> [2, 5, 1]
Msg sent from proc       B [2, 5, 1] -> [2, 6, 1]
Message recv at proc     A [6, 3, 0] -> [7, 6, 1]
Message recv at proc     C [0, 0, 1] -> [2, 7, 2]
Msg sent from proc       B [2, 6, 1] -> [2, 7, 1]
Final state: A [7, 6, 1]
Event in proc            C [2, 7, 2] -> [2, 7, 3]
Message recv at proc     C [2, 7, 3] -> [2, 8, 4]
Final state: C [2, 8, 4]
Msg sent from proc       B [2, 7, 1] -> [2, 8, 1]
Final state: B [2, 8, 1]
```