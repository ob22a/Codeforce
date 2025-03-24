#include<iostream>
int wrongSubtraction(int num,int amount);
int main(){
    int n,k;
    std::cin>>n>>k;
    std::cout<<wrongSubtraction(n,k);
    return 0;
}
int wrongSubtraction(int num,int amount){
    for(int i=0;i<amount;++i){
        if(num%10==0) num/=10;
        else --num;
    }
    return num;
}
