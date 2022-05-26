def drawUF(a):
    dot = gv.Digraph(comment='Nada')
    n = len(a)
    for i in range(n):
        dot.node(str(i), str(i))
    for i in range(n):
        if i != a[i]:
            dot.edge(str(i), str(a[i]))
    dot.graph_attr['rankdir'] = 'BT'
    return dot
