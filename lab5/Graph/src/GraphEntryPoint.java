import py4j.GatewayServer;


public class GraphEntryPoint {
    private static Graph graph;

    public GraphEntryPoint() {
        graph = new Graph();

    }
    public Graph getGraph(){
        return graph;
    }
    public static void main(String[] args) {

        GatewayServer server = new GatewayServer(new GraphEntryPoint(), 25333);
        server.start();


    }
}
