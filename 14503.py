# 로봇 청소기

N, M = map(int, input().split())
robot_x, robot_y, robot_pose = map(int, input().split())

# 북, 동, 남, 서
to_x = [0, 1, 0, -1]
to_y = [-1, 0, 1, 0]

# 빈칸 : 0, 벽돌 : 1

map_list = [list(map(int, input().split())) for i in range(N)]
print(map)

while True:
    robot_pose -= 1
    x = to_x[robot_pose]
    y = to_y[robot_pose]

    if map_list[robot_x+x][robot_y+y] == 0:
        robot_x += x
        robot_y += x
    else:
        continue