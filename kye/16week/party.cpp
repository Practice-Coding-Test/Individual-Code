#include<iostream>
#include<vector>
#include<algorithm>
#include<queue>
#include<climits>
using namespace std;

int n, m, x;
vector<pair<int, int>>weight[1001];
int dikstra(int start, int end)
{
	int d[1001];
	for (int i = 1; i <= n; i++)
	{
		d[i] = INT_MAX;
	}
	d[start] = 0;
	priority_queue<pair<int, int>,vector<pair<int,int>>, greater<>>pq;
	pq.push({ 0,start });
	while (!pq.empty())
	{
		int cur_node = pq.top().second;
		int cur_edge = pq.top().first;
		pq.pop();
		if (cur_edge > d[cur_node])
			continue;
		for (int i = 0; i < weight[cur_node].size(); i++)
		{
			if (d[weight[cur_node][i].second] > cur_edge + weight[cur_node][i].first)
			{
				d[weight[cur_node][i].second] = cur_edge + weight[cur_node][i].first;
				pq.push({ d[weight[cur_node][i].second],weight[cur_node][i].second });
			}
		}
	}
	return d[end];
}
int main()
{
	cin >> n >> m >> x;
	for (int i = 1; i <= m; i++)
	{
		int u, v, w;
		cin >> u >> v >> w;
		weight[u].push_back({ w,v });
	}
	int result;
	int ans = INT_MIN;
	for (int i = 1; i <= n; i++)
	{
		if (i == x)
			continue;
		result = dikstra(i, x) + dikstra(x, i);
		ans = max(ans, result);
	}
	cout << ans;
}
