import subprocess
"""
data = subprocess.check_output(["netsh", "wlan", "show", "profiles"]).decode("utf-8").split("\n")

profiles = [i.split(":")[1][1:-1] for i in data if "All User Profiles" in i]
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None
        
    def inOrder(self, root):
        global arr
        if root:
            self.inOrder(root.left)
            arr.append(root.data)
            self.inOrder(root.right) 
        return arr
        
def getNode(data):
    node = Node(data)
    return node

flag = True
def populateTree(node, arr):
    mid = len(arr)//2
    if not isinstance(node, Node):
        node = getNode(node)
    print(str(node.data) + "->", end="")
    if not arr or arr==[]:
        return
    elif len(arr)==1:
        node.left = arr[0]
    else:
        node.left = arr[0]
        node.right = arr[1]
        populateTree(node.left, arr[2:mid])
        populateTree(node.right, arr[mid+1:len(arr)])
"""   
for i in profiles:
    result = subprocess.check_output(["netsh", "wlan", "show", "profile", i, "key=clear"]).decode("utf-8").split("\n")
    results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
    
    try:
        print("{:<30}| {:<}".format(i, results[0]))
    except IndexError:
        print("{:<30}| {:<}".format(i, ""))
"""  
if __name__=="__main__":
    arr = list()
    root = getNode(1)
    root.left = getNode(2)
    root.right = getNode(3)
    root.left.left = getNode(4)
    root.left.right = getNode(5)  
    root.right.left = getNode(6)
    root.right.right = getNode(7)    
    arr = root.inOrder(root)
    for node in arr:
        print(node, end="->")
    
    """
    1    1 - 2 - 3 - 4 - 5 - 6 -7 
   / \
  2   3
 / \ / \
4   6 7  8
/    \
9    10
"""