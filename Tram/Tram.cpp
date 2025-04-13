#include <iostream>

int main() {
    int n,passengers=0,maximum=0;
    std::cin>>n;
    for(int i=0;i<n;++i){
        int in=0,out=0;
        std::cin>>out>>in;
        passengers+=in-out;
        maximum=std::max(maximum,passengers);
    }
    std::cout<<maximum;
}
