#include<iostream>
#include<algorithm>
#include<string>
using namespace std;

int main(){
    int n;
    cin>>n;

    string s;
    cin>>s;

    // Brute force soln for now
    for(int div=1;div<=n;++div){
        if(n%div==0) reverse(s.begin(),s.begin()+div);
    }

    cout<<s<<"\n";
}