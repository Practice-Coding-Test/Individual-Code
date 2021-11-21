#include <iostream>
#include<vector>
#include<climits>
#include<cmath>

using namespace std;

int map[50][50];
vector<pair<int, int>>home;
vector<pair<int, int>>chicken;
vector<pair<int, int>>select_chicken;
int n, m;
int result, dist, ans, dist_city;
int selected[2500] = { 0, };
int checkdist()
{
	ans = 0;
	pair<int, int> temp;
	for (int i = 0; i < chicken.size(); i++)
	{
		if (selected[i])
		{
			select_chicken.push_back({ chicken[i].first,chicken[i].second });
			//cout << chicken[i].first << " " << chicken[i].second << "\n";
		}
	}
	for (int i = 0; i < home.size(); i++)
	{
		result = INT_MAX;
		temp = home[i];
		for (int j = 0; j < m; j++)
		{
			dist = abs(temp.first - select_chicken[j].first) + abs(temp.second - select_chicken[j].second);
			result = min(result, dist);
		}
		ans += result;

	}
	//cout << "조합별 최소거리" << ans << "\n";
	select_chicken.clear();
	return ans;
}
void combination(int idx, int cnt)
{
	if (cnt == m)
	{
		dist_city = min(dist_city, checkdist());
		return;
	}
	for (int i = idx; i < chicken.size(); i++)
	{
		if (selected[i])
			continue;
		selected[i] = 1;
		combination(i + 1, cnt + 1);
		selected[i] = 0;
	}
	return;
}
int main()
{
	cin >> n >> m;
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < n; j++)
		{
			cin >> map[i][j];
			if (map[i][j] == 1)
				home.push_back({ i,j });
			if (map[i][j] == 2)
				chicken.push_back({ i,j });
		}
	}
	dist_city = INT_MAX;
	combination(0, 0);
	cout << dist_city;
}