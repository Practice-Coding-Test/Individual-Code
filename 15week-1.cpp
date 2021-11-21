#include<iostream>
#include<vector>
#include<algorithm>
#include<climits>
using namespace std;

vector<pair<long long, int>>loc;//��ǥ�� 1000000000���� �̴ϱ� long long Ÿ��
int main()
{
	int n;
	cin >> n;
	int x, sex;
	for (int i = 0; i < n; i++)
	{
		cin >> sex >> x;
		if (sex == 0)//�������� ���ؼ� �����϶��� -1�� ����
			sex = -1;
		loc.push_back({ x,sex });
	}
	sort(loc.begin(), loc.end());//��ǥ�� �������� ����
	vector<int>sum(n, 0);
	sum[0] = loc[0].second;
	for (int i = 1; i < n; i++)
	{
		sum[i] = sum[i - 1] + loc[i].second;//������ ���ϱ�
	}
	vector<long long>minimum(2 * 1000000 + 1, LLONG_MAX);
	vector<long long>maximum(2 * 1000000 + 1, LLONG_MIN);
	minimum[1000000] = -1;//�ε����� 0�� ��ǥ������ ����� ���� -1 ó�� sum[i]==0 �ΰ� �� ���� ���� �ε����� 0�϶� ���
	vector<int>hash(2 * 1000000 + 1);
	for (long long i = 0; i < n; i++)
	{
		int idx = sum[i] + 1000000;//i��° �ε��������� �������� �ؽ���
		hash[idx] = true;//�湮üũ
		minimum[idx] = min(minimum[idx], i);//���� ������ �߿��� ���� ���� idx
		maximum[idx] = max(minimum[idx], i);//���� ������ �߿��� ���� ū idx
	}
	long long result = 0;
	for (long long i = 0; i < 2 * 1000000 + 1; i++)
	{
		if (hash[i])//�湮�ߴٸ�
		{
			if (minimum[i] == maximum[i])
				continue;
			long long distance = loc[maximum[i]].first - loc[minimum[i] + 1].first;
			//�������� i�� ��ǥ���� ���� ū �ε����� ���� ���� �ε��� +1�� �Ÿ�
			result = max(distance, result);// ���� ���� ū �Ÿ� ���ϱ�
		}
	}

	cout << result;

}