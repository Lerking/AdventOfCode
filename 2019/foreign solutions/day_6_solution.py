#This is NOT my own solution.
import networkx as nx

orbit_map = nx.DiGraph()
orbits = [tuple(line.strip().split(")")) for line in open("day_6_input.txt", "r")]
orbit_map.add_edges_from(orbits)
part1 = sum([len(nx.ancestors(orbit_map, node)) for node in orbit_map.nodes()])
print(f"There are {part1} direct and indirect orbits")
part2 = nx.shortest_path_length(orbit_map.to_undirected(), "YOU", "SAN")-2
print(f"There are {part2} between YOU and SAN")