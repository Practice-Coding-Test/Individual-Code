# Baekjoon
## 14week-1
https://www.acmicpc.net/problem/6198
도시에는 N개의 빌딩이 있다.

빌딩 관리인들은 매우 성실 하기 때문에, 다른 빌딩의 옥상 정원을 벤치마킹 하고 싶어한다.

i번째 빌딩의 키가 hi이고, 모든 빌딩은 일렬로 서 있고 오른쪽으로만 볼 수 있다.

i번째 빌딩 관리인이 볼 수 있는 다른 빌딩의 옥상 정원은 i+1, i+2, .... , N이다.

그런데 자신이 위치한 빌딩보다 높거나 같은 빌딩이 있으면 그 다음에 있는 모든 빌딩의 옥상은 보지 못한다.

예) N=6, H = {10, 3, 7, 4, 12, 2}인 경우

             = 
 =           = 
 =     -     = 
 =     =     =        -> 관리인이 보는 방향
 =  -  =  =  =   
 =  =  =  =  =  = 
10  3  7  4  12 2     -> 빌딩의 높이
[1][2][3][4][5][6]    -> 빌딩의 번호
1번 관리인은 2, 3, 4번 빌딩의 옥상을 확인할 수 있다.
2번 관리인은 다른 빌딩의 옥상을 확인할 수 없다.
3번 관리인은 4번 빌딩의 옥상을 확인할 수 있다.
4번 관리인은 다른 빌딩의 옥상을 확인할 수 없다.
5번 관리인은 6번 빌딩의 옥상을 확인할 수 있다.
6번 관리인은 마지막이므로 다른 빌딩의 옥상을 확인할 수 없다.
따라서, 관리인들이 옥상정원을 확인할 수 있는 총 수는 3 + 0 + 1 + 0 + 1 + 0 = 5이다.

# Baekjoon
## 14week-2
https://www.acmicpc.net/problem/6194
To repel the invading thirsty aardvarks, Farmer John wants to build a moat around his farm.  He owns N (8 <= N <= 5,000) watering holes, and will be digging the moat in a straight line between pairs of them.  His moat should protect (i.e., surround) all his watering holes; every watering hole must be on or inside the moat, and the moat must form a closed loop.

Digging a moat is expensive work, and frugal FJ wants his moat to have the minimum length possible.  Find the length of the shortest moat he can construct.

The unique holes are each located at integer coordinates in the range (1..45,000, 1..45,000). FJ has noticed that no three watering holes lie along the same line.

Consider this grid where the 20 '*'s represent watering holes:

...*-----------------*......
../..........*........\.....
./.....................\....
*......................*\...
|..........*........*....\..
|*........................\.
|..........................*
*..........................|
.\*........................|
..\.....................*..|
...\........*............*.|
....\..................*...*
.....\..*..........*....../.
......\................../..
.......*----------------*...
The enclosing lines are the shortest possible path that can enclose this set of watering holes.

The line displacements, starting with the top line are: (18,0), (6,-6), (0,-5), (-3,-3), (-17,0), (-7,7), (0,4), and (3,3).  This yields a distance of 70.8700576850888(...). Our output will print only two decimal places, so the distance will be reported as 70.87.


