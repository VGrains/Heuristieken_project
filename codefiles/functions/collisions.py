def calculate_collisions(routes):
    collisions = {}
    for x in routes:
        collisions[x] = 0
        for y in routes[x]:
            for i in routes:
                if y in routes[i]:
                    collisions[x] += 1
                
    collisions_sorted = {k: v for k, v in reversed(sorted(collisions.items(), key=lambda item: item[1]))}

    return collisions_sorted