#include <wiringPi.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
int len=120;		//Number of steps
int ptime=20;		//Period, ms
int st_file_x, st_file_y;

#include </home/pi/mixed_proj/sm/sm_header/sm6.h>
#include </home/pi/mixed_proj/sm/move/move.h>

struct point {		//Contour points
	int x;			//X-coordinate
	int y;			//Y-coordinate
	int t;			//Time
};

struct t_position {		//Table position
	int x;			//X-coordinate
	int y;			//Y-coordinate
	int x_phase;			//X phase
	int y_phase;			//Y phase
};

struct point pic[10];		//Array of points

int st_file_op(char *operation) {
	FILE *st_file;
	if (operation == "read"){
		st_file = fopen("st_x_file","r");								//Reading starting phase from file
		fscanf(st_file, "%d", &(st_file_x));
		fclose(st_file);
		st_file = fopen("st_y_file","r");								//Reading starting phase from file
		fscanf(st_file, "%d", &(st_file_y));
		fclose(st_file);
	}
	if (operation == "write"){
		st_file = fopen("st_x_file","w");								//Reading starting phase from file
		fprintf(st_file, "%d", st_file_x);
		fclose(st_file);
		st_file = fopen("st_y_file","w");								//Reading starting phase from file
		fprintf(st_file, "%d", st_file_y);
		fclose(st_file);
	}
	if ((operation != "read")&&(operation != "write")){
		printf("Smthg wrong with st_file func");
		return 1;
	}
}


int toggle_dir(void) {				//Direction acc. to toggle switcher
	if ((digitalRead(PIN_all[26])==1)&&(digitalRead(PIN_all[27])==0)) {
		printf("26 PIN 1");
		dir("r");
	}
	if ((digitalRead(PIN_all[27])==1)&&(digitalRead(PIN_all[26])==0)) {
		dir("l");
	}
}

int main()
{
	if (piHiPri(90) == -1) {printf("Priority setting FAILED");}
	if (wiringPiSetup() == -1) {printf("WiringPi setup FAILED");}

	int i, j, rc, a;
	
	a = 0;
	FILE *num_file;
	FILE *pic_file;
	
	for (i=0; i<12; i++) {
		pinMode (PIN[i], OUTPUT);
		digitalWrite (i, LOW);
	}
		
	// Set RPI pin 26-28 to be an input
	pinMode (PIN_all[28], INPUT);
	pinMode (PIN_all[27], INPUT);
	pinMode (PIN_all[26], INPUT);
	pinMode (PIN_all[25], INPUT);
	//  with a pullup
	pullUpDnControl (PIN_all[28], PUD_DOWN) ;
	pullUpDnControl (PIN_all[27], PUD_DOWN) ;
	pullUpDnControl (PIN_all[26], PUD_DOWN) ;
	pullUpDnControl (PIN_all[25], PUD_DOWN) ;
		
	num_file = fopen("num_file","r");
	if (num_file==NULL){
		perror ("failed to open num_file");
		return EXIT_FAILURE;
	}	
	fscanf(num_file, "%d %d", &(len), &(ptime));
	fclose(num_file);
	
	st_file_op("read");
	
	pic_file = fopen("pic_file","r");
	if (pic_file==NULL){
		perror ("failed to open pic_file");
		return EXIT_FAILURE;
	}	
	i=1;
	pic[0].x=0; pic[0].y=0; pic[0].t=0;
	while (fscanf(num_file, "%d %d %d", &(pic[i].x), &(pic[i].y), &(pic[i].t)) != EOF) {
		i++;
	}
	fclose(num_file);
	
	//PIN_set("y");
	/*for (i=0; i<6; i++){
		printf("%d..;",PIN[i]);
	}
	printf("\n");
	printf("%d",st_file_y);
	*/
	if (digitalRead(PIN_all[25])==1) {
		while (digitalRead(PIN_all[28])==1) {
			for (i=0; i<6; i++){
				printf("%d..;",PIN[i]);
			}
			printf("\n");
			/*pwr(1,1);
			delay(200);
			pwr(1,0);
			delay(200);
			
			fflush(stdout);
			//move("y",1);*/
			if (digitalRead(PIN_all[28])==0) {break;}
		}
	}
	if (digitalRead(PIN_all[25])==0) {
		dir("r");
		i=1;
		while (pic[i].t != 0) {
			printf("%d\n",(pic[i].x-pic[i-1].x));
			move("x",(pic[i].x-pic[i-1].x));
			if (digitalRead(PIN_all[28])==0) {break;}
			//printf("Hey");
			delay(pic[i].t);
			i++;
		}	
	}	
	
	for (j=0; j<30; j++) {
			digitalWrite(PIN[j], LOW);
		}
	
	st_file_op("write");
		
	return EXIT_SUCCESS;
}
		
		
