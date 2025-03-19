#include<iostream>
#include<string>
using namespace std;
int main(){
    int n;
    cin>>n;
    int x=0;
    for(int i=0;i<n;++i){
        string operation;
        cin>>operation;
        if(operation.substr(0,2)=="++" || operation.substr(1,3)=="++"){
            ++x;
        }
        else if(operation.substr(0,2)=="--" || operation.substr(1,3)=="--"){
            --x;
        }
    }
    cout<<x;
}
