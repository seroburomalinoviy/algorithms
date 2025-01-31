import objgraph

my_list = [1, 2, 3]
objgraph.show_refs([my_list], filename='my_list.png')