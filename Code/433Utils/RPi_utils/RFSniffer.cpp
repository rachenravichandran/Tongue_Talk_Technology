#include "../rc-switch/RCSwitch.h"
#include <stdlib.h>
#include <stdio.h>
RCSwitch mySwitch;
int main(int argc, char *argv[]) {
     int PIN = 2;
     
     if(wiringPiSetup() == -1) {
       printf("wiringPiSetup failed, exiting...");
       return 0;
     }
     int pulseLength = 0, i = 100;
     if (argv[1] != NULL) 
	pulseLength = atoi(argv[1]);
     mySwitch = RCSwitch();
     if (pulseLength != 0) 
	mySwitch.setPulseLength(pulseLength);
     mySwitch.enableReceive(PIN);  
     while(1) {
      if (mySwitch.available()) {
	
        int value = mySwitch.getReceivedValue();
        if (value == 0 ) {
          printf("Unknown encoding\n");
        } //else if( value > 1000)
	//{}
	else{    
FILE *f = fopen(argv[1], "wb");
	if(f==NULL)
	{
	printf("NO FILE");
	exit(0);
	}
          printf("Received %i ---%d\n", value, i);
	 fprintf(f, "%d %i",i, value);
	//fwrite(&value,sizeof(int),1,f);	  
	i++;
fclose(f);
	 if(i > 999)
	{
		i = 100;
	}
        }
        mySwitch.resetAvailable();
	
      }
  }
  exit(0);
}

