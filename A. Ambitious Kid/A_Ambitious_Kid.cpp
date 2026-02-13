#include<iostream>
#include<vector>
using namespace std;

int main(){
    int t;
    cin>>t;
    vector<int> nums(t);
    for(int& num:nums) cin>>num;

    int sol = INT_MAX;
    for(int num:nums) sol = min(sol,abs(num));

    cout<<sol<<endl;
}