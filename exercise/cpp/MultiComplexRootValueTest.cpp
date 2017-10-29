#include<iostream>
#include<complex>
#include<cmath>

typedef std::complex<double> cplxf;
#define PI 3.1415926
#define I cplxf(0.0,1.0)

int main(){
    double theta=30;
    cplxf a=exp(-theta/180.0*PI*I);
    std::cout<<a<<std::endl;
    std::cout<<"sqrt(a)="<<sqrt(a)<<std::endl;
    return 0;
}

