#include <iostream>
#include <string>
#include <vector>

using namespace std;

void helper(string s) {
    int n = s.size();
    bool ans[26]={};
    int i = 0;

    while (i < n) {
        int j=i;
        while (j < n && s[j] == s[i]) j++;
        if((j-i)%2==1) {
            ans[s[i]-'a'] = true;
        }
        i = j;
    }

    for (int k=0; k<26; ++k) {
        if (ans[k]) cout<< (char)(k + 'a');
    }
    cout << '\n';
}

int main() {
    int test;
    cin >> test;
    while (test--) {
        string text;
        cin >> text;
        helper(text);
    }
}
