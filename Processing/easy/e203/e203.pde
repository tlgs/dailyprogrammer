/* 16/06/2017 */

final int SIDE = 50;

void setup(){
    size(200, 200);
    background(255);
}

void draw(){
    translate(width/2, height/2);
    rotate(radians(frameCount*2 % 360));
    
    background(255);
    noStroke();
    fill((frameCount%512 < 256) ? frameCount%256 : 255 - frameCount%256);
    rect(-SIDE/2, -SIDE/2, SIDE, SIDE);
}