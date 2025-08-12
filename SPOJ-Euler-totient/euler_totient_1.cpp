#include <iostream>
#include<vector>
using namespace std;

vector<int> computeTotient(int n) {
    vector<int> phi(n+1);
    for (int i = 0; i <= n; ++i) phi[i] = i;

    for (int i = 2; i <= n; ++i) {
        if (phi[i] == i) { 
            for (int j = i; j <= n; j += i)
                phi[j] -= phi[j] / i;
        }
    }
    return phi;
}

int main() {
	int MAX=1000000;
	vector<int> sol = computeTotient(MAX);
	int T;
	cin>>T;
	
	while(T--){
		int n;
		cin>>n;
		cout<<sol[n]<<"\n";
	}
	
	return 0;
}
