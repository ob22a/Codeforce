#include<iostream>
#include<vector>

using namespace std;

int main(){
    int t;
    cin>>t;
    while(t--){
        int n;
        cin>>n;
        int sol=0;
        for(int i=0;i<n;++i){
            int val;
            cin>>val;
            sol+=(val==0)?1:val;
        }
        cout<<sol<<"\n";
    }
}