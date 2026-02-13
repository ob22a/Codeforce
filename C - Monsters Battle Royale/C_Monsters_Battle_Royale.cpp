#include<iostream>
#include<vector>

using namespace std;

int gcf(int a,int b){
    while(b){
        int temp=a;
        a=b;
        b=temp%b;
    }
    return a;
}

int main(){
    int size;
    cin>>size;
    int sol;
    cin>>sol;
    --size;
    while(size--){
        int val;
        cin>>val;
        sol=gcf(sol,val);
    }
    cout<<sol<<"\n";
}