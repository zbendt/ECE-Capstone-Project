float th1,th2,th3 = 90; 
float x,y,z;

char ch;
// robot geometry
 // (look at pics above for explanation)
 const float e = 45;     // end effector
 const float f = 60;     // base
 const float re = 300;
 const float rf = 210;
 
 // trigonometric constants
 const float sqrt3 = sqrt(3.0);
 const float pi = 3.141592653;    // PI
 const float sin120 = sqrt(3)/2.0;   
 const float cos120 = -0.5;        
 const float tan60 = sqrt(3);
 const float sin30 = 0.5;
 const float tan30 = 1/sqrt(3);

void setup() {
  // put your setup code here, to run once:
  x = 0; 
  y = 0; 
  z = -200;
  Serial.begin(115200);
  delta_calcInverse(72, -72, -200, x, y, z);
  Serial.println(x);
  Serial.println(y);
  Serial.println(z);
}

void loop() {
  // put your main code here, to run repeatedly:

}


 // inverse kinematics
 // helper functions, calculates angle theta1 (for YZ-pane)
 int delta_calcAngleYZ(float x0, float y0, float z0, float &theta) {
    Serial.print(x0);
     Serial.print(" ");
     Serial.print(y0);
     Serial.print(" ");
     Serial.println(z0);
     float y1 = -0.5 * 0.57735 * f; // f/2 * tg 30
     y0 -= 0.5 * 0.57735    * e;    // shift center to edge
     // z = a + b*y
     float a = (x0*x0 + y0*y0 + z0*z0 +rf*rf - re*re - y1*y1)/(2*z0);
     float b = (y1-y0)/z0;
     // discriminant
     float d = -(a+b*y1)*(a+b*y1)+rf*(b*b*rf+rf); 
     Serial.print(a);
     Serial.print(" ");
     Serial.print(b);
     Serial.print(" ");
     Serial.println(d);
     if (d < 0) return -1; // non-existing point
     float yj = (y1 - a*b - sqrt(d))/(b*b + 1); // choosing outer point
     float zj = a + b*yj;
     theta = 180.0*atan(-zj/(y1 - yj))/pi + ((yj>y1)?180.0:0.0);
     return 0;
 }
 
 // inverse kinematics: (x0, y0, z0) -> (theta1, theta2, theta3)
 // returned status: 0=OK, -1=non-existing position
 int delta_calcInverse(float x0, float y0, float z0, float &theta1, float &theta2, float &theta3) {
     theta1 = theta2 = theta3 = 0;
     int status = delta_calcAngleYZ(x0, y0, z0, theta1);
     if (status == 0) status = delta_calcAngleYZ(x0*cos120 + y0*sin120, y0*cos120-x0*sin120, z0, theta2);  // rotate coords to +120 deg
     if (status == 0) status = delta_calcAngleYZ(x0*cos120 - y0*sin120, y0*cos120+x0*sin120, z0, theta3);  // rotate coords to -120 deg
     return status;
 }
