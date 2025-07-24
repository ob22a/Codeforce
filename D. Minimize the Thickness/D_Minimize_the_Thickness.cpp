#include<iostream>
#include<numeric>
#include<vector>

using namespace std;

void helper(const vector<int>& arr,const int& size){
    int sol=size;
    int total=accumulate(arr.begin(),arr.end(),0ll);
    
    for(int d=1;1ll*d*d<=total;++d){
        if(total%d==0){
            for(int target:{d,total/d}){
                int sum=0;
                bool isValid=true;
                int maxLen=0;
                for(int i=0,j=-1;i<size;++i){
                    sum+=arr[i];
                    if(sum==target){
                        maxLen=max(maxLen,i-j);
                        j=i;
                        sum=0;
                    }
                    else if(sum>target){
                        isValid=false;
                        break;
                    }
                }
                if (isValid && sum == 0) sol=min(sol, maxLen);
            }
        }
    }

    cout<<sol<<"\n";
}

int main(){
    int test;
    cin>>test;
    while(test--){
        int size;
        cin>>size;
        vector<int> a(size);
        for(int& num:a) cin>>num;
        helper(a,size);
    }
}