#include<iostream>
#include<vector>

using namespace std;

void helper(const vector<int>& f,const int& n,int& row){
    int happy=0;
    int leftOver=0;
    for(const int& num:f){
        int fam=num;
        while(fam>=2 && row>0){
            happy+=2;
            fam-=2;
            row--;
        }
        if(fam>0) leftOver++;
    }

    while (row-- && leftOver){
        happy++;
        leftOver--;
    }

    happy-=leftOver;
    
    cout<<happy<<"\n";
}

int main(){
    int test;
    cin>>test;
    while(test--){
        int n,r;
        cin>>n>>r;
        vector<int> families(n);
        for(int& x:families) cin>>x;
        helper(families,n,r);
    }
}