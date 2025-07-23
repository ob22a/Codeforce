#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

int helper(vector<int> nums){
    int small=*min_element(nums.begin(),nums.end());
    int sol=0;
    for(int num:nums) sol+=abs(num-small);
    return sol;
}

int main(){
    int noTest;
    cin>>noTest;
    for(int i=0;i<noTest;++i){
        int size;
        cin>>size;
        vector<int> candies;
        for(int j=0;j<size;++j){
            int val;
            cin>>val;
            candies.push_back(val);
        }
        cout<<helper(candies)<<'\n';
    }
    return 0;
}