( pseudo code )
Exo 1 Histogramme : 

\# map

```
for key in list : 
	list[key][1] = int(log(pop(line[key][1])))
repartition = {}
for key in list :
	repartition[list[key][1]][1] = 0;
```

\# reduce

```
for key in list :
	repartition[list[key][1]][1] += 1
```


( pseudo code )
Exo 2 moyenne :

\#map

```
temp = {}
for year in list :
	temp[year][1] = []
for year in list :
	temp[year].append(list[year][temp])
```

\#reduce

```
for year in temp :
	temp[year][1] = sum(temp[year][1])
```

