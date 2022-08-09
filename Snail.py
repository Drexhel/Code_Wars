import numpy as np
def snail(snail_map):
    result = []
    while len(snail_map) != 0:
        for i in snail_map[0]:
            result.append(i)
        snail_map = np.delete(snail_map,0,0)
        snail_map = np.transpose(snail_map)
        snail_map = np.flip(snail_map,0)

    return result