
from hc_pizza_practice import *

from multiprocessing import Pool

import time
start = time.time()

if __name__ == '__main__':
    with Pool(8) as p:
        print(p.map(process_file, file_names))