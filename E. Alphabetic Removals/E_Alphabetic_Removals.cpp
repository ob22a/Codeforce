#include<iostream>
#include<string>
#include<array>
using namespace std;

int main(){
    int size,k;
    cin>>size>>k;
    string s;
    cin>>s;

    array<int,26> freq={};
    for(char c:s) freq[c-'a']++;

    array<int,26> remaining=freq;

    for(int& f:remaining){
        if(k>=f){
            k-=f;
            f=0;
        }
        else{
            f-=k;
            k=0;
        }
        if(k==0) break;
    }

    string sol;
    for(char c:s){
        int idx=c-'a';
        if(remaining[idx]<freq[idx]) freq[idx]--;
        else sol+=c;
    }

    cout<<sol<<"\n";
}