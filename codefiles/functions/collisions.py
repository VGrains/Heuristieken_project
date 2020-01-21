def calculate_collisions(routes, gate_locations):  
    all_nodes = []
    for route in routes:
        for node in routes[route]:
            all_nodes.append(node)

    collisions = {}
    for route in routes:
        for node in routes[route]:
            collisions[node] = 0
            for current_node in all_nodes:
                if node == current_node and node not in gate_locations.values():
                    collisions[node] += 1

    collisions_sorted = {k: v for k, v in reversed(sorted(collisions.items(), key=lambda item: item[1]))}

    return collisions_sorted


def total_collisions(collisions):
    total = sum(collisions[x] for x in collisions if collisions[x] != 0 and collisions[x] != 1)

    return total