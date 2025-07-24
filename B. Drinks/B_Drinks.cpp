#include<iostream>

using namespace std;

int main(){
    int n;
    cin>>n;
    int num=n;
    double orange;
    while(n--){
        double val;
        cin>>val;
        orange+=(val/100);
    }
    cout<<(orange*100/num);
}