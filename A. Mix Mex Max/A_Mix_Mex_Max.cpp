#include<iostream>
#include<vector>
#include<unordered_set>
using namespace std;

void helper(const vector<int>& nums,const int& size){
    unordered_set<int> exists;
    for(const int& num:nums){
        if(num!=-1){
            exists.insert(num);
        }
    }

    if(exists.empty() || (exists.size()<2 && exists.find(0)==exists.end())){
        cout<<"YES\n";
        return;
    }

    cout<<"NO\n";
}

int main(){
    int t;
    cin>>t;
    while (t--){
        int size;
        cin>>size;
        vector<int> num(size);
        for(int& x:num) cin>>x;
        helper(num,size);
    }
    
}