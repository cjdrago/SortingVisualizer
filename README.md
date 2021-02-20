# Sorting Visualizer
### Poroject description
The sorting visualizer project goal is to show explicitly to users the difference between five different sorting algorithms: ***Selection Sort, Bubble Sort, Insertion Sort, Coctail Sort and Quick Sort***.

<br>

To show those algorithms, I selected three different visualization forms: wide bars (*sorting array has smaller length*), thin bars (*sorting array has a great amount  of items*) and color (*more fun way to observe the sorting process*).

<br>

Also, at the end of every sorting process you can run again, see the time that took to the algorithm to sort and its name. 

### Sorting algorithms description (*geeksforgeeks.org*)

1. [Bubble sort](https://www.geeksforgeeks.org/bubble-sort/)
2. [Insertion Sort](https://www.geeksforgeeks.org/insertion-sort/)
3. [Seleciton Sort](https://www.geeksforgeeks.org/selection-sort/)
4. [Quick Sort](https://www.geeksforgeeks.org/quick-sort/)
5. [Cocktail Sort](https://www.geeksforgeeks.org/cocktail-sort/)

### Program issues

This section is a 'To Do list' whith bugs that need to be solved.

- [ ] When you select an algorithm, select what you want to sort and after that (followin that sequence) you change the algorithm there is a bug described as: 
        
        TypeError: 'NoneType' object cannot be interpreted as an integer

- [ ] When you execute color sorting, ther is a bug in the status section: ***"Status: Sorted!!"*** overlaps ***"Status: Sorting..."***

- [ ] When bar sorting is selected, i want to show which bar i am going to sort (light blue bar), it only hapens at the following algortithms: 
    - Selection sort 
    - Insertion Sort 
    - Quick Sort 
