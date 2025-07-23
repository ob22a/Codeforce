#include<iostream>
#include<algorithm>
#include<vector>

using namespace std;

int helper(const vector<int>& arr){
    int zeros=0;
    for(int num:arr){
        if(num==0) ++zeros;
    }
    int sol=0;
    for(int i=0;i<zeros;++i){
        if(arr[i]==1) ++sol;
    }
    return sol;
}

int main(){
    int noTest;
    cin>>noTest;
    for(int i=0;i<noTest;++i){
        int size;
        cin>>size;
        vector<int>a(size);
        for(int j=0;j<size;++j) cin>>a[j];
        cout<<helper(a)<<"\n";
    }
    return 0;
}