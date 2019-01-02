#created by Akhil. Git username <iamakhilverma>

import copy
import string

#file is opening
content = open('input.txt', 'r').readlines()

adj = [] # adjacency list to store the edge information

for line in content:    
    # if edge is on-way
    if line[0] == '0': # 0 command is for giving the number of nodes
    	u, v = line.strip().split(' ')
    	numNodes = int(v)
    	values = [0 for i in range(numNodes)]
    	adj = [[] for i in range(numNodes)]
    elif line[0] == '1': # 1 command is for giving the information on edge dependencies
    	a, u, v = line.strip().split(' ')
    	adj[ord(u) - ord('A')].append(ord(v) - ord('A'))
    else: # this command is for giving the information on the value of nodes
    	a, u, v = line.strip().split(' ')
    	values[ord(u) - ord('A')] = int(v)

# running DFS to calculate the value of nodes
visited = [False for i in range(numNodes)]
answerList = []



def dfs(node):
	visited[node] = True
	answer = 0
	tempadj = copy.deepcopy(adj[node]) #to not change the main adj list
	tempadj.sort( key=numChild, reverse=True)
	# print(tempadj)
	for child in tempadj:
		answer = answer + dfs(child)
	answer = answer + values[node]
	#storing the answer to later print in the sorted form
	answerList.append((node, answer))
	return answer

# used as a comparator for sorting function
def numChild(node):
	return len(adj[node])	



if __name__ == "__main__":
	_ = dfs(0) #return value not required
	#printing the answer
	for alp, val in answerList[::-1]:
		if (val != 0):
			print(str(unichr(65+alp))  + '\t' + str(val))



