points = []
distances = []
end = "COM"

with open('day6_input.txt', encoding="utf-8") as fich:
    orbits = [line.strip() for line in fich.readlines()]

orig_orbits = orbits[:]
# PART 1

for item in orbits:
    points.append(item.strip().split(')')[0])
    points.append(item.strip().split(')')[1])

while len(set(points)) > 1:
    print(orbits)
    points = []
    terminals = []
    index_to_pop = []

    for item in orbits:
        points.append(item.strip().split(')')[0])
        points.append(item.strip().split(')')[1])

    for point in set(points):
        count = points.count(point)
        print("Point: " + point + ". Count: " + str(count))
        if count == 1 and point != end:
            terminals.append(point)
            index_to_pop.append([i for i, s in enumerate(
                orbits) if ")"+point in s][0])
            index_to_pop.sort(reverse=True)
            print("Index to pop later: " + str(index_to_pop))

    for terminal in terminals:
        path = []
        print("\n" + terminal)
        while terminal != end:
            index = [i for i, s in enumerate(orbits) if ")"+terminal in s][0]
            print("Terminal: " + terminal + ". Index: " + str(index))
            print(orbits[index])
            path.append(terminal)
            terminal = orbits[index].strip().split(')')[0]
        path.append("COM")
        print("Path: " + str(path))
        distances.append(len(path)-1)
        print("Distances: " + str(distances))

    for item in index_to_pop:
        print("Pop: " + str(orbits[item]) + "\n")
        orbits.pop(item)

    terminals = []
    index_to_pop = []

print("Total of direct and indirect orbits: " + str(sum(distances)))


# PART 2

points = []
index = [i for i, s in enumerate(orig_orbits) if ")YOU" in s][0]
start = orig_orbits[index].strip().split(')')[0]
print("My orbit: " + str(start))
index = [i for i, s in enumerate(orig_orbits) if ")SAN" in s][0]
end = orig_orbits[index].strip().split(')')[0]
print("Santa's orbit: " + str(end))


for item in orig_orbits:
    points.append(item.strip().split(')')[0])
    points.append(item.strip().split(')')[1])


print(orbits)
points = []
terminals = []
path = [[], []]

for j in range(2):

    for item in orbits:
        points.append(item.strip().split(')')[0])
        points.append(item.strip().split(')')[1])

    for point in set(points):
        count = points.count(point)
        if point == start:
            terminals.append(point)

    for terminal in terminals:
        path[j] = []
        print("\n" + terminal)
        while terminal != "COM":
            index = [i for i, s in enumerate(orbits) if ")"+terminal in s][0]
            print("Terminal: " + terminal + ". Index: " + str(index))
            print(orbits[index])
            terminals.append(orbits[index].strip().split(')')[1])
            path[j].append(terminal)
            terminal = orbits[index].strip().split(')')[0]
        path[j].append("COM")
        print("Path: " + str(path[j]))
        distances.append(len(path[j])-1)
        print("Distances: " + str(distances))
        break

    terminals = []
    start = end

distance = (distances[0] - (len(set(path[0]) & set(path[1])) - 1)) + \
    (distances[1] - (len(set(path[0]) & set(path[1])) - 1))

print(distance)
