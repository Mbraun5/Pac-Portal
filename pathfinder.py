class Pathfinder:
    def __init__(self, nodes):
        self.nodes = nodes
        self.inf = 99999
        ''' For Testing:
        for key, node in enumerate(self.nodes):
            print(key, ": ", node)
        print(len(nodes))
        '''
        self.nodeDict = {0: [1, 6], 1: [0, 2, 7], 2: [1, 9], 3: [4, 10], 4: [3, 5, 12], 5: [4, 13],
                         6: [0, 7, 14], 7: [6, 8, 1, 15], 8: [7, 9, 16], 9: [8, 10, 2], 10: [9, 11, 3],
                         11: [10, 12, 19], 12: [11, 13, 4, 20], 13: [12, 5, 21], 14: [15, 6],
                         15: [14, 7, 28], 16: [17, 8], 17: [16, 23], 18: [19, 25], 19: [18, 11],
                         20: [21, 12, 31], 21: [20, 13], 22: [23, 29], 23: [22, 24, 17],
                         24: [23, 25, 27], 25: [24, 26, 18], 26: [25, 30], 27: [24], 28: [15, 29, 35],
                         29: [28, 22, 33], 30: [31, 26, 33], 31: [30, 20, 40], 32: [33, 29, 36],
                         33: [32, 30, 39], 34: [35, 42], 35: [34, 36, 28, 44], 36: [35, 37, 32],
                         37: [36, 46], 38: [39, 47], 39: [38, 40, 33], 40: [39, 41, 31, 49],
                         41: [40, 51], 42: [43, 34], 43: [42, 53], 44: [45, 35, 53], 45: [44, 46, 55],
                         46: [45, 47, 37], 47: [46, 48, 38], 48: [47, 49, 58], 49: [48, 40, 59],
                         50: [51, 60], 51: [50, 41], 52: [53, 62], 53: [52, 54, 43], 54: [53, 44],
                         55: [56, 45], 56: [55, 63], 57: [58, 64], 58: [57, 48], 59: [60, 49],
                         60: [59, 61, 50], 61: [60, 65], 62: [52, 63], 63: [62, 64, 56], 64: [63, 65, 57],
                         65: [64, 61]}
        self.origDict = self.create_orig_dict()

    def create_orig_dict(self):
        orig_dict = {}
        for i in range(0, 66):
            orig_dict[i] = [self.inf, i, False]
        # print(orig_dict)
        return orig_dict

    def find_fastest_path(self, a, b):
        self.origDict = self.create_orig_dict()
        alg_dict = self.origDict.copy()
        smallest_index = a
        visit_list = [a]
        while alg_dict[b][2] is False:
            # print(alg_dict)
            alg_dict[smallest_index][2] = True
            visit_list.remove(smallest_index)
            for index in self.nodeDict[smallest_index]:
                if alg_dict[index][0] == self.inf:
                    if self.nodes[index].x - self.nodes[smallest_index].x == 0:
                        alg_dict[index][0] = int(abs(self.nodes[index].y - self.nodes[smallest_index].y))
                    else:
                        alg_dict[index][0] = int(abs(self.nodes[index].x - self.nodes[smallest_index].x))
                    alg_dict[index][1] = smallest_index
                    visit_list.append(index)
                else:
                    if self.nodes[index].x - self.nodes[smallest_index].x == 0:
                        value = int(abs(self.nodes[index].y - self.nodes[smallest_index].y))
                    else:
                        value = int(abs(self.nodes[index].x - self.nodes[smallest_index].x))
                    if alg_dict[index][0] > value + alg_dict[smallest_index][0]:
                        alg_dict[index][0] = value + alg_dict[smallest_index][0]
                        alg_dict[index][1] = smallest_index
                    if index not in visit_list and alg_dict[index][2] is False:
                        visit_list.append(index)
            smallest_elem = 999999
            for elem in visit_list:
                if alg_dict[elem][0] < smallest_elem:
                    smallest_index = elem
                    smallest_elem = alg_dict[elem][0]
        current_elem = b
        ret_list = [b]
        while current_elem is not a:
            ret_list.insert(0, alg_dict[current_elem][1])
            current_elem = alg_dict[current_elem][1]
        return ret_list

    '''
    path = pathfinder.Pathfinder(maze.nodes)
    print(maze.nodes[0] == maze.nodes[1])
    for node in maze.nodes:
        targetrect = pygame.Rect(965, 965, 45, 45)
        if node == targetrect:
            print("yes")
        else:
            print("no")
        print()
        print()
        print(self.nodeDict)
        for key in self.nodeDict:
            print(nodes[key], end=": ")
            for obj in self.nodeDict[key]:
                print(nodes[obj], end=" ")
            print()
        print()
        print()
    '''