#include<iostream>
int main(){
    int a,b;
    for(int i=0;i<5;++i){
        for(int j=0;j<5;++j){
            int val;
            std::cin>>val;
            if(val==1){
                a=i;
                b=j;
            }
        }
    }
    //The mid point is at 2,2
    a=a<2 ? 2-a : a-2;
    b=b<2 ? 2-b : b-2;
    std::cout<<a+b;
    return 0;
}
