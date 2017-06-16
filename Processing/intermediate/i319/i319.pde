/* 15/06/2017 */

final int WIDTH = 1024;
final int HEIGHT = 768;
final int X_MARGIN = WIDTH/40;
final int Y_MARGIN = HEIGHT/40;
final int STEP = 3;
final int BOX_WIDTH = 5;
final int BOXES_ROW = (WIDTH- 2*X_MARGIN + STEP)/(BOX_WIDTH + STEP);
final int BOX_HEIGHT = BOX_WIDTH;

final int N_POP = 10000;
final int SEED = 10;
final float S2I = 0.01;
final float S2R = 0.01;
final float I2R = 0.015;

final int X_TEXT = X_MARGIN;
final int Y_TEXT = 700;
final int FONT_SIZE = 24;

class Individual{
    char s;
    int x, y;
  
    public Individual(char state, int xpos, int ypos){
        s = state;
        x = xpos;
        y = ypos;
    }
  
    public void colorize(){
        noStroke();
        switch(s){
            case 'S': fill(245, 249, 122); break;
            case 'I': fill(255, 83, 61); break;
            case 'R': fill(65, 232, 53); break;
        }
      rect(x, y, BOX_WIDTH, BOX_HEIGHT);
    }
}

class Population{
    Individual[] pop;
    
    public Population(){
        pop = new Individual[N_POP];
        
        for(int i=0; i < N_POP; i++){
            char init_state = i < SEED ? 'I' : 'S'; 
            pop[i] = new Individual(init_state, X_MARGIN+(i%BOXES_ROW)*(STEP+BOX_WIDTH), Y_MARGIN+(i/BOXES_ROW)*(STEP+BOX_HEIGHT));
            pop[i].colorize();
        }
    }
    
    public boolean isFullyPatched(){
        for(int i=0; i < N_POP; i++){
            if(pop[i].s != 'R'){
                return false;
            }
        }
        return true;
    }
    
    public void update(){
        for(int i=0; i < N_POP; i++){
            if(pop[i].s == 'S' && random(1) < S2R){
                pop[i].s = 'R';
            }
            else if(pop[i].s == 'I' && random(1) < I2R){
                pop[i].s = 'R';
            }
            else if(pop[i].s == 'S' && random(1) < S2I){
                pop[i].s = 'I';
            }
        }
    }
   
    public void render(){
        for(int i=0; i < N_POP; i++){
            pop[i].colorize();
        }
    }
}

void renderCounter(int n){
    fill(255);
    rect(X_TEXT, Y_TEXT-FONT_SIZE, FONT_SIZE*4, FONT_SIZE*2);
    fill(0);
    text(n, X_TEXT, Y_TEXT);
}

Population x;
int counter;
PFont f;

void setup(){
    size(1024, 768);
    background(255);
    
    x = new Population();
    counter = 0;
    f = createFont("Arial", FONT_SIZE, true);
    textFont(f);
}

void draw(){
    if(!x.isFullyPatched()){
        x.update();
        x.render();
        counter++;
        renderCounter(counter);
    }
}