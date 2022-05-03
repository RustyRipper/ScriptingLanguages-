import py4j.GatewayServer;


public class GraphEntryPoint {


    public Graph getNewGraph(){
        return new Graph();
    }
    public static void main(String[] args) {

        GatewayServer server = new GatewayServer(new GraphEntryPoint());
        server.start();


    }
}
