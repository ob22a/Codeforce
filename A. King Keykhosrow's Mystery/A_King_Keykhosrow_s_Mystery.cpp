#include<iostream>
using namespace std;

int gcf(int& a,int& b){
    int temp=max(a,b);
    if(temp!=a){
        b=a;
        a=temp;
    }
    while(b){
        int temp=a;
        a=b;
        b=temp%a;
    }
    return a;
}

int main(){
    int test;
    cin>>test;
    while(test--){
        int num1,num2;
        cin>>num1>>num2;
        cout<<(1ll*num1*num2)/gcf(num1,num2)<<"\n";
    }
}