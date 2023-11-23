import random
import time
from heap import *
from draw_graphs import *
from draw_plots import draw_plot_for_build,draw_plot_for_execution


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

# uncomment to draw graphs
    #draw_graph_2(list_of_all_heaps[0][1].heap,2,"2_heap")
    #draw_graph_3(list_of_all_heaps[1][1].heap,3,"3_heap")
    #draw_graph_4(list_of_all_heaps[2][1].heap,4,"4_heap")
    draw_plot_for_build(list_of_all_heaps, number_of_data)
    draw_plot_for_execution(list_of_all_heaps, number_of_data)

    # insert(list_of_all_heaps[0][1].heap,len(list_of_all_heaps[0][1].heap),2,1500000)
    # draw_graph_2(list_of_all_heaps[0][1].heap,2,"heap_insert")

    # extract_max(list_of_all_heaps[0][1].heap,len(list_of_all_heaps[0][1].heap),2)
    # draw_graph_2(list_of_all_heaps[0][1].heap,2,"heap_extr")
    
if __name__ == "__main__":
    main()
