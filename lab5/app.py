from GraphController import GraphController

graph = GraphController()

flag = True


def upload_data():
    graph.add_node('jeden')
    graph.add_node('dwa')
    graph.add_node('trzy')
    graph.add_node('cztery')

    graph.add_edge("jeden", "dwa", 2)
    graph.add_edge("dwa", "trzy", 5)
    graph.add_edge("cztery", "jeden", 5)
    graph.add_edge("jeden", "dwa", 3)
    graph.add_edge("jeden", "cztery", 3)


while flag:
    print("---------Menu----------")
    print("1.Print Graph")
    print("2.Add node")
    print("3.Remove node")
    print("4.Add edge")
    print("5.Remove edge")
    print("6.DFS")
    print("7.BFS")
    print("8.Upload data")
    try:
        choice = int(input("Choose option:"))
    except ValueError:
        print("bad parametr")
        choice = 0
    if choice == 0:
        print("try again")
    elif choice == 1:
        graph.print_graph()
    elif choice == 2:
        graph.add_node(input("Set label"))
    elif choice == 3:
        graph.remove_node(input("Insert label(node) to remove"))
    elif choice == 4:
        graph.add_edge(input("Insert label(node source)"), input("Insert label(node dest)"),
                       int(input("Insert weight of edge")))
    elif choice == 5:
        graph.remove_edge(input("Insert label(node source)"), input("Insert label(node dest)"))
    elif choice == 6:
        graph.dfs(input("Insert root-label"))
    elif choice == 7:
        graph.bfs(input("Insert root-label"))
    elif choice == 8:
        upload_data()
    else:
        graph.stop_graph()
        flag = False

