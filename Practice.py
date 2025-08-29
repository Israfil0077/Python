import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
# Romania cities and road distances
romania_graph = {
    'Arad': [('Zerind', 75), ('Sibiu', 140), ('Timisoara', 118)],
    'Zerind': [('Arad', 75), ('Oradea', 71)],
    'Oradea': [('Zerind', 71), ('Sibiu', 151)],
    'Timisoara': [('Arad', 118), ('Lugoj', 111)],
    'Lugoj': [('Timisoara', 111), ('Mehadia', 70)],
    'Mehadia': [('Lugoj', 70), ('Drobeta', 75)],
    'Drobeta': [('Mehadia', 75), ('Craiova', 120)],
    'Craiova': [('Drobeta', 120), ('Rimnicu Vilcea', 146), ('Pitesti', 138)],
    'Sibiu': [('Arad', 140), ('Oradea', 151), ('Fagaras', 99), ('Rimnicu Vilcea', 80)],
    'Fagaras': [('Sibiu', 99), ('Bucharest', 211)],
    'Rimnicu Vilcea': [('Sibiu', 80), ('Craiova', 146), ('Pitesti', 97)],
    'Pitesti': [('Rimnicu Vilcea', 97), ('Craiova', 138), ('Bucharest', 101)],
    'Bucharest': [('Fagaras', 211), ('Pitesti', 101), ('Urziceni', 85), ('Giurgiu', 90)],
    'Giurgiu': [('Bucharest', 90)],
    'Urziceni': [('Bucharest', 85), ('Hirsova', 98), ('Vaslui', 142)],
    'Hirsova': [('Urziceni', 98), ('Eforie', 86)],
    'Eforie': [('Hirsova', 86)],
    'Vaslui': [('Urziceni', 142), ('Iasi', 92)],
    'Iasi': [('Vaslui', 92), ('Neamt', 87)],
    'Neamt': [('Iasi', 87)]
}
# Heuristic values using my student ID
student_id = "0112230585"
last_two = int(student_id[-2:])
h_values = {
    'Arad': 366,
    'Bucharest': (last_two ** 2) + 1,
    'Craiova': 160, 'Drobeta': 242, 'Eforie': 161,
    'Fagaras': 176, 'Giurgiu': 77, 'Hirsova': 151, 'Iasi': 226,
    'Lugoj': 244, 'Mehadia': 241, 'Neamt': 234, 'Oradea': 380,
    'Pitesti': 100, 'Rimnicu Vilcea': 193, 'Sibiu': 253,
    'Timisoara': 329, 'Urziceni': 80, 'Vaslui': 199, 'Zerind': 374
}


def heuristic(node):
    return h_values.get(node, 0)
    # My path is based on SL_NO 6 (Oradea to Eforie)
    SL_NO = (int(student_id) % 10) + 1
    if SL_NO == 6:
    start_city = 'Oradea'
    goal_city = 'Eforie'
    #  A* search implementation
    def a_star_search(graph, start, goal, heuristic_func):
    open_set = set([start])
    came_from = {}
    g_score = {start: 0}
    while open_set:
    current = min(open_set, key=lambda c: g_score.get(
        c, float('inf')) + heuristic_func(c))
    if current == goal:
    path = []
    while current:
    path.append(current)
    current = came_from.get(current)
    return path[::-1]
    open_set.remove(current)
    for neighbor, dist in graph.get(current, []):
    tentative = g_score[current] + dist
    if neighbor not in g_score or tentative < g_score[neighbor]:
    came_from[neighbor] = current
    g_score[neighbor] = tentative
    open_set.add(neighbor)
    return None
    # Run search and show result
    found_path = a_star_search(romania_graph, start_city, goal_city, heuristic)
    print(f"My path from {start_city} to {goal_city}:", found_path)
    # Visualize path step-by-step
    def show_path(graph, path, heuristic_func):
    G = nx.Graph()
    for u in graph:
    for v, w in graph[u]:
    G.add_edge(u, v, weight=w)
    pos = nx.spring_layout(G, seed=55)
    fig, ax = plt.subplots(figsize=(11, 8))
    edges = [(path[i], path[i+1]) for i in range(len(path)-1)]
    def update(n):
    ax.clear()
    nx.draw_networkx_nodes(G, pos, node_size=1000,
                           node_color="Green", ax=ax)
    nx.draw_networkx_edges(G, pos, alpha=0.3, ax=ax)
    nx.draw_networkx_labels(G, pos, ax=ax)
    for city, (x, y) in pos.items():
    ax.text(x, y+0.05, f"h={heuristic_func(city)}",
            color="green", ha='center', fontsize=13)
    nx.draw_networkx_nodes(
        G, pos, nodelist=path[:n+1], node_color="red", node_size=1000, ax=ax)
    if n > 0:
    nx.draw_networkx_edges(
        G, pos, edgelist=edges[:n], edge_color="red", width=3, ax=ax)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=nx.get_edge_attributes(G, 'weight'),
                                 font_color="red", font_size=10, ax=ax)
    ax.set_title(f"Step {n+1}/{len(path)}: {path[n]}")
    ax.axis('off')
    anim = FuncAnimation(fig, update, frames=len(path),
                         interval=3000, repeat=False)
    plt.show()
    if found_path:
    show_path(romania_graph, found_path, heuristic)


if found_path:
    show_path(romania_graph, found_path, heuristic)
