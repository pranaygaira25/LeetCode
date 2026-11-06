class Seg {
public:
    int mi, ma, best;
    Seg *left, *right;

    Seg(vector<int>& A, int l, int r) {
        mi = A[l];
        ma = A[r];
        best = 0;
        left = right = nullptr;

        if (l != r) {
            int m = (l + r) / 2;
            left = new Seg(A, l, m);
            right = new Seg(A, m + 1, r);
        }
    }

    void update(int pos, int val) {
        if (pos < mi || pos > ma) return;
        best = max(best, val);
        if (left) left->update(pos, val);
        if (right) right->update(pos, val);
    }

    int query(int l, int r) {
        if (r < mi || l > ma) return 0;
        if (l <= mi && ma <= r) return best;
        return max(left->query(l, r), right->query(l, r));
    }
};

class Solution {
public:
    vector<int> maxActiveSectionsAfterTrade(string s, vector<vector<int>>& queries) {
        int n = s.size();

        vector<int> le(n), ri(n);

        le[0] = 0;
        for (int i = 1; i < n; i++) {
            if (s[i] == s[i - 1])
                le[i] = le[i - 1];
            else
                le[i] = i;
        }

        ri[n - 1] = n - 1;
        for (int i = n - 2; i >= 0; i--) {
            if (s[i] == s[i + 1])
                ri[i] = ri[i + 1];
            else
                ri[i] = i;
        }

        auto canApply = [&](int l, int r) {
            if (l < 0 || r >= n || l >= r) return false;
            return le[l] != le[r];
        };

        auto queryLeftMost = [&](int l, int r) {
            int res = ri[l] - l + 1;
            l = ri[ri[l] + 1] + 1;
            res += min(r, ri[l]) - l + 1;
            return res;
        };

        auto queryRightMost = [&](int l, int r) {
            int res = r - le[r] + 1;
            r = le[le[r] - 1] - 1;
            res += r - max(l, le[r]) + 1;
            return res;
        };

        vector<int> pos, vals;

        for (int i = 0; i < n; i++) {
            if (i && s[i] == s[i - 1]) continue;
            if (s[i] == '1') continue;

            pos.push_back(i);
            vals.push_back(ri[i] - le[i] + 1);
        }

        int ones = count(s.begin(), s.end(), '1');

        if (pos.size() <= 1)
            return vector<int>(queries.size(), ones);

        for (int i = 0; i + 1 < (int)vals.size(); i++)
            vals[i] += vals[i + 1];

        Seg* seg = new Seg(pos, 0, (int)pos.size() - 1);

        for (int i = 0; i < (int)vals.size(); i++)
            seg->update(pos[i], vals[i]);

        vector<int> ans;

        for (auto& q : queries) {
            int l = q[0];
            int r = q[1];

            if (s[l] == '1')
                l = ri[l] + 1;

            if (s[r] == '1')
                r = le[r] - 1;

            if (canApply(l, r)) {
                int best = max(queryLeftMost(l, r), queryRightMost(l, r));

                l = ri[ri[l] + 1] + 1;
                r = le[le[r] - 1] - 1;

                if (l <= r && le[l] != le[r])
                    best = max(best, seg->query(l, le[r] - 1));

                ans.push_back(ones + best);
            } else {
                ans.push_back(ones);
            }
        }

        return ans;
    }
};