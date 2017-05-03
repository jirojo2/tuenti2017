#
# Tuenti Challenge 2017
# Challenge 6
# Jose Ignacio Rojo Rivero
#

import networkx as nx
import matplotlib.pyplot as plt
import sys
import os

from os.path import basename
from os.path import splitext

# some debug utilities
debug = len(sys.argv) == 1 or 'debugInput' in sys.argv[1] or 'debug' in sys.argv

infile = sys.argv[1] if len(sys.argv) > 1 else 'testInput.txt'

# lets draw the graphs in folders by input type
if debug:
    graphs_dir = 'graphs-%s' % splitext(basename(infile))[0]
    if not os.path.exists(graphs_dir):
        os.makedirs(graphs_dir)

# back to Calculus I...
def arithmetic_series(start, stop, step=1):
    number_of_terms = (stop - start) // step
    sum_of_extrema = start + (stop - step)
    return number_of_terms * sum_of_extrema // 2

# parse file
with open(infile) as f:
    N = int(f.readline())
    for n in xrange(N):
        tokens = f.readline().split(' ')
        F = int(tokens[0])
        S = int(tokens[1])

        G = nx.DiGraph()
        up_edges = []
        down_edges = []
        shortcut_edges = []

        if F > 1:
            if debug: print 'preparing graph'

            # add shortchuts
            if debug: print '  A) filter shortcuts'
            shortcuts = {}
            shortcut_entries = []
            for _ in xrange(S):
                tokens = f.readline().split(' ')
                A = int(tokens[0])
                B = int(tokens[1])
                Y = int(tokens[2])

                if B == A+1 and Y >= A:
                    # this is not a good shortcut...
                    # tuenti traps...
                    continue

                sc = (A, B)
                # filter longer shortcuts (tuenti traps...)
                # dijsktra is not that strong it seems...
                if sc not in shortcuts or Y < shortcuts[sc]:
                    shortcuts[sc] = Y
                    shortcut_entries.append(A)

            if debug: print '  B) add shortcuts'
            door_nodes = {}
            door_nodes[1] = True
            door_nodes[F] = True
            for (A, B), Y in shortcuts.iteritems():
                G.add_edge(A, B, weight=Y)
                shortcut_edges.append((A, B))
                door_nodes[A] = True
                door_nodes[B] = True

            # add floors and common tests
            if debug: print '  C) add floor nodes'
            doors = sorted(door_nodes.keys())
            for a, b in zip(doors[:-1], doors[1:]):
                w = arithmetic_series(a, b)
                if G.has_edge(a, b):
                    edge_w = G.get_edge_data(a, b)['weight']
                    if edge_w <= w:
                        continue
                G.add_edge(a, b, weight=w)
                if debug: up_edges.append((a, b))

            # go backwards
            if debug: print '  D) add backways'
            nodes = sorted(G.nodes())
            for a, b in zip(nodes[:-1], nodes[1:]):
                G.add_edge(b, a, weight=0)
                down_edges.append((b, a))

            # calculate the shortest path
            if debug: print 'calculating shortest path'
            if debug:
                print nx.shortest_path(G, 1, F, weight='weight')
            path = nx.shortest_path_length(G, 1, F, weight='weight')
        else:
            # tuenti traps...
            path = 0

        # generate output :D
        print 'Case #%d: %s' % (n+1, path)

        # graph info
        if debug and F > 1:
            print 'Graph info:'
            print '  nodes: %d' % len(G.nodes())
            print '  edges: %d' % len(G.edges())
            print '  tests: %d' % len(up_edges)
            print '  down: %d' % len(down_edges)
            print '  shortucts: %d' % len(shortcut_edges)

        # export graph
        if debug and F > 1:
            nx.write_weighted_edgelist(G, "%s/%d.weighted.edgelist" % (graphs_dir, n+1))

        # draw the graph
        if debug and F > 1:
            labels_up = { (a, b): data['weight'] for a, b, data in G.edges(data=True) if (a, b) in up_edges }
            labels_shortcut = { (a, b): data['weight'] for a, b, data in G.edges(data=True) if (a, b) in shortcut_edges }
            
            fig = plt.figure(num=None, figsize=(20, 20), dpi=100)
            plt.axis('off')
            pos = nx.circular_layout(G)
            nx.draw_networkx_nodes(G, pos)
            nx.draw_networkx_labels(G, pos)
            nx.draw_networkx_edges(G, pos, edgelist=down_edges, edge_color='b', arrows=True, width=3.0)
            nx.draw_networkx_edges(G, pos, edgelist=shortcut_edges, edge_color='r', arrows=True, width=2.0)
            nx.draw_networkx_edge_labels(G, pos, edge_labels=labels_shortcut, font_color='r')
            nx.draw_networkx_edges(G, pos, edgelist=up_edges, edge_color='g', arrows=True, width=1.0)
            #nx.draw_networkx_edge_labels(G, pos, edge_labels=labels_up, font_color='g')
            plt.savefig("%s/%d.png" % (graphs_dir, n+1), bbox_inches='tight')
            # plt.show()
            plt.clf()
            del fig
