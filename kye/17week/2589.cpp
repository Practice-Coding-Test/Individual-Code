#include<iostream>
#include<vector>
#include<string>
#include<queue>
#include<algorithm>
using namespace std;

vector<string>map;
int w, h;
int xx[] = { 0,0,1,-1 };
int yy[] = { 1,-1,0,0 };
int bfs(int x, int y)
{
	int distance = 0;
	int visited[50][50] = { 0, };
	queue<pair<int,int>>q;
	q.push({ x,y });
	visited[x][y] = 1;
	while (!q.empty())
	{
		pair<int, int>temp;
		temp = q.front();
		q.pop();
		for (int i = 0; i < 4; i++)
		{
			int nx = temp.first + xx[i];
			int ny = temp.second + yy[i];
			if (nx < 0 || ny < 0 || nx >= h || ny >= w || visited[nx][ny] || map[nx][ny] == 'W')
				continue;
			visited[nx][ny] = visited[temp.first][temp.second] + 1;
			q.push({ nx,ny });
			distance = max(distance, visited[nx][ny]);
		}
	}
	return distance;
}
int main()
{
	cin >> h >> w;
	string s;
	for (int i = 0; i<h;i++)
	{
		cin >> s;
		map.push_back(s);
	}
	int result=0;
	for (int i = 0; i < h; i++)
	{
		for (int j = 0; j < w; j++)
		{
			if (map[i][j] == 'L')
			{
				result = max(result, bfs(i, j));
			}
		}
	}
	cout << result;
}
