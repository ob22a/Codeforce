#include<iostream>
#include<string>
#include<unordered_set>
bool checkGender(std::string username);
int main(){
    std::string username;
    std::cin>>username;
    if(checkGender(username)) std::cout<<"CHAT WITH HER!";
    else std::cout<<"IGNORE HIM!";
    return 0;
}
bool checkGender(std::string username){
    std::unordered_set<int> seen;
    int count=0;
    for(char a:username){
        if(seen.find(a)==seen.end()){
            ++count;
            seen.insert(a);
        }
    }
    return count%2==0; //Is Female
}
