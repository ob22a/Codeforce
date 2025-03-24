#include<iostream>

int main(){
    int k,n,w;//cost,initial,amount
    std::cin>>k>>n>>w;
    int price=k*((w*(w+1))/2);//Formula for sum of first n numbers 
    int borrow=(price>n)?price-n:0;
    std::cout<<borrow;
    return 0;
}
