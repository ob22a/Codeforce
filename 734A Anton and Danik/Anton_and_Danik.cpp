#include<iostream>
std::string winner(int num,std::string s);
int main(){
    int n;
    std::cin>>n;
    std::string s;
    std::cin>>s;
    std::cout<<winner(n,s);
    return 0;
}
std::string winner(int num,std::string s){
    int a=0,b=0;
    for(int i=0;i<num;++i){
        if(s[i]=='A') ++a;
        else ++b;
    }
    if(a>b) return "Anton";
    else if(a<b) return "Danik";
    else return "Friendship";
}
