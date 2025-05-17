#include<iostream>
using namespace std;

int main(){
    int num;
    cin>>num; //Take the number of test cases 

    for(int i=0;i<num;++i){
        int noPlayers;
        cin>>noPlayers;//Take the number of players 

        bool stopped=false;
        int zeroCount=0;
        int prev=-1;
        int result=-1;

        for(int j=0;j<noPlayers;++j){
            prev=result;
            cin>>result;
            if(result==0) ++zeroCount;
            if(prev!=-1){
                if(prev==result && result==0){
                    stopped=true;
                }
            }
        }

        if(!stopped && zeroCount>0) cout<<"NO"<<endl; 
        else cout<<"YES"<<endl;
    }
}