# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 16:23:51 2019

@author: keshav singh
"""

import networkx as nx
import matplotlib.pyplot as plt

G=nx.gnp_random_graph(50,0.3)
nx.draw(G)
plt.show()