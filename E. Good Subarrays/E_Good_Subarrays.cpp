#include<iostream>
#include<string>
#include<unordered_map>

using namespace std;

void helper(const string& s,const int& size){
    long long sum=0,total=0;
    unordered_map<int,int> freq;
    freq[0]++;
    for(int i=0;i<size;++i){
        sum+=(s[i]-'0')-1;
        total+=freq[sum];
        freq[sum]++;
    }
    cout<<total<<"\n";
}

int main(){
    int t;
    cin>>t;
    while (t--){
        int n;
        cin>>n;
        string s;
        cin>>s;
        helper(s,n);
    }
}