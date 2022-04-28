import java.util.Comparator;

public class SortEdges implements Comparator<Edge> {
    public int compare(Edge a, Edge b){
        if (a.weight == b.weight)
            return b.destinationNode.label.compareTo(a.destinationNode.label);
        return b.weight- a.weight;
    }
}
