# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 22:28:18 2019

@author: keshav singh
"""

import networkx as nx
import random
import matplotlib.pyplot as plt

G=nx.gnp_random_graph(10,0.5,directed=True)
nx.draw(G,with_labels=True)
plt.show()