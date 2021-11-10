class Point:
    def __init__(self, i, j, step):
        self.__i = i
        self.__j = j
        self.__step = step

    def __get_i(self):
        return self.__i
    I = property(__get_i)

    def __get_j(self):
        return self.__j
    J = property(__get_j)

    def __get_step(self):
        return self.__step
    Step = property(__get_step)


import numpy
def horse(m, n, from_i, from_j, to_i, to_j):
    if from_i<0 or from_j<0 or to_i <0 or to_j <0 or from_i >=m or to_i>=m or to_j>=n or from_j>=n:
        return -2
    if from_i == to_i and from_j == to_j:
        return 0
    queue = []
    first = Point(from_i, from_j, 0)
    visited = numpy.zeros((m, n))
    next = ((1, 2), (2, 1), (1, -2), (2, -1), (-1, -2), (-2, -1), (-1, 2), (-2, 1))
    visited[from_i][from_j] = 1
    queue.append(first)
    while queue:
        cur = queue.pop(0)
        for i in next:
            next_step = Point(cur.I+i[0], cur.J+i[1], cur.Step+1)
            if next_step.I == to_i and next_step.J == to_j:
                return next_step.Step
            elif 0 <= next_step.I < m and 0 <= next_step.J < n and not visited[next_step.I][next_step.J]:
                visited[next_step.I][next_step.J] = 1
                queue.append(next_step)
    return -1


if __name__ == '__main__':
    print(horse(5, 6, 0, 0, 1, 1))



