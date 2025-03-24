#include<iostream>
#include<string>
void toUpper(std::string& s);
/*Transforming the Uppercase to Lower using math instead of using std::transform
    A=65 AND a=97 so the difference is 32
    */
int main(){
    std::string g1,g2;
    std::getline(std::cin,g1);
    std::getline(std::cin,g2);
    toUpper(g1);
    toUpper(g2);
    if(g1==g2) std::cout<<0;
    else if(g1<g2) std::cout<<-1;
    else std::cout<<1;
    return 0;
}
void toUpper(std::string& s){
    for(auto it=s.begin();it<s.end();++it){
        if('A'<=*it && *it<='Z') (*it)+=32;
    }
}
