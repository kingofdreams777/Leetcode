testGraph = {
    0: [8,1,5],
    1: [0],
    5: [0,8],
    8: [0,5],
    2: [3, 4],
    3: [2, 4],
    4: [3, 2]
}

def connectedComponentCount(graph) -> int:
    visit = set()
    count = 0

    def explore(current) -> bool:
        if current in visit: return False

        visit.add(current)

        for neighbor in graph[current]:
            explore(neighbor)

        return True

    for node in graph:
        if explore(node):
            count += 1

    return count

print(connectedComponentCount(testGraph))