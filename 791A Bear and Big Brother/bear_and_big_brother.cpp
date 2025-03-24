#include<iostream>
int numberOfYears(int a,int b);
int main(){
    int a,b;
    std::cin>>a>>b;
    std::cout<<numberOfYears(a,b);
    return 0;
}
int numberOfYears(int a,int b){
    int year=0;
    while(a<=b){
        a*=3;
        b*=2;
        ++year;
    }
    return year;
}
