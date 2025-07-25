#include<iostream>
#include<string>
#include<array>
using namespace std;

void helper(const string& s,const int& size){
    array<bool,26> alpha={};
    for(int i=0;i<size;++i){
        if(alpha[s[i]-'A']){
            cout<<"NO\n";
            return;
        }
        if((i<size-1 && s[i]==s[i+1]) || (i==size-1 && s[i-1]==s[i])) continue;
        alpha[s[i]-'A']=true;
    }
    cout<<"YES\n";
}

int main(){
    int test;
    cin>>test;
    while (test--){
        int size;
        cin>>size;
        string s;
        cin>>s;
        helper(s,size);
    }
}