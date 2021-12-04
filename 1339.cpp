/*#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<cmath>
using namespace std;

vector<string>words;
vector<long long>alpha;
int selected[27];
long long sum = 0;
bool compare(long long & a,long long & b)
{
	return a> b;
}
int main()
{
	int n;
	cin >> n;
	for (int i = 0; i < n; i++)
	{
		string word;
		cin >> word;
		words.push_back(word);
	}
	fill(selected, selected + 27, -1);
	alpha.assign(27,0);
	for (int i = 0; i < words.size(); i++)
	{
		for (int j = 0; j < words[i].size(); j++)
		{
			alpha[words[i][j] - 'A']+=pow(10,words[i].size()-j-1);
		}
	}
	sort(alpha.begin(), alpha.end(),compare);
	int num = 9;
	for (int i = 0; i < alpha.size(); i++)
	{
		if (alpha[i] == 0)
			break;
		sum += num * alpha[i];
		num--;

	}
	cout << sum;
}*/