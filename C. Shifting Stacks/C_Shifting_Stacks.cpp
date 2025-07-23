#include<iostream>
#include<vector>

using namespace std;

void helper(const vector<int>& arr){
    int n=arr.size();
    long long carry=0;
    for(int i=0;i<n;++i){
        if(carry+arr[i]<i){
            cout<<"NO\n";
            return;
        }
        carry+=(arr[i]-i);
    }
    cout<<"YES\n";
}

int main(){
    int test;
    cin>>test;
    for(int i=0;i<test;++i){
        int size;
        cin>>size;
        vector<int>heights(size);
        for(int j=0;j<size;++j) cin>>heights[j];
        helper(heights);
    }
}