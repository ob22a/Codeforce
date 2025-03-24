#include<iostream>
int main(){
    int n,k;
    int cutoff=-1;
    int sol=0;
    std::cin>>n>>k;
    for(int i=1;i<=n;++i){
        int a;
        std::cin>>a;
        if((a!=0 && cutoff==-1)||(a==cutoff)){
            sol=i;
        }
        if(i==k && a!=0){
            cutoff=a;
        }
    }
    std::cout<<sol;
    return 0;
}
