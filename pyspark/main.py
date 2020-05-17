import sys
import numpy as np
import random
import pprint
from operator import add
from pyspark import SparkContext

master = "local[*]"
pp = pprint.PrettyPrinter(indent=2).pprint

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print('Usage: ' + sys.argv[0] + ' <input file> <n>', file=sys.stderr)
        sys.exit(1)

    CONF_INPUT_FILE = sys.argv[1]
    CONF_N = int(sys.argv[2])

    sc = SparkContext(master, "KMeans")

    random.seed(42)

    m = sc.textFile(CONF_INPUT_FILE) \
        .map(lambda x: ( ( int(random.uniform(0, CONF_N)), [ np.fromstring(x, dtype=float, sep=',') ] ))) \
        .reduceByKey(lambda x, y: x + y) \
        .sortByKey()

    pp(m.collect())
    pp(m.count())

