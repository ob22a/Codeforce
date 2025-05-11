#include<iostream>
#include<unordered_set>
using namespace std;
bool distinctDigits(int num){
    unordered_set<int> distinct;
    while(num>0){
        if(distinct.count(num%10)) return false;
        distinct.insert(num%10);
        num/=10;
    }
    return true;
}
int main(){
    int year;
    cin>>year;
    while(!distinctDigits(++year)){
    }
    cout<<year;
}