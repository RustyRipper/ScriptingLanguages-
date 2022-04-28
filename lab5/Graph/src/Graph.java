import java.util.*;

public class Graph {

    private final Map<Node, List<Edge>> connectedNodes;

    public Graph() {
        connectedNodes = new HashMap<>();
    }

    public void addNode(String label) {
        connectedNodes.putIfAbsent(new Node(label), new ArrayList<>());
    }
    public void setNodeLabel(String label){
        if(connectedNodes.containsKey(new Node(label))){

        }
    }

    public void removeNode(String label) {

        Node nodeToRemove = new Node(label);
        Edge edgeToRemove = new Edge(nodeToRemove, 0);
        connectedNodes.values().forEach(e -> e.remove(edgeToRemove));
        connectedNodes.remove(nodeToRemove);
    }

    public void addEdge(String label1, String label2, int weight) {
        Node node1 = new Node(label1);
        addNode(label1);
        Node node2 = new Node(label2);
        addNode(label2);
        if(!connectedNodes.get(node1).contains(new Edge(node2,0)))
            connectedNodes.get(node1).add(new Edge(node2, weight));
    }

    public void removeEdge(String label1, String label2) {
        Node node1 = new Node(label1);
        Node node2 = new Node(label2);
        List<Edge> edges = connectedNodes.get(node1);
        if (edges != null)
            edges.remove(new Edge(node2, 0));

    }

    public ArrayList<String> DFS(String root) {
        ArrayList<String> visited = new ArrayList<>();
        Stack<String> stack = new Stack<String>();
        stack.push(root);
        while (!stack.isEmpty()) {
            String vertex = stack.pop();
            if (!visited.contains(vertex)) {
                visited.add(vertex);
                List<Edge> edges = getEdges(vertex);
                if (edges != null) {
                    edges.sort(new SortEdges());
                    for (Edge e : edges) {
                        stack.push(e.destinationNode.label);
                    }
                }
            }
        }
        return visited;
    }

    public ArrayList<String> BFS(String root) {

        ArrayList<String> visited = new ArrayList<>();
        Queue<String> queue = new LinkedList<String>();
        queue.add(root);
        visited.add(root);
        while (!queue.isEmpty()) {
            String vertex = queue.poll();
            List<Edge> edges = getEdges(vertex);
            edges.sort(new SortEdges());
            Collections.reverse(edges);

            for (Edge e : edges) {
                if (!visited.contains(e.destinationNode.label)) {
                    visited.add(e.destinationNode.label);
                    queue.add(e.destinationNode.label);
                }
            }
        }
        return visited;
    }

    private List<Edge> getEdges(String label) {
        return connectedNodes.get(new Node(label));
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("Graph:\n");
        for (var entry : connectedNodes.entrySet()) {
            sb.append(entry.getKey().toString()).append("=").append(entry.getValue()).append("\n");
        }
        return sb.toString();
    }


}
