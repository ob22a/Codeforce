#include<iostream>
using namespace std;
int main(){
    int n;
    cin>>n;
    int i=0;
    for(i;i<n;++i){
        int answer;
        cin>>answer;
        if(answer==1){
            cout<<"HARD";
            break;
        }
    }
    if(i==n) cout<<"EASY";
}