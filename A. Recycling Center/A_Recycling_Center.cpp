#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

void helper(vector<int>& nums,const int& n,const int& c){
    sort(nums.begin(),nums.end());
    int i=0;
    while(i<n-1 && nums[i+1]<=c) i++;
    int count=0;
    int factor=1;
    for(int j=i;j>=0;--j){
        if(nums[j]*factor<=c){
            ++count; factor*=2;
        }
    }
    cout<<(n-count)<<"\n";
}

int main(){
    int t;
    cin>>t;
    while(t--){
        int n,c;
        cin>>n>>c;
        vector<int> nums(n);
        for(int& x:nums) cin>>x;
        helper(nums,n,c);
    }
}