#include<iostream>
int main(){
    int n,h;
    std::cin>>n>>h;
    int width=0;
    for(int i=0;i<n;++i){
        int val;
        std::cin>>val;
        if(val>h) width+=2;
        else ++width;
    }
    std::cout<<width;
}