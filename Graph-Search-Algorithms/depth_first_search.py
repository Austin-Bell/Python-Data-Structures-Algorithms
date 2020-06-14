# define a depth first search function which uses recursion

def dfs(graph, current_vertex, target_value, visited=None):
    # visited is a list to keep track of our current path
    if visited == None:
        visited = []
    visited.append(current_vertex)
    
    # build out the base case
    if current_vertex == target_value:
        return visited

    # recursive case
    for neighbor in graph[current_vertex]:
        if neighbor not in visited:
            path = dfs(graph, neighbor, target_value, visited)
            if path:
                return path


