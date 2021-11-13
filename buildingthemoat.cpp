/*#include<iostream>
#include<vector>
#include<algorithm>
#include<stack>
#include<cmath>
using namespace std;
typedef long double ld;

vector<pair<ld, ld >>points;
ld ccw(pair<ld, ld>a, pair<ld, ld >b, pair<ld, ld >c)
{
	return(b.first - a.first) * (c.second- a.second) - (c.first - a.first) * (b.second - a.second);
}
bool compare_y(pair<ld, ld >p1, pair<ld, ld >p2)
{
	if (p1.second != p2.second)
		return p1.second < p2.second;
	else
		return p1.first < p2.first;
}
bool compare_angle(pair<ld, ld >a, pair< ld, ld>b)
{
	ld cc = ccw(points[0], a, b);

	return cc > 0;

}
ld dist(pair<ld, ld>a, pair<ld, ld>b)
{
	ld dist = (b.first - a.first) * (b.first - a.first) + (b.second - a.second) * (b.second - a.second);
	return sqrt(dist);
}
int main()
{
	int n;
	ld  x, y;
	cin >> n;
	for (int i = 0; i < n; i++)
	{
		cin >> x >> y;
		points.push_back({ x,y });
	}

	sort(points.begin(), points.end(), compare_y);
	sort(points.begin()+1, points.end(), compare_angle);

	stack<pair<ld, ld >>s;
	s.push(points[0]);
	s.push(points[1]);
	ld distance = 0;
	for (int i = 2; i < n; i++)
	{
		while (s.size() >= 2)
		{
			pair<ld, ld > second;
			second = s.top();
			s.pop();
			pair<ld, ld > first;
			first = s.top();
			if (ccw(first, second, points[i]) > 0)
			{
				s.push(second);
				break;
			}
		}
		s.push(points[i]); 

	}
	pair<ld, ld> end = s.top();
	while(s.size()>1)
	{
		pair<ld, ld> first = s.top();
		s.pop();
		pair<ld, ld> second = s.top();
		distance += dist(first, second);

	}
	pair<ld, ld> start = s.top();
	distance += dist(start, end);
	cout.precision(2);
	cout << fixed << distance;
}*/