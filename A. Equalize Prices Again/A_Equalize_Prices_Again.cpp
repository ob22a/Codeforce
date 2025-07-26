#include<iostream>
#include<vector>
#include<numeric>
#include<algorithm>

using namespace std;

void helper(const vector<int>& prices,const int n){
    long long total=accumulate(prices.begin(),prices.end(),0ll);
    int sol=*max_element(prices.begin(),prices.end());
    while((sol*n)>=total) sol--;
    cout<<(sol+1)<<"\n";
}

int main(){
    int test;
    cin>>test;
    while(test--){
        int n;
        cin>>n;
        vector<int> prices(n);
        for(int& x:prices) cin>>x;
        helper(prices,n);
    }
}