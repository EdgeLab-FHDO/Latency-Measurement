#include <stdio.h>
#include <iostream>
#include "wiringPi.h"
#include <ctime>
#include <sys/time.h>
#include <fstream>

using namespace std;

int main() {
    wiringPiSetupGpio();
    const int INPUT_PIN = 24;
    pinMode(INPUT_PIN, INPUT);
    pullUpDnControl(INPUT_PIN, PUD_UP); 
    
    while (true){
        if(digitalRead(INPUT_PIN)==LOW){
            struct timeval now;
            gettimeofday(&now, NULL);
            //cout<<"time_sec "<<now.tv_sec <<endl;
            //cout<<"Local date and time is "<<now.tv_usec <<endl;
            
            //struct timespec ts;
            //timespec_get(&ts, TIME_UTC);
            //char buff[100];
            //strftime(buff, sizeof buff, "%D %T", gmtime(&ts.tv_sec));
            //printf("Current time: %s.%09ld UTC\n", buff, ts.tv_nsec);
            //delay(2000);
            
            ofstream file;
            file.open("data_file.txt",ios::app);
            file<<now.tv_usec <<endl;
            delay(2000);
            file.close();
        }
        
    }
 return 0; 
}
