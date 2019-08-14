double old_R[3][3]={{1,0,0},{0,1,0},{0,0,1}};
double current_R[3][3]={{0}};
double x_angular_rate[2];
double x_angle[2],y_angle[2],z_angle[2];
double x_acc[2],y_acc[2],z_acc[2];
double x_velocity[2],y_velocity[2],z_velocity[2];
double x_position[2],y_position[2],z_position[2];
double gyro_x,gyro_y,gyro_z;
int countx_gyro,county_gyro,countz_gyro;
int countx_accel,county_accel,countz_accel;
double start_time;
float angle ,x_pos,y_pos,z_pos;

void setup(){
  Initialize_Globals();
  Calibrate();
  Serial.begin(9600);
}

void loop() {
start_time=millis();

}

void Gyroscope(double x_gyro,y_gyro,z_gyro){
  double w_d=0.2;//window discrimination for no movement condition
  x_angular_rate[1]=make_radians_per_sec(x_gyro)-make_radians_per_sec(gyro_x);
  if((x_angular_rate[1]<=w_d)&&(x_angular_rate[1]>=w_d)){x_angular_rate[1]=0;}

  //integration
  x_angle[1]=x_angle[0]+(x_angular_rate[0]+((x_angular_rate[1]))
}
