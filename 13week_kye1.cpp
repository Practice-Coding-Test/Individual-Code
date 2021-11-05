#include <iostream>
#include <vector>

using namespace std;

int main()
{
	int n;
	cin >> n;
	vector<int>v;
	v.push_back(-1);

	for (int i = 0; i < n; i++)
	{
		int num;
		cin >> num;
		if (v.back() < num)
		{
			v.push_back(num);
		}
		else if (v.back() > num)
		{
			auto low = lower_bound(v.begin(), v.end(), num) - v.begin();
			v[low] = num;

		}

	}
	cout << v.size() - 1;
}