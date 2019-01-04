# TAXONOMY PROBLEM

The problem is given in the Taxonomy_Problem.pdf file. 

### How to write the input file:

      1. Write 0, then shift by a horizontal tab, then provide the no. of nodes
         where no. of nodes is equal to the no. of taxonomy levels here 
      
      2. Write 1, then shift by a horizontal tab, then provide the information on edge dependencies
         which is parent node, then shift by a horizontal tab, then child node. Repeat this for all 
         the childs in separate lines. 
      
      3. Write 2(or anything else other than 0 and 1), then shift by a horizontal tab, then provide the 
         information on the nodes where information on nodes means the name of the node followed by the 
         no. of reads with a horiztonal tab shift in between. 

   
### History: 
Previously, I wrote a code which had the taxonomical input hardcoded, but to make it tolerant to 
taxonomical variations,we have to modify the input file accordingly, hence we need to put <1> and <2> 
in the input file. 

### Limitation: 
_We can't take more than 26 nodes in this form of code. We'll have to modify it_
