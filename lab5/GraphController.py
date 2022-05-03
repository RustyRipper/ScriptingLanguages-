import subprocess

from py4j.java_gateway import JavaGateway, GatewayParameters


class GraphController:
    graphs = {}
    actualGraph = None

    def __init__(self):
        subprocess.Popen(['java', 'GraphEntryPoint'])
        self.gateway2 = JavaGateway()

    def choose_graph(self, graphName):
        self.actualGraph = self.graphs[graphName]

    def add_graph(self, graphName):
        self.graphs[graphName] = self.gateway2.entry_point.getNewGraph()

    def print_graphs(self):
        print(self.graphs)

    def add_node(self, label):
        self.actualGraph.addNode(str(label))

    def remove_node(self, label):
        self.actualGraph.removeNode(str(label))

    def add_edge(self, label_source, label_dest, weight):
        self.actualGraph.addEdge(str(label_source), str(label_dest), weight)

    def remove_edge(self, label_source, label_dest):
        self.actualGraph.removeEdge(str(label_source), str(label_dest))

    def bfs(self, root):
        print(self.actualGraph.BFS(str(root)))

    def dfs(self, root):
        print(self.actualGraph.DFS(str(root)))

    def change_node_label(self, old_label, new_label):
        self.actualGraph.modifyNodeLabel(str(old_label), str(new_label))

    def change_edge_weight(self, source_label, dest_label, weight):
        self.actualGraph.modifyWeightEdge(str(source_label), str(dest_label), weight)

    def print_graph(self):
        print(self.actualGraph.toString())

    def stop_graph(self):
        self.gateway2.close()
        self.gateway2.shutdown()
