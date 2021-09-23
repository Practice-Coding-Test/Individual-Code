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
	//���ڸ� ���ڷ� ��ȯ�ϴ� �Լ�
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
		//��������� �帣�ϱ� ���� ������� �ش�.
		graph[a].push_back(b);
		graph[b].push_back(a);
		capacity[a][b] += f;//=f�ƴϰ� �� ���ؾ��Ѵ�...�Ȱ��� ����ȣ ���� �ʴ´ٰ� �� ���� �����ϱ�......
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
			if (u == dest)//���� ��忡 ���������� ��
				break;
			for (int i = 0; i < graph[u].size(); i++)
			{
				int v = graph[u][i];
				if ((parent[v] == -1) && (capacity[u][v] - flow[u][v] > 0))//���� ��μ��� �ȵǾ��ְ�, �뷮�� ���� �ִٸ�
				{
					parent[v] = u;//v�� �θ���� u
					q.push(v);
				}
			}
		}
		if (parent[dest] == -1)//���� �������� ���� ���ߴٸ� ��ΰ� ���ٴ� ��
			break;


		//�带 �� �ִ� �ּ� ������ ã�´�
		int minflow = 987654321;
		for (int i = dest; i != start; i = parent[i])//�θ��带 ã�ư���
		{
			minflow = min(minflow, capacity[parent[i]][i] - flow[parent[i]][i]);//���� �ּҿ뷮�� ã�´�
		}
		for (int i = dest; i != start; i = parent[i])
		{
			flow[parent[i]][i] += minflow;//���ݱ��� �帥 �� �����ش�
			flow[i][parent[i]] -= minflow;//�ڽĳ�忡�� �θ���δ� ���� ���� �����ش�.
		}
		result += minflow;
	}
	cout << result;
}