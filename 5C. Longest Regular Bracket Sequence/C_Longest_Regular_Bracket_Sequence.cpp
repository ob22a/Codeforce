#include<iostream>
#include<stack>
#include<vector>
using namespace std;

int main(){
    stack<int>s;
    string bracket;
    cin>>bracket;
    int n=bracket.length();
    vector<int> dp(n,0);

    int maxlen=0,count=0;
    for(int i=0;i<n;++i){
        if(bracket[i]==')'){
            if(!s.empty()){
                int j=s.top(); s.pop();
                dp[i]=(i-j+1)+((j>0)?dp[j-1]:0);
                
                if(dp[i]>maxlen){
                    maxlen=dp[i];
                    count=1;
                }
                else if(dp[i]==maxlen) ++count;
            }
        }
        else s.push(i);
    }
    if(maxlen==0) cout<<"0 1"<<endl;
    else cout<<maxlen<<" "<<count<<endl;
}