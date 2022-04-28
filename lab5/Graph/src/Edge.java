import java.util.Objects;

public class Edge {

    final Node destinationNode;
    int weight;

    public Edge(Node destinationNode, int weight) {

        this.destinationNode = destinationNode;
        this.weight = weight;
    }

    @Override
    public String toString() {
        return "{ " + destinationNode + " (" + weight + ") }";

    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Edge edge = (Edge) o;
        return Objects.equals(destinationNode, edge.destinationNode);
    }

    @Override
    public int hashCode() {
        return Objects.hash(destinationNode);
    }


}