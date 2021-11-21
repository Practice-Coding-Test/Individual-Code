#include<iostream>
#include<vector>
#include<algorithm>
#include<climits>
using namespace std;

vector<pair<long long, int>>loc;//좌표는 1000000000까지 이니까 long long 타입
int main()
{
	int n;
	cin >> n;
	int x, sex;
	for (int i = 0; i < n; i++)
	{
		cin >> sex >> x;
		if (sex == 0)//누적합을 위해서 남자일때는 -1로 변경
			sex = -1;
		loc.push_back({ x,sex });
	}
	sort(loc.begin(), loc.end());//좌표를 기준으로 정렬
	vector<int>sum(n, 0);
	sum[0] = loc[0].second;
	for (int i = 1; i < n; i++)
	{
		sum[i] = sum[i - 1] + loc[i].second;//누적합 구하기
	}
	vector<long long>minimum(2 * 1000000 + 1, LLONG_MAX);
	vector<long long>maximum(2 * 1000000 + 1, LLONG_MIN);
	minimum[1000000] = -1;//인덱스가 0인 좌표에서의 계산을 위해 -1 처리 sum[i]==0 인것 중 가장 작은 인덱스가 0일때 대비
	vector<int>hash(2 * 1000000 + 1);
	for (long long i = 0; i < n; i++)
	{
		int idx = sum[i] + 1000000;//i번째 인덱스에서의 누적합의 해쉬값
		hash[idx] = true;//방문체크
		minimum[idx] = min(minimum[idx], i);//같은 누적합 중에서 가장 작은 idx
		maximum[idx] = max(minimum[idx], i);//같은 누적합 중에서 가장 큰 idx
	}
	long long result = 0;
	for (long long i = 0; i < 2 * 1000000 + 1; i++)
	{
		if (hash[i])//방문했다면
		{
			if (minimum[i] == maximum[i])
				continue;
			long long distance = loc[maximum[i]].first - loc[minimum[i] + 1].first;
			//누적합이 i인 좌표에서 가장 큰 인덱스와 가장 작은 인덱스 +1의 거리
			result = max(distance, result);// 가장 값이 큰 거리 구하기
		}
	}

	cout << result;

}