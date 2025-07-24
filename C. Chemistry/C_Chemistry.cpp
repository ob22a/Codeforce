#include<iostream>
#include<string>
#include<array>

using namespace std;

void helper(const string& s,const int& k,const int& size){
    array<int,26> alpha={};
    for(char c:s) alpha[c-'a']++;
    int odd=0;
    for(int freq:alpha){
        if(freq%2!=0) odd++;
    }
    if(odd-k<=1) cout<<"YES";
    else cout<<"NO";
    cout<<"\n";
}

int main(){
    int test;
    cin>>test;
    while(test--){
        int size,k;
        cin>>size>>k;
        string s;
        cin>>s;
        helper(s,k,size);
    }
}