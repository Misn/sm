int pwr_st(int state_number)			//Setting current state
{
	int i;
	for (i=0; i<sm_ph_num; i++) {		//On/Off for all phases
		pwr(PIN[i],states_full[state_number][i]);
	}
	printf("\n");
	//delay(ptime);				//Period
}

int pwr(int n, int p)			//PIN state switcher
{
	pinMode (PIN[n], OUTPUT);
	if (p==1){
		digitalWrite (PIN[n], HIGH);
		printf("%d",1);}
	if (p==0){
		digitalWrite (PIN[n], LOW);
		printf("%d",0);}
}

int dir(char *direction_local) {			//Direction setting
	int i;
	if (direction_local=="r") {			//Right*
		for (i=0; i<sm_st_num; i++) {
			states[i]=states_r[i];
			states_dic[i]=states_dic_r[i];
		}
	}
	if (direction_local=="l") {			//Left*
		for (i=0; i<sm_st_num; i++) {
			states[i]=states_l[i];
			states_dic[i]=states_dic_l[i];
		}
	}
}

int find_starting_st(char *direction_local, int st){
	if (direction_local=="r") {			//Right*
		return (st+1);
	}
	if (direction_local=="l") {			//Left*
		return (sm_st_num-st);
	}
}

int PIN_set(char *axis) {			//Axis setting
	int i;
	if (axis=="x") {				//X-axis*
		for (i=0; i<sm_ph_num; i++) {
			PIN[i]=PIN_x[i];
		}
	}
	if (axis=="y") {			//Y-axis*
		for (i=0; i<sm_ph_num; i++) {
			PIN[i]=PIN_y[i];
		}
	}
}

int move(char *a, int diff)											//Move *st_num* steps
{
	int i = 0;
	int num, st_x, st_y, st, mov, st_s, st_c, ph_mov , tmp, position;
	
	//st_x - x-axis state; st_y - y-axis state; st - state
	//mov - number of steps; st_s - starting state; st_c - current state
	//#################### State from file; PIN set ####################
	if (a=="x"){
		printf("x-axis\n");
		st=st_file_x;
		PIN_set("x");
	}
	if (a=="y-axis\n"){
		printf("2"); 
		st=st_file_y;
		PIN_set("y");
	}
	if ((a!="x")&&(a!="y")){
		printf("%s - smthg wrong!\n",a);
		perror ("failed to open st_file");
		return EXIT_FAILURE;
	}
			
	//#################### Direction; number of steps ####################
	if (diff<0){
		dir("l");
		st_s=find_starting_st("l",st);
		mov=abs(diff);
	} else {
	if (diff>0) {
		dir("r");							
		st_s=find_starting_st("r",st);
		printf("£££%d£££", st_file_x);
		mov=abs(diff);
	}
	}
	st_c=st_s;
	
	
	//#################### Powering ####################
	for (i=st_s; i<(st_s+mov); i++) {					//Main *move* cycle
		if (digitalRead(PIN_all[28])==0) {break;}						//Checking OFF-button
		pwr_st(states[i%sm_st_num]);									//Making state
		st_c=states[i%sm_st_num];
	}
	//printf("*move* ended\n");
	if (a=="x"){
		st_file_x=st_c;
	}
	if (a=="y"){
		st_file_y=st_c;
	}
}
