import heapq

def your_code(n, m, s, t, edges):
    g = [[] for _ in range(n)]
    for u, v, dist in edges:
        g[u].append((v, dist))
    
    dist = [99999999999] * n
    dist[s] = 0
    aa = [-1] * n  
    aa[s] = s
    pq = [(0, s)]
    
    while pq:
        d, u = heapq.heappop(pq)
        if u == t:
            break
        if d > dist[u]:
            continue
        for v, w in g[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                aa[v] = u
                heapq.heappush(pq, (dist[v], v))
    
    
    if dist[t] == 99999999999:
        return "Ne mogu naiti marshrut! :'("  
    
    path = []
    curr = t
    while curr != s:
        path.append(curr)
        curr = aa[curr]
    path.append(s)
    revpath = []
    for i in range(len(path) - 1, -1, -1):
        revpath.append(path[i])

    return f"{dist[t]}\n{' '.join(map(str, revpath))}"

def test_gps_cases():
    tests = [
        # Тест 1:
        {
            "n": 8, "m": 8, "s": 0, "t": 7,
            "edges": [(0,1,600),(0,2,1200),(1,3,800),(2,3,400),(2,4,700),(3,5,500),(4,5,300),(5,7,900)],
            "answer": "2800\n0 1 3 5 7"
        },
        # Тест 2:
        {
            "n": 4, "m": 3, "s": 0, "t": 3,
            "edges": [(0,1,1),(1,2,1),(0,2,10)],
            "answer": "Ne mogu naiti marshrut! :'("
        },
        # Тест 3:
        {
            "n": 4, "m": 4, "s": 0, "t": 3,
            "edges": [(0,1,4),(0,3,12),(1,2,3),(2,3,5)],
            "answer": "12\n0 3"
        },
        # Тест 4:
        {
            "n": 1, "m": 0, "s": 0, "t": 0,
            "edges": [],
            "answer": "0\n0"
        },
        # Тест 5:
        {
            "n": 3, "m": 3, "s": 0, "t": 2,
            "edges": [(0,1,5),(0,2,12),(1,2,3)],
            "answer": "8\n0 1 2"
        }
    ]

    for i, test in enumerate(tests, 1):
        print(f"Тест {i}:")
        result = your_code(test["n"], test["m"], test["s"], test["t"], test["edges"])
        print(f"Ожидаемый: {test['answer']}")
        print(f"Получено:  {result}")
        print("-" * 50)

test_gps_cases()
