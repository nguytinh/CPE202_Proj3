from functions import Graph

g = Graph()

g.addVertex('Kevin Bacon')
g.addVertex('Tom Hanks')
g.addVertex('Bill Paxton')
g.addVertex('Paul Herbert')
g.addVertex('Yves Aubert')
g.addVertex('Shane Zaza')
g.addVertex('Seretta Wilson')
g.addVertex('Meryl Streep')
g.addVertex('John Beluci')
g.addVertex('Kathleen Quinlan')
g.addVertex('Donald Sutherland')
g.addVertex('Lloyd Bridges')
g.addVertex('Grace Kelly')
g.addVertex('Nicole Kidman')
g.addVertex('Patrick Allen')
g.addVertex('Glenn Close')
g.addVertex('John Gielgud')
g.addVertex('Vernon Dobtcheff')
g.addVertex('Kate Winslet')

g.addBiEdge('Kevin Bacon', 'John Belushi')
g.addBiEdge('Kevin Bacon', 'Meryl Streep')
g.addBiEdge('Kevin Bacon', 'Donald Sutherland')
g.addBiEdge('Kevin Bacon', 'Tom Hanks')
g.addBiEdge('Kevin Bacon', 'Bill Paxton')
g.addBiEdge('Kevin Bacon', 'Kathleen Quinlan')
g.addBiEdge('John Belushi', 'Donald Sutherland')
g.addBiEdge('Donald Sutherland', 'Nicole Kidman')
g.addBiEdge('Donald Sutherland', 'Patrick Allen')
g.addBiEdge('Grace Kelly', 'Patrick Allen')
g.addBiEdge('Grace Kelly', 'Lloyd Bridges')
g.addBiEdge('Tom Hanks', 'Lloyd Bridges')
g.addBiEdge('Tom Hanks', 'Bill Paxton')
g.addBiEdge('Tom Hanks', 'Kathleen Quinlan')
g.addBiEdge('Tom Hanks', 'Paul Herbert')
g.addBiEdge('Tom Hanks', 'Yves Aubert')
g.addBiEdge('Tom Hanks', 'Shane Zaza')
g.addBiEdge('Tom Hanks', 'Serretta Wilson')
g.addBiEdge('Kathleen Quinlan', 'Bill Paxton')
g.addBiEdge('Paul Herbert', 'Bill Paxton')
g.addBiEdge('Paul Herbert', 'Serretta Wilson')
g.addBiEdge('Paul Herbert', 'Shane Zaza')
g.addBiEdge('Paul Herbert', 'Yves Aubert')
g.addBiEdge('Yves Aubert', 'Serretta Wilson')
g.addBiEdge('Shane Zaza', 'Serretta Wilson')
g.addBiEdge('Shane Zaza', 'Yves Aubert')
g.addBiEdge('Kate Winslet', 'Bill Paxton')
g.addBiEdge('Kate Winslet', 'Paul Herbert')
g.addBiEdge('Kate Winslet', 'Vernom Dobtcheff')
g.addBiEdge('Kate Winslet', 'John Gielgud')
g.addBiEdge('Patrick Allen', 'John Gielgud')
g.addBiEdge('John Gielgud', 'Vernom Dobtcheff')
g.addBiEdge('Donald Sutherland', 'Vernom Dobtcheff')
g.addBiEdge('Glenn Close', 'Nicole Kidman')
g.addBiEdge('John Gielgud', 'Nicole Kidman')

#this vertex is added to test if a vertex exists but has no connections
g.addVertex('Tinh-Phong Nguyen')


def bacon_degree(name):
    starting_vertex = g.getVertex('Kevin Bacon')
    all_paths = g.shortest_path(starting_vertex)
    exists = False
    connected = False

    if name in g.vertList:
        exists = True

    for p in all_paths:
        if p[0] == name:
            connected = True
            return p[2]

    if exists == True and connected == False:
        return "Vertex exists but there are no connections to Kevin Bacon"

def highest_bacon_num():
    starting_vertex = g.getVertex('Kevin Bacon')
    all_paths = g.shortest_path(starting_vertex)
    ls = []
    greatest = 0

    for i in all_paths:
        if i[2] > greatest:
            greatest = i[2]
    for k in all_paths:
        if k[2] == greatest:
            ls.append(k[0])
    return ls

def actor_link(name1, name2):
    starting_vertex = g.getVertex(name1)
    all_paths = g.shortest_path(starting_vertex)
    exists = False
    connected = False

    if name1 in g.vertList and name2 in g.vertList:
        exists = True

    for p in all_paths:
        if p[0] == name2:
            connected = True
            return p[2]

    if exists == True and connected == False:
        return "Vertecies exists but there are no connections between them"


