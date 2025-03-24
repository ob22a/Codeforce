#include<iostream>
#include<string>
bool correctTranslation(std::string s,std::string t);
int main(){
    std::string s,t;
    std::cin>>s>>t;
    if(correctTranslation(s,t)) std::cout<<"YES";
    else std::cout<<"NO";
    return 0;
}
bool correctTranslation(std::string s,std::string t){
    std::string temp="";
    for(auto it=s.end()-1;it>=s.begin();--it){
        temp+=*it;
    }
    return temp==t;
}
