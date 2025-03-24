#include<iostream>
int minRemove(std::string& s);
int main(){
    int n;
    std::cin>>n;
    std::string s;
    std::cin>>s;
    std::cout<<minRemove(s);
    return 0;
}
int minRemove(std::string& s){
    int count=0;
    for(auto i=s.begin();i<s.end()-1;++i){
        if(*i==*(i+1)) ++count;
    }
    return count;
}
