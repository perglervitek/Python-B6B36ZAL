graf = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "D": ["E"],
    "E": ["A"],
    "C": ["D", "E"]
}

strom = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "D": [],
    "E": [],
    "C": []
}


def dfs(g, node):
    print(node)
    for i in g[node]:
        dfs(g, i)


def dfs_collect(g, node, visited=[]):
    if node not in visited:
        visited.append(node)
    for i in g[node]:
        if i not in visited:
            dfs_collect(g, i)
    return visited

# ----------------------

def bfs_iter(g, start_node):
  visited = []
  queue = [start_node]
  while len(queue) > 0:
    node = queue.pop(0)
    if node not in visited:
      visited.append(node)
      queue += g[node] # <--
  return visited

def dfs_iter(g, start_node):
  visited = []
  stack = [start_node]
  while len(stack) > 0:
    node = stack.pop(0)
    if node not in visited:
      visited.append(node)
      stack = g[node] + stack # <--
  return visited

dfs(strom, "A")
print(dfs_collect(strom, "A"))