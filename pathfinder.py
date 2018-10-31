class Pathfinder:
    def __init__(self, nodes):
        self.nodes = nodes
        for key, node in enumerate(self.nodes):
            print(key, ": ", node)
        print(len(nodes))
        self.nodeDict = {0: [1, 6], 1: [0, 2, 7], 2: [1, 9], 3: [4, 10], 4: [3, 5, 12], 5: [4, 13],
                         6: [0, 7, 14], 7: [6, 8, 1, 15], 8: [7, 9, 16], 9: [8, 10, 2], 10: [9, 11, 3],
                         11: [10, 12, 19], 12: [11, 13, 4, 20], 13: [12, 5, 21], 14: [15, 6],
                         15: [14, 7, 28], 16: [17, 8], 17: [16, 23], 18: [19, 25], 19: [18, 11],
                         20: [21, 12, 31], 21: [20, 13], 22: [23, 29], 23: [22, 24, 17],
                         24: [23, 25, 27], 25: [24, 26, 18], 26: [25, 30], 27: [24], 28: [15, 29, 35],
                         29: [28, 22, 33]}
        print()
        print()
        print(self.nodeDict)
        for key in self.nodeDict:
            print(nodes[key], end=": ")
            for obj in self.nodeDict[key]:
                print(nodes[obj], end=" ")
            print()




    '''
    path = pathfinder.Pathfinder(maze.nodes)
    print(maze.nodes[0] == maze.nodes[1])
    for node in maze.nodes:
        targetrect = pygame.Rect(965, 965, 45, 45)
        if node == targetrect:
            print("yes")
        else:
            print("no")
    '''