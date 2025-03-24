#include<iostream>
#include<string>
void capitalize(std::string& s);
int main(){
    std::string s;
    std::cin>>s;
    capitalize(s);
    std::cout<<s;
    return 0;
}
void capitalize(std::string& s){
    //Capitalizing means subtracting 32 according to ASCII table 
    auto p=s.begin();
    if(*p>='a'&& *p<='z') *p-=32;
}
