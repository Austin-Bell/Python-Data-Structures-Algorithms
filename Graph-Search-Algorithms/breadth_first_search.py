# define breadth first search function
def bfs(graph, start_vertex, target_value):

    # variable that stores are starting point
    path = [start_vertex]
    # a list that contains start_vertex and starting path
    vertex_and_path = [start_vertex, path]
    bfs_queue = [vertex_and_path]
    # define a variable that stores vertices in empty set
    visited = set()

    # Use a while loop to search through queue
    while bfs_queue:
        # set current_vertex & path equal to first vertex & path on queue
        current_vertex, path = bfs_queue.pop(0)
        
        visited.add(current_vertex)
        for neighbor in graph[current_vertex]:
            if neighbor not in visited:
                if neighbor == target_value:
                    return path + [neighbor]
                else:
                    bfs_queue.append([neighbor, path + [neighbor]])
