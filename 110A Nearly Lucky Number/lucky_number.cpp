#include<iostream>
bool nearlyLucky(long long num);
int main(){
    long long n;
    std::cin>>n;
    if(nearlyLucky(n)) std::cout<<"YES";
    else std::cout<<"NO";
    return 0;
}
 
bool nearlyLucky(long long num){
    int count=0;
    while(num>0){
        if(num%10==4 or num%10==7){
            ++count;
        }
        num/=10;
    }
    return ((count==4)||(count==7));//Since the test case is upto 10^18 the only possible lucky numbers are 4 and 7.
}
