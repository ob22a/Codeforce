#include<iostream>
#include<vector>

using namespace std;

void helper(const vector<pair<int,int>>& resp,const int size){
    int sol=-1;
    for(int i=0;i<size;++i){
        if(resp[i].first<=10){
            if(sol == -1 || resp[i].second > resp[sol].second){
                sol = i;
            }
        }
    }
    cout<<sol+1<<"\n";
}

int main(){
    int test;
    cin>>test;
    while(test--){
        int size;
        cin>>size;
        vector<pair<int,int>> response;
        for(int j=0;j<size;++j){
            int a,b;
            cin>>a>>b;
            response.push_back({a,b});
        }
        helper(response,size);
    }
}