#include<iostream>
#include<stack>
#include<algorithm>

using namespace std;

int main()
{
	stack<pair<long long int,int>>s;
	int n;
	cin >> n;
	long long int num;
	long long int sum = 0;
	long long int i = 1;
	for (i = 1; i <= n; i++)
	{
		cin >> num;
		if (s.empty() || s.top().first > num)
		{
			s.push({ num,i });
			continue;
		}
		while (!s.empty()&&s.top().first <= num)
		{
			long long int idx = s.top().second;
			s.pop();
			sum += i - idx - 1;
		}
		s.push({ num,i });
		
	}
	while (!s.empty())
	{
		int idx = s.top().second;
		s.pop();
		sum += i - idx - 1;

	}
	cout << sum << "\n";
}
