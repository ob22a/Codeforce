#include<iostream>
int main(){
    int m[5][5];
    int a,b;
    for(int i=0;i<5;++i){
        for(int j=0;j<5;++j){
            int val;
            std::cin>>val;
            m[i][j]=val;
            if(val==1){
                a=i;
                b=j;
            }
        }
    }
    //The mid point is 2,2 on the matrix
    a=a<2? 2-a : a-2;
    b=b<2? 2-b : b-2;
    std::cout<<a+b;
}
