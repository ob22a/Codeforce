#include<iostream>
using namespace std;

int main(){
    int n,m;
    cin>>n>>m;

    bool isLeft=false;
    for(int i=0;i<n;++i){
        for(int j=0;j<m;++j){
            if(i%2==0 || (isLeft && j==0) || (!isLeft && j==m-1)) cout<<"#";
            else cout<<".";
        }
        if(i%2!=0) isLeft=!isLeft;
        cout<<"\n";
    }

}