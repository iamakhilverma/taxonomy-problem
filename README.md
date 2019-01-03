# TAXONOMY PROBLEM
## 1. Generate a classification report based on this taxonomy.
1. Definition of taxonomy:

   A taxonomy consists of a set of terms organized in a hierarchical manner. Here we are dealing with a taxonomy of alphabets    that are organized as shown in Figure 1.
2. List of reads classified into taxonomy levels:

   We have a list of terms and a number of "reads" classified into each term. This will be used as the input file in our task
   Classification of 1000 reads.   
3. Task:

   |Taxonomy level ---|--- |---Number of reads
   |G        ---   |  --- |--- 100|
L               50
N               50
Y               300
Z               250
V               250

Write a program to generate a classification report given an input file with taxonomy level and number of reads separated by a tab.

>The classification report will show the total number of "reads" that fall under a certain term in the taxonomy. The number of "reads" under a terms has to be greater than 1 to be shown in the output. The terms must be ordered in the same order as the depth in the taxonomy.
3.1 Example input file
Z    100
V    100
X    200
3.2 Example output
A    400
D    400
G    400
L    400
Q    400
T    400
X    200
V    200
Z    100
3
