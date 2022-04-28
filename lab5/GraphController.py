import subprocess

from py4j.java_gateway import JavaGateway, GatewayParameters


class GraphController:

    def __init__(self):
        subprocess.Popen(['java', 'GraphEntryPoint'])
        self.gateway2 = JavaGateway(gateway_parameters=GatewayParameters(port=25333))
        self.graph = self.gateway2.entry_point.getGraph()

    def add_node(self, label):
        self.graph.addNode(str(label))

    def remove_node(self, label):
        self.graph.removeNode(str(label))

    def add_edge(self, label_source, label_dest, weight):
        self.graph.addEdge(str(label_source), str(label_dest), weight)

    def remove_edge(self, label_source, label_dest):
        self.graph.removeEdge(str(label_source), str(label_dest))

    def bfs(self, root):
        print(self.graph.BFS(str(root)))

    def dfs(self, root):
        print(self.graph.DFS(str(root)))

    def print_graph(self):
        print(self.graph.toString())

    @staticmethod
    def stop_graph():
        jg = JavaGateway()
        jg.close()
        jg.shutdown()
