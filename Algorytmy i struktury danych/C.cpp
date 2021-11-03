#include <bits/stdc++.h>

using namespace std;
int n, p, m;
char ch;
int zl[1055], dp[10555], dp2[1055];
int ost2[1055][55];
vector<int>vec, vec2;
vector<int>good[55];
int main() {
	ios_base::sync_with_stdio(0);

	cin >> n >> p >> m;
	for (int i = 1; i <= p; i++) {
		int cnt = 0;
		int pot = 1;
		for (int i = 1; i <= 9; i++) {
			cin >> ch;
			int pom = 0;
			if (ch == 'x') {
				pom++;
			}
			cnt += (pot * pom);
			pot *= 2;
		}
		zl[cnt]++;
	}

	for (int i = 0; i < (1 << 10); i++) {
		vec.clear();
		int a = i;
		while (a != 0) {
			vec.push_back(a % 2);
			a /= 2;
		}
		while (vec.size() < 10) {
			vec.push_back(0);
		}

		int var = i;

		for (int j = 0; j < (1 << 5); j++) {
			vec2.clear();
			a = j;
			while (a != 0) {
				vec2.push_back(a % 2);
				a /= 2;
			}
			while (vec2.size() < 5) {
				vec2.push_back(0);
			}

			int var2 = j;

			int cnt = 0;
			int cnt2 = 0;

			int it1 = 9;
			int it2 = 4;
			int licz = 1;
			while (licz <= 15) {
				cnt *= 2;
				if (licz % 3 == 1) {
					cnt += vec2[it2--];
				}
				else cnt += vec[it1--];

				if (licz % 3 != 0) {
					cnt2 *= 2;
					if (licz % 3 == 1) {
						cnt2 += vec2[it2 + 1];
					}
					else cnt2 += vec[it1 + 1];
				}
				licz++;
			}

			ost2[var][var2] = cnt2;

			dp[var] = 1;

			int check1 = cnt;
			check1 /= (1<<6);
			int check2 = cnt % (1<<12);
			check2 /= (1<<3);
			int check3 = cnt % (1<<9);

			if (zl[check1] == 0 && zl[check2] == 0 && zl[check3] == 0) {
				good[var2].push_back(var);
			}
		}
	}

	for (int i = 3; i <= n; i++) {
		for (int j = 0; j < (1 << 5); j++) {
			for (int k = 0; k < good[j].size(); k++) {
				int kand = good[j][k];
				dp2[ost2[kand][j]] += dp[kand];
				dp2[ost2[kand][j]] %= m;
			}
		}
		for (int j = 0; j < (1 << 10); j++) {
			dp[j] = dp2[j];
			dp2[j] = 0;
		}

	}

	int ans = 0;
	for (int j = 0; j < (1 << 10); j++) {
		ans += dp[j];
		ans %= m;
	}

	cout << ans;
}