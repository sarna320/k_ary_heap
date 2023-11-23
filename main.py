import random
import time
from heap import *
from draw_graphs import *
from draw_plots import *


def main():
    list_entry = []
    for i in range(0, 100000):
        list_entry.append(random.randint(1, 300000))

    number_of_data = list(range(10000, 110000, 10000))

    list_of_all_heaps = []
    for k in range(2, 5):
        list_of_heaps = []
        for i in number_of_data:
            temp = list_entry[0:i]
            start = time.process_time()
            build_heap(temp, len(temp), k)
            stop = time.process_time()
            x = Heap(h=temp, bt=stop - start, et=0)
            start = time.process_time()
            for ii in range(0, i):
                extract_max(temp, len(temp), k)
            stop = time.process_time()
            x.extraction_time = stop - start
            list_of_heaps.append(x)
        list_of_all_heaps.append(list_of_heaps)

    #uncomment to draw graphs
    # for i in range(2,5):
    #     draw_graph(list_of_all_heaps[i-2][1].heap, i)

    draw_plots(list_of_all_heaps, number_of_data)

    # insert(list_of_all_heaps[0][1].heap, len(list_of_all_heaps[0][1].heap), 2, 1500000)
    # draw_graph(list_of_all_heaps[0][1].heap, 2, "heap_insert")
    # extract_max(list_of_all_heaps[0][1].heap, len(list_of_all_heaps[0][1].heap), 2)
    # draw_graph(list_of_all_heaps[0][1].heap, 2, "heap_extr")


if __name__ == "__main__":
    main()
