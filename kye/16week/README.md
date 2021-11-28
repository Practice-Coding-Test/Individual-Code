# Baekjoon
## 16week-1
https://www.acmicpc.net/problem/1238
N개의 숫자로 구분된 각각의 마을에 한 명의 학생이 살고 있다.

어느 날 이 N명의 학생이 X (1 ≤ X ≤ N)번 마을에 모여서 파티를 벌이기로 했다. 이 마을 사이에는 총 M개의 단방향 도로들이 있고 i번째 길을 지나는데 Ti(1 ≤ Ti ≤ 100)의 시간을 소비한다.

각각의 학생들은 파티에 참석하기 위해 걸어가서 다시 그들의 마을로 돌아와야 한다. 하지만 이 학생들은 워낙 게을러서 최단 시간에 오고 가기를 원한다.

이 도로들은 단방향이기 때문에 아마 그들이 오고 가는 길이 다를지도 모른다. N명의 학생들 중 오고 가는데 가장 많은 시간을 소비하는 학생은 누구일지 구하여라.

입력
첫째 줄에 N(1 ≤ N ≤ 1,000), M(1 ≤ M ≤ 10,000), X가 공백으로 구분되어 입력된다. 두 번째 줄부터 M+1번째 줄까지 i번째 도로의 시작점, 끝점, 그리고 이 도로를 지나는데 필요한 소요시간 Ti가 들어온다. 시작점과 끝점이 같은 도로는 없으며, 시작점과 한 도시 A에서 다른 도시 B로 가는 도로의 개수는 최대 1개이다.

모든 학생들은 집에서 X에 갈수 있고, X에서 집으로 돌아올 수 있는 데이터만 입력으로 주어진다.

출력
첫 번째 줄에 N명의 학생들 중 오고 가는데 가장 오래 걸리는 학생의 소요시간을 출력한다.
# Baekjoon
## 16week-2
https://www.acmicpc.net/problem/6214
In easier times, Farmer John's cows had no problems. These days, though, they have problems, lots of problems; they have P (1 <= P <= 300) problems, to be exact. They have quit providing milk and have taken regular jobs like all other good citizens.  In fact, on a normal month they make M (1 <= M <= 1000) money.

Their problems, however, are so complex they must hire consultants to solve them. Consultants are not free, but they are competent: consultants can solve any problem in a single month. Each consultant demands two payments: one in advance (1 <= payment <= M) to be paid at the start of the month problem-solving is commenced and one more payment at the start of the month after the problem is solved (1 <= payment <= M). Thus, each month the cows can spend the money earned during the previous month to pay for consultants. Cows are spendthrifts: they can never save any money from month-to-month; money not used is wasted on cow candy.

Since the problems to be solved depend on each other, they must be solved mostly in order. For example, problem 3 must be solved before problem 4 or during the same month as problem 4.

Determine the number of months it takes to solve all of the cows' problems and pay for the solutions.

입력
Line 1: Two space-separated integers: M and P.
Lines 2..P+1: Line i+1 describes problem i with two space-separated integers: B_i and A_i. B_i is the payment to the consult BEFORE the problem is solved; A_i is the payment to the consult AFTER the problem is solved.
 

출력
Line 1: The number of months it takes to solve and pay for all the cows' problems.
