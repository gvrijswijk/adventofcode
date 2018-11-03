import re
from array import *
import numpy as np
import math


def Input(day, year=2017):
    "Open the day's input file."
    #file = str(year) + '/' + str(day) + '_input.txt'
    file = str(day) + '_input.txt'
    return open(file)


def manhattan_distance(start, end=(0, 0)):
    sx, sy = start
    ex, ey = end
    return abs(ex - sx) + abs(ey - sy)

start1 = '.#./..#/###' #1
start2 = '...#/.##./#..#/#.#.' #2
start3 = '#...#./.#.##./####.#/#...#./#####./#..#.#' #3
start4 = '.#.#..#../##..#.###/#.#####../.#.#...#./...#####./...#..#.#/.#..#..#./......##./......#.#' #4
start5 = '#.####..###./..#.#.#...#./#.#.#.##..../.##.#...#.##/....###.#.##/###...#...#./.###....#.#./##..#.##.##./........#.##/###.###...#./.###.####.#./##..##...##.' #4
start6 = '#...#..#.#..#..#../.#........#.######/###......####..#../.#.#..#..#..#..#../##.#########.#.###/#.##..#..#..####../#..#..#..#..#...#./###.#.######.#..../#..####..#..###.../.#.#..#..#...#.#../...###.#.#####.###/...#..####..#.##../#..#..#..#..#...#./###.#.###.#..#..../#..####..######.../.#.#...#.#...#.#../...###...#####.###/...#.....#..#.##..' #6

def parse_rules(input):
    rules = {}
    for line in input.readlines():
        r = re.compile(r'([\.\#\/]+)')
        q = r.findall(line)
        rules[q[0]] = q[1]
    return rules

def str_to_lst(str_in, sep):
    return str_in.split(sep)

def lst_to_str(lst_in, sep):
    return sep.join(lst_in)

def str_to_arr(str_in, sep):
    return np.array([list(e) for e in str_in.split(sep)])

def arr_to_str(arr_in, sep):
    return sep.join([''.join(e) for e in arr_in])

def mirror(str_in, sep):
    return arr_to_str(np.fliplr(str_to_arr(str_in, sep)), sep)

def rotate(str_in, sep, n):
    return arr_to_str(np.rot90(str_to_arr(str_in, sep), n),sep)

def create_possibilities(str_in, sep, rot=4, mir=1):
    poss = []
    for i in range(rot):
        str_in = rotate(str_in, sep, i)
        if str_in not in poss:
            poss.append(str_in)
        if mir == 1 and mirror(str_in, sep) not in poss:
            poss.append(mirror(str_in, sep))
    return(poss)

def deconstruct_grid(str_in, sep):
    grid = str_to_arr(str_in, '/')
    subgrids = []
    f = [3, 2][len(grid) % 2 == 0]
    for x in range(0, len(grid), f):
        for y in range(0, len(grid), f):
            subgrids.append(arr_to_str(grid[x:x+f, y:y+f], '/'))
    return subgrids

def construct_grid(lst_in, sep):
    subgrids = [str_to_lst(e, sep) for e in lst_in]
    print(subgrids)

rules = parse_rules(Input('21'))


input = start1

for i in range(18):
    print(str(i)+ ":" + input)
    grid = deconstruct_grid(input,'/')
    #print(grid)

    for n, e in enumerate(grid):
        for f in create_possibilities(e, '/'):
            if f in rules:
                grid[n] = rules[f]
    #print(grid)
    f = int(math.sqrt(len(grid)))
    grid = np.array(grid).reshape(f,f)

    for m, e in enumerate(grid):
        for n, f in enumerate(e):
            if n == 0:
                t1 = np.array(str_to_arr(f,'/'))
            else:
                t1 = np.concatenate((t1, str_to_arr(f, '/')), axis=1)
        if m == 0:
            t2 = t1
        else:
            t2 = np.concatenate((t2, t1), axis=0)

    t3 = arr_to_str(t2, '/')
    #print(t3)
    input = t3
print(len(t3))
print(t3.count('#'))
