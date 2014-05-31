import itertools as it

def nodes(graph):
	'''Returns all unique nodes present in graph.  Expects graph to be edgelist.
	example:  g1 = [[n1, n2],[n2, n3]]
	          nodes(g1)

	result:   [n1, n2, n3]
	'''
	nodes = []
	[nodes.extend(i) for i in graph]
	return list(set(nodes))
	


def n_nodes(node_list):
	'''Counts number of nodes in a set of nodes. 
	Expects nodes to be list/set/frozenset.
	'''
	return len(set(nodes(node_list)))



def n_edges(graph):
	'''Counts nummber of edges in a graph.
	example:  g1 = [[n1, n2],[n2, n3]]
	          nodes(g1)

	result:   [n1, n2, n3]
	'''
	return len(graph)



def nodes_edges(node, graph):
	'''Returns a list of all edges for a specified node.
	'''
	edges = list(filter(lambda x: x.count(node), graph))
	return edges



def total_deg(node, graph):
	'''Returns the total degree for a given node in a given graph.
	'''
	t_deg = nodes_edges(node, graph)
	return len(t_deg)



def in_edges(node, graph):
	'''Returns the in degree (number of inward pointing edges on a node) on a specific node
	'''
	edges = nodes_edges(node, graph)
	in_edge = list(filter(lambda x: x.index(node) == 1, edges))
	return in_edge



def in_degree(node, graph):
	'''Returns number of inward pointing edges on specific node.
	'''
	return len(in_edges(node, graph))



def out_edges(node, graph):
	'''Retruns the out degree (number of outward pointing edges) on specific node
	'''
	edges = nodes_edges(node, graph)
	out_edge = list(filter(lambda x: x.index(node) == 0, edges))
	return out_edge


def out_degree(node, graph):
	'''Return the number of outwward pointing edges on a specific node.
	'''
	return len(out_edges(node,graph))