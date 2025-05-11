#include<iostream>
#include<stack>
#include<vector>
#include<string>
using namespace std;

int main(){
    string bracket;
    cin>>bracket;
    int n=bracket.length();

    int maxlen=0;
    stack<int>s;

    for(int i=0;i<n;i++){
        if(bracket[i]==')'){
            if(!s.empty()){
                s.pop();
                maxlen+=2;
            }
        }
        else s.push(bracket[i]);
    }

    cout<<maxlen<<endl;
}