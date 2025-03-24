#include<iostream>
bool moreCapital(std::string s);
void modify(std::string& s);
int main(){
    std::string s;
    std::cin>>s;
    modify(s);
    std::cout<<s;
    return 0;
}
bool moreCapital(std::string str){
    int c=0,s=0;
    for(char l:str){
        if('a'<=l && 'z'>=l) ++s;
        if('A'<=l && 'Z'>=l) ++c;
    }
    return c>s;
}
void modify(std::string& s){
    if(moreCapital(s)){
        for(auto it=s.begin();it<s.end();++it){
            if('a'<=*it && 'z'>=*it) (*it)-=32;
        }
    }
    else{
         for(auto it=s.begin();it<s.end();++it){
            if('A'<=*it && 'Z'>=*it) (*it)+=32;
        }
    }
}
