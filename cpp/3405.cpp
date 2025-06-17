#include <iostream>
#include <vector>
using namespace std;

const int MOD = 1e9 + 7;
const int MAX = 100000 + 10; // Adjust according to constraints

long long fact[MAX], inv_fact[MAX];

long long mod_pow(long long base, long long exp) {
    long long result = 1;
    base %= MOD;
    while (exp > 0) {
        if (exp & 1)
            result = (result * base) % MOD;
        base = (base * base) % MOD;
        exp >>= 1;
    }
    return result;
}

long long mod_inv(long long a) {
    return mod_pow(a, MOD - 2);
}

void precompute_factorials() {
    fact[0] = 1;
    for (int i = 1; i < MAX; ++i)
        fact[i] = fact[i - 1] * i % MOD;

    inv_fact[MAX - 1] = mod_inv(fact[MAX - 1]);
    for (int i = MAX - 2; i >= 0; --i)
        inv_fact[i] = inv_fact[i + 1] * (i + 1) % MOD;
}

long long nCr(int n, int r) {
    if (r > n || r < 0) return 0;
    return fact[n] * inv_fact[r] % MOD * inv_fact[n - r] % MOD;
}

class Solution {
public:
    int countGoodArrays(int n, int m, int k) {
        if (k > n - 1) return 0;
        precompute_factorials();

        long long ans = nCr(n - 1, k);
        ans = (ans * m) % MOD;
        ans = (ans * mod_pow(m - 1, n - 1 - k)) % MOD;
        return (int)ans;
    }
};
