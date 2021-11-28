/*#include <iostream>
#include<vector>

using namespace std;
int main()
{
	int m, p;
	
	vector < pair<int, int>>cost;
	cin >> m >> p;
	int size = 2 * p + 1;
	vector<int>dp(size, 0);
	cout << dp.size() << "\n";
	int start;
	int end;
	for (int i = 0; i < p; i++)
	{
		cin >> start >> end;
		cost.push_back({ start,end });

	}
	int month = 1;
	int s = 0;
	int e = 0;
	while(s<p || e<p)
	{
		while (dp[month]+cost[e].second<= 100 || dp[month]+cost[s].first<=100)
		{
			if (s > e)
			{
				dp[month] += cost[e].second;
				e++;
			}
			else
			{
				dp[month] += cost[s].first;
				s++;
			}
			if (s == p || e == p)
				break;
		}
		dp[month + 1] += dp[month];
		month++;
	
	}
	cout << month;
}*/