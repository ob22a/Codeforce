#include<iostream>
using namespace std;
 
int main(){
    int n;
    cin>>n;
    for(int i=0 ;i<n;++i){
        string s;
        string modified="";
        cin>>s;
        if(s.length()>10){
            modified=s[0]+to_string(s.length()-2)+s.back();
            cout<<modified<<endl;
        }
        else cout<<s<<endl;
    }
}
