

def find_points_ort(query_x, query_y, line_x1, line_y1, line_x2, line_y2):
    # x, y = 0, 0
    k1 = ( line_y2 - line_y1 ) / (line_x2 - line_x1)
    k2 = -1/k1

    x = (k1 * line_x1 - k2 * query_x + query_y - line_y1) / ( k1 - k2 )
    y = k2 * (x - query_x) + query_y

    return (x, y)



def main():
    n = int(input())
    points_line = []
    for i in range(n):
        points_line.append(list(map(int, input().split())))

    q = int(input())
    points_query = []
    for i in range(q):
        points_query.append(list(map(int, input().split())))

    points_ort = []
    for i in range(q):
        x, y = find_points_ort(
            points_query[i][0],
            points_query[i][1],
            points_line[0][0],
            points_line[0][1],
            points_line[1][0],
            points_line[1][1]
        )
        points_ort.append([x, y])

    # print(points_ort)

    sorted_points_line = sorted(points_line)
    ans = []
    for i in range(len(points_ort)):
        shortestX, shortestY = float('inf'), float('inf')
        for j in range(len(sorted_points_line)):
            if points_ort[i][0] - sorted_points_line[j][0] < shortestX and points_ort[i][1] - sorted_points_line[j][1] < shortestY:
                shortestX = sorted_points_line[j][0]
                shortestY = sorted_points_line[j][1]
        ans.append([shortestX, shortestY])

    print(ans)










main()