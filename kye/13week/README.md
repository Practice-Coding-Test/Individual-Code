# Baekjoon
## 13week-1
https://www.acmicpc.net/problem/6192
The cows have been busily baking pies that contain gold coins! Each pie has some number Ni (1 <= Ni <= 25) of gold coins and is neatly labeled on its crust with the number of gold coins inside.

The cows have placed the pies very precisely in an array of R rows and C columns (1 <= R <= C <= 100) out in the pasture.  You have been placed in the pasture at the location (R=1,C=1) and have gathered the gold coins in that pie. You must make your way to the other side of the pasture, moving one column closer to the end point (which is location (R,C)) with each move you make. As you step to the new column, you may stay on the same row or change your row by no more than 1 (i.e., from (r,c) you can move to (r-1,c+1), (r, c+1), or (r+1,c+1).  Of course, you would not want to leave the field and fail to get some gold coins, and you must end up at (R,C).

Given a map of the pasture, what is the greatest number of gold coins you can gather?

By way of example, consider this field of gold-bearing cow pies:

start-> 6 5 3 7 9 2 7
        2 4 3 5 6 8 6
        4 9 9 9 1 5 8 <-end
Here's one path:

start-> 6 5 3 7 9 2 7
         \
        2 4 3 5 6 8 6
           \   / \
        4 9 9-9 1 5-8 <-end
The path above yields 6+4+9+9+6+5+8 = 47 gold coins. The path below is even better and yields 50 coins, which is the best possible:

start->6 5 3 7 9 2 7
         \
        2 4 3 5 6-8 6
           \   /   \
        4 9 9-9 1 5 8 <-end
# Programmers
## 13week-2
https://programmers.co.kr/learn/courses/30/lessons/87377

Ax + By + C = 0으로 표현할 수 있는 n개의 직선이 주어질 때, 이 직선의 교점 중 정수 좌표에 별을 그리려 합니다.

예를 들어, 다음과 같은 직선 5개를

2x - y + 4 = 0
-2x - y + 4 = 0
-y + 1 = 0
5x - 8y - 12 = 0
5x + 8y + 12 = 0
좌표 평면 위에 그리면 아래 그림과 같습니다.


이때, 모든 교점의 좌표는 (4, 1), (4, -4), (-4, -4), (-4, 1), (0, 4), (1.5, 1.0), (2.1, -0.19), (0, -1.5), (-2.1, -0.19), (-1.5, 1.0)입니다. 이 중 정수로만 표현되는 좌표는 (4, 1), (4, -4), (-4, -4), (-4, 1), (0, 4)입니다.

만약 정수로 표현되는 교점에 별을 그리면 다음과 같습니다.


위의 그림을 문자열로 나타낼 때, 별이 그려진 부분은 *, 빈 공간(격자선이 교차하는 지점)은 .으로 표현하면 다음과 같습니다.

"..........."  
".....*....."  
"..........."  
"..........."  
".*.......*."  
"..........."  
"..........."  
"..........."  
"..........."  
".*.......*."  
"..........."  
이때 격자판은 무한히 넓으니 모든 별을 포함하는 최소한의 크기만 나타내면 됩니다.

따라서 정답은

"....*...."  
"........."  
"........."  
"*.......*"  
"........."  
"........."  
"........."  
"........."  
"*.......*"  
입니다.

직선 A, B, C에 대한 정보가 담긴 배열 line이 매개변수로 주어집니다. 이때 모든 별을 포함하는 최소 사각형을 return 하도록 solution 함수를 완성해주세요.
