#include<vector>
#include<iostream>
#include<climits>
#include<string>
#include<algorithm>

using namespace std;

vector<string> solution(vector<vector<int>>line)
{
	vector<pair<long long, long long>>cross;
	long long x, y;
	long long minx = LLONG_MAX, miny = LLONG_MAX, maxx = LLONG_MIN, maxy = LLONG_MIN;

	for (int i = 0; i < line.size(); i++)
	{
		for (int j = i + 1; j < line.size(); j++)
		{
			long long a = line[i][0], b = line[i][1], e = line[i][2];
			long long c = line[j][0], d = line[j][1], f = line[j][2];
			long long under = line[i][0] * line[j][1] * 1LL - line[i][1] * line[j][0] * 1LL;
			if (under == 0)//i번째 직선과 j번째 직선이 평행이거나 일치하는 경우
				continue;
			if ((b * f * 1LL - e * d * 1LL) % under ||
				(e * c * 1LL - a * f * 1LL) % under)//정수 교점만 찾기
			{
				continue;
			}
			x = (b * f * 1LL - e * d * 1LL) / under;
			y = (e * c * 1LL - a * f * 1LL) / under;

			cross.push_back({ x,y });
			minx = min(x, minx);
			maxx = max(x, maxx);
			miny = min(y, miny);
			maxy = max(y, maxy);
		}
	}

	string a = string(maxx - minx + 1, '.');
	vector<string>answer(maxy - miny + 1, a);
	for (auto i : cross)
	{
		answer[abs(i.second - maxy)][abs(i.first - minx)] = '*';//""와 ''의 차이
	}

	return answer;

}
int main()
{
	vector<vector<int>>line;
	for (int i = 0; i < 5; i++)
	{
		int a, b, c;
		cin >> a >> b >> c;
		line.push_back({ a,b,c });
	}
	solution(line);
}
