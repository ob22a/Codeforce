#include<iostream>
#include<algorithm>
#include<vector>

using namespace std;

void helper(const vector<int>& red, const vector<int>& blue,const int& n,const int& m){
    vector<long long> preSum1(n+1);
    vector<long long> preSum2(m+1);
    for(int i=0;i<n;++i) preSum1[i+1]=preSum1[i]+red[i];
    for(int i=0;i<m;++i) preSum2[i+1]=preSum2[i]+blue[i];

    int sol=(*max_element(preSum1.begin(),preSum1.end())+(*max_element(preSum2.begin(),preSum2.end())));
    cout<<sol<<"\n";
}

int main(){
    int test;
    cin>>test;
    while(test--){
        int n;
        cin>>n;
        vector<int> r(n);
        for(int& num:r) cin>>num;
        int m;
        cin>>m;
        vector<int> b(m);
        for(int& num:b) cin>>num;
        helper(r,b,n,m);
    }
}