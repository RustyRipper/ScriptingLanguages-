from GraphController import GraphController
import time
graph_controller = GraphController()

flag = True


def menu_graph():
    flag2 = True
    while flag2:
        print("---------Graph----------")
        print("0.Back")
        print("1.Print Graph")
        print("2.Add node")
        print("3.Remove node")
        print("4.Add edge")
        print("5.Remove edge")
        print("6.DFS")
        print("7.BFS")
        print("8.Upload data")
        print("9.Change node label")
        print("10.Change edge weight")

        try:
            choice2 = int(input("Choose option: "))
        except ValueError:
            print("bad parametr")
            choice2 = -1

        if choice2 == 1:
            graph_controller.print_graph()
        elif choice2 == 2:
            graph_controller.add_node(input("Set label: "))
        elif choice2 == 3:
            graph_controller.remove_node(input("Insert label(node) to remove: "))
        elif choice2 == 4:
            graph_controller.add_edge(input("Insert label(node source): "), input("Insert label(node dest): "),
                                      int(input("Insert weight of edge: ")))
        elif choice2 == 5:
            graph_controller.remove_edge(input("Insert label(node source): "), input("Insert label(node dest): "))
        elif choice2 == 6:
            graph_controller.dfs(input("Insert root-label: "))
        elif choice2 == 7:
            graph_controller.bfs(input("Insert root-label: "))
        elif choice2 == 8:
            upload_data()
        elif choice2 == 9:
            graph_controller.change_node_label(input("Insert old label: "), input("Insert  new label: "))
        elif choice2 == 10:
            graph_controller.change_edge_weight(input("Insert label(node source): "), input("Insert label(node dest): "), int(input("new weight: ")))
        else:
            flag2 = False


def upload_data():
    graph_controller.add_node('jeden')
    graph_controller.add_node('dwa')
    graph_controller.add_node('trzy')
    graph_controller.add_node('cztery')

    graph_controller.add_edge("jeden", "dwa", 2)
    graph_controller.add_edge("dwa", "trzy", 5)
    graph_controller.add_edge("cztery", "jeden", 5)
    graph_controller.add_edge("jeden", "dwa", 3)
    graph_controller.add_edge("jeden", "cztery", 3)


while flag:
    print("---------Menu----------")
    print("0.Exit")
    print("1.Create graph")
    print("2.Choose graph")
    print("3.Print graphs")

    try:
        choice = int(input("Choose option: "))
    except ValueError:
        print("bad parametr")
        choice = -1
    if choice == 0:
        flag = False
    if choice == 1:
        graph_controller.add_graph(input("Set graphName: "))
    elif choice == 2:
        graph_controller.choose_graph(input("Choose graph: "))
        menu_graph()
    elif choice == 3:
        graph_controller.print_graphs()
    else:
        graph_controller.stop_graph()
        time.sleep(2.5)
        flag = False
