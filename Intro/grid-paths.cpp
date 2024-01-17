#include <iostream>
#include <vector>

using namespace std;

#define isValid(a) (a>=0 && a<7 ? 1 : 0)

#define LEFT 0
#define UP 1
#define RIGHT 2
#define DOWN 3

string st;

int x[4] = {0, -1, 0, 1};
int y[4] = {-1, 0, 1, 0};

int p[48];

bool vis[7][7];

int solve(int row, int col, int idx) {
    if (idx == st.length()) {
        return (row == 6 && col == 0);
    }

    if (row == 6 && col == 0) {
        return 0;
    }

    if (vis[row][col]) {
        return 0;
    }

    bool visited[4];

    for (int i = 0; i < 4; ++i) {
        if (isValid(row + x[i]) && isValid(col + y[i])) {
            visited[i] = vis[row + x[i]][col + y[i]];
        }
    }

    if (!visited[LEFT] && !visited[RIGHT] && visited[UP] && visited[DOWN]) {
        return 0;
    }

    if (!visited[UP] && !visited[DOWN] && visited[LEFT] && visited[RIGHT]) {
        return 0;
    }

    if (isValid(row-1) && isValid(col-1) && vis[row-1][col-1]) {
        if (!visited[LEFT] && !visited[UP]) {
            return 0;
        }
    }

    if (isValid(row-1) && isValid(col+1) && vis[row-1][col+1]) {
        if (!visited[UP] && !visited[RIGHT]) {
            return 0;
        }
    }

    if (isValid(row+1) && isValid(col-1) && vis[row+1][col-1]) {
        if (!visited[LEFT] && !visited[DOWN]) {
            return 0;
        }
    }

    if (isValid(row+1) && isValid(col+1) && vis[row+1][col+1]) {
        if (!visited[RIGHT] && !visited[DOWN]) {
            return 0;
        }
    }

    vis[row][col] = true;

    int ans = 0;

    if (st[idx] == '?') {
        for (int i = 0; i < 4; ++i) {
            if (isValid(row+x[i]) && isValid(col+y[i])) {
                ans += solve(row + x[i], col + y[i], idx + 1);
            }
        }
    } else {
        if (p[idx] < 4) {
		int nxtR = row + x[p[idx]];
		int nxtC = col + y[p[idx]];
		if (isValid(nxtR) && isValid(nxtC)) ans += solve(nxtR, nxtC, idx+1);
	}
    }

    vis[row][col] = false;

    return ans;
}

int main() {
    cin >> st;

    for (int i = 0; i < 48; i++) {
		char cur = st[i];

		if (cur == 'L') p[i] = 0;
		else if (cur == 'U') p[i] = 1;
		else if (cur == 'R') p[i] = 2;
		else if (cur == 'D') p[i] = 3;
		else p[i] = 4;  // cur == '?'
	}
    cout << solve(0, 0, 0) << endl;

    return 0;
}
