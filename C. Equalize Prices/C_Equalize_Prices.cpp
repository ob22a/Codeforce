#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;

void helper(const vector<int>& nums,const int& k,const int& size){
    int large=*max_element(nums.begin(),nums.end());
    int small=*min_element(nums.begin(),nums.end());
    if(small+k<large-k) cout<<-1<<"\n";
    else cout<<small+k<<"\n";
}

int main(){
    int test;
    cin>>test;
    while(test--){
        int n,k;
        cin>>n>>k;
        vector<int> nums(n);
        for(int& x:nums) cin>>x;
        helper(nums,k,n);
    }
}