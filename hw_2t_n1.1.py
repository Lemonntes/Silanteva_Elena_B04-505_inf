def your_code(n, tariffs):

    INF = 900000000000000000000
    dist = []
    for i in range(n):
        row = []
        for j in range(n):
            if tariffs[i][j] == -1:
                row.append(INF)
            else:
                row.append(tariffs[i][j])
        dist.append(row)

    
    for i in range(n):
        dist[i][i] = 0

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist

test_cases = [
        # Тест 1:
        {
            "n": 5,
            "tariffs": [[0, 10, -1, -1, 25], [-1, 0, 15, 5, -1], [-1, -1, 0, 8, 12], [20, -1, -1, 0, 10], [-1, 30, -1, -1, 0]],
            "expected": [[0, 10, 25, 15, 25], [25, 0, 15, 5, 15], [28, 38, 0, 8, 12], [20, 30, 45, 0, 10], [55, 30, 45, 35, 0]]
        },

        # Тест 2: Полносвязный
        {
            "n": 3,
            "tariffs": [[0,5,9],[16,0,12],[7,3,0]],
            "expected": [[0,5,9],[16,0,12],[7,3,0]]
        },
        # Тест 3: Недостижимые города
        {
            "n": 4,
            "tariffs": [[0,10,-1,-1],[-1,0,20,-1],[-1,-1,0,30],[-1,-1,-1,0]],
            "expected": [[0,10,30,60],[999999,0,20,50],[999999,999999,0,30],[999999,999999,999999,0]]
        }
    ]
def print_matrix(matrix):
    for row in matrix:
        print(' '.join(str(x) if x < 999999 else '-1' for x in row))

for i, test in enumerate(test_cases, 1):
    print(f"Тест {i}")
    print(f"n = {test['n']}")

    result = your_code(test['n'], test['tariffs'])

    print("Результат:")
    print_matrix(result)
    print("\nОжидаемый:")
    for row in test['expected']:
        print(' '.join(str(x) if x < 999999 else '-1' for x in row))
    print("-" * 60)
