from GraphController import GraphController

graph = GraphController()
graph.add_node('jeden')
graph.add_node('dwa')
graph.add_node('trzy')
graph.add_node('cztery')

graph.add_edge("jeden", "dwa", 2)
graph.add_edge("dwa", "trzy", 5)
graph.add_edge("cztery", "jeden", 5)
graph.add_edge("jeden", "dwa", 3)
graph.add_edge("jeden", "cztery", 3)

print(graph.bfs('jeden'))
print(graph.dfs('jeden'))
graph.print_graph()


