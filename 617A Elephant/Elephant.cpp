#include<iostream>
int elephantSteps(int num);
int main(){
    int n;
    std::cin>>n;
    std::cout<<elephantSteps(n);
    return 0;
}
int elephantSteps(int num){
    int rem=(num%5==0)?0:1;
    return rem+num/5;
}
