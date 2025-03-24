#include<iostream>
#include<string>
#include<vector>
void bubbleSort(std::vector<int>& l);
void swap(int& a,int& b);
int main(){
    std::string s;
    std::cin>>s;
    std::vector<int> num;
    for(char a:s){
        if(a!='+'){
            num.push_back((int)(a-'0'));
        }
    }
    bubbleSort(num);
    for(auto it=num.begin();it<num.end()-1;++it){
        std::cout<<*(it)<<"+";
    }
    std::cout<<*(num.end()-1);
    
    return 0;
}
void bubbleSort(std::vector<int>& l){
    int n=l.size();
    for(int i=0;i<n;++i){
        bool isSwapped=false;
        for(int j=0;j<n-1-i;++j){
            if(l[j]>l[j+1]){
                swap(l[j],l[j+1]);
                isSwapped=true;
            }
        }
        if(!isSwapped) break;
    }
}
void swap(int& a,int& b){
    int temp=a;
    a=b;
    b=temp;
}
