#include<iostream>
#include<vector>
#include<numeric>
#include<algorithm>
using namespace std;

bool isUnhappy(const vector<int>& arr,const int size,const long long& total,const long long& val){
    int unhappy=0;
    long long newSum=(total+val);
    double avg=(double)newSum/size;
    avg/=2.0;
    for(int num:arr){
        if(num<avg) ++unhappy;
    }
    return unhappy>(size/2);
}

void helper(const vector<int>& arr,const int size){
    if(size<=2){
        cout<<-1<<"\n";
        return;
    }

    long long totalSum=accumulate(arr.begin(),arr.end(),0ll);

    long long l=0,r=1e12;
    long long ans=-1;
    while(l<=r){
        long long m=l+(r-l)/2;
        if(isUnhappy(arr,size,totalSum,m)){
            ans=m;
            r=m-1;
        }
        else l=m+1;
    }

    cout<<ans<<"\n";

}

int main(){
    int t;
    cin>>t;
    while(t--){
        int size;
        cin>>size;
        vector<int> popl(size);
        for(int& x:popl) cin>>x;
        helper(popl,size);
    }
}