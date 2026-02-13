#include<iostream>
#include<vector>
using namespace std;

int extended_gcd(int a, int b, long long &x, long long &y) {
    int x0=1,y0=0,x1=0,y1=1;

    while (b){
        int q=a/b;
        int r=a%b;

        a=b;
        b=r;

        int temp1=x1,temp2=y1;
        x1=x0-q*x1;
        y1=y0-q*y1;
        x0=temp1;
        y0=temp2;
    }

    x=x0;
    y=y0;
    
    return a;
}

int main(){
    int a,b,c;
    cin>>a>>b>>c;
    
    long long x,y;
    int factor=extended_gcd(a,b,x,y);
    
    if(c%factor!=0){
        cout<<0<<"\n";
        return 0;
    }

    int n=c/factor;
    x*=n;
    y*=n;

    vector<pair<int,int>> soln;

    auto helper= [&](auto&& self,long long large,long long small,bool isA){
        /*
            ans1 = large - a*t
            ans2 = small + b*t

            We can start t from large/a - (large%a==0) To ensure positive results and t will decrease by 1 at each step
            The loop will break when one of the answers is negative
        */
        for(int t=(large/b)-(large%b==0);;t--){
            long long ans1=large-(((isA)?b:a/factor)*t);
            long long ans2=small+(((isA)?a:b/factor)*t);

            if(ans1<=0 || ans2<=0){
                break;
            }
            soln.push_back({ans1,ans2});
        }
    };

    if(x>y) helper(helper,x,y,true);
    else helper(helper,y,x,false);

    cout<<soln.size()<<"\n";
    for(const pair<int,int>& p:soln){
        cout<<p.first<<" "<<p.second<<"\n";
    }

    return 0;

}