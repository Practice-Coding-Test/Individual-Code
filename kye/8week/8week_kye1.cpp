#include <iostream>
#include <vector>
#include <queue>
#include <cstring>
#include <algorithm>

using namespace std;

vector<int>graph[53];
int capacity[53][53];
int flow[53][53];
int parent[53];

char trans(char a)
{
	//문자를 숫자로 변환하는 함수
	if (a <= 'Z')
		return a - 'A';
	else
		return a - 'a' + 26;
}
int main()
{
	memset(capacity, 0, sizeof(capacity));
	memset(flow, 0, sizeof(flow));
	int result = 0;
	char a, b;
	int f;
	int n;
	cin >> n;
	for (int i = 0; i < n; i++)
	{
		cin >> a >> b >> f;

		a = trans(a);
		b = trans(b);
		//양방향으로 흐르니까 서로 연결시켜 준다.
		graph[a].push_back(b);
		graph[b].push_back(a);
		capacity[a][b] += f;//=f아니고 꼭 더해야한다...똑같은 노드번호 주지 않는다고 한 말이 없으니까......
		capacity[b][a] += f;
	}
	int start = trans('A');
	int dest = trans('Z');
	while (1)
	{
		memset(parent, -1, sizeof(parent));
		queue<int>q;
		q.push(start);
		while (!q.empty())
		{
			int u = q.front();
			q.pop();
			if (u == dest)//도착 노드에 도착했으면 끝
				break;
			for (int i = 0; i < graph[u].size(); i++)
			{
				int v = graph[u][i];
				if ((parent[v] == -1) && (capacity[u][v] - flow[u][v] > 0))//아직 경로선택 안되어있고, 용량이 남아 있다면
				{
					parent[v] = u;//v의 부모노드는 u
					q.push(v);
				}
			}
		}
		if (parent[dest] == -1)//만약 종점까지 가지 못했다면 경로가 없다는 것
			break;


		//흐를 수 있는 최소 유량을 찾는다
		int minflow = 987654321;
		for (int i = dest; i != start; i = parent[i])//부모노드를 찾아간다
		{
			minflow = min(minflow, capacity[parent[i]][i] - flow[parent[i]][i]);//남은 최소용량을 찾는다
		}
		for (int i = dest; i != start; i = parent[i])
		{
			flow[parent[i]][i] += minflow;//지금까지 흐른 양 더해준다
			flow[i][parent[i]] -= minflow;//자식노드에서 부모노드로는 음의 값을 더해준다.
		}
		result += minflow;
	}
	cout << result;
}
