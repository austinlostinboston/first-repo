import itertools as it

def nodes(graph):
	'''Returns all unique nodes present in graph.  Expects graph to be edgelist.
	graph(3 nodes, 2 edges) = [[n1, n2],[n2, n3]]'''
	nodes = []
	[nodes.extend(i) for i in graph]
	return list(set(nodes))
	
def n_nodes(node_list):
	'''Counts number of nodes in a set of nodes. 
	Expects nodes to be list/set/frozenset.'''
	return len(set(nodes(node_list)))

def n_edges(graph):
	'''Counts nummber of edges in a graph.  Expects graph to be edgelist.
	graph(3 nodes, 2 edges) = [[n1, n2],[n2, n3]]'''
	return len(graph)

def	nodes_edges(node, graph):
	'''Returns a list of all edges for a specified node.
	'''
	edges = list(filter(lambda  x: x.count(node), graph))
	return edges

def total_deg(node, graph):
	'''Returns the total degree for a given node in a given graph.
	'''
	t_deg = nodes_edges(node, graph)
	return len(t_deg)

def in_deg(node, graph):
	edges = nodes_edges(node, graph)
	#in_edges
	return edges

def out_deg(node, graph):
	#edges = nodes_edges(node, graph)
	return edges
	