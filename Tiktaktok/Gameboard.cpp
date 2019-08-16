/*header file for main.cpp*/
#include <iostream>
#include <iomanip>
using namespace std;

class Gameboard
{
    char gameSpace[16];
    char the_winner;
public:
    Gameboard(){
        the_winner = 'z';
        for(int draw = 0; draw < 16;draw++){
            gameSpace[draw] = '_';
        }
    }
    char* getGameSpace(void){
          return gameSpace;
    }

    int set_space(int index_space,char symbol){
    {
        if(gameSpace[index_space] == '_'){
            gameSpace[index_space] = symbol;
            return 1;
        }
        else{
            return -1;
        }
    }
        return 1;
    }

    char check_rows(){
        int x_count = 0;
        int o_count = 0;

        for(int row = 0; row <16; row+=4){
            for(int col = 0; col<4;col++){
                if(gameSpace[row+col] == 'o'){
                    o_count++;
                }
                if(gameSpace[row+col] == 'x'){
                    x_count++;
                }

            }
    if(o_count == 4 ){
        return 'o';
    }

    if(x_count == 4){
        return 'x';
    }

    x_count = 0;
    o_count = 0;

            }

    return 'z';
    }


    char check_cols(){
        int x_count = 0;
        int o_count = 0;

        for(int col = 0; col<4; col++){
            for(int row = 0; row<16;row+=4){
                if(gameSpace[row+col] == 'o'){
                    o_count++;
                }
                if(gameSpace[row+col] == 'x'){
                    x_count++;
                }

            }
    if(o_count == 4 ){
        return 'o';
    }

    if(x_count == 4){
        return 'x';
    }

    x_count = 0;
    o_count = 0;

    }

    return 'z';
    }

char check_diagonals(){
    int x_count = 0;
    int o_count = 0;
    //Check left diagonal
    for(int dia = 0; dia < 16; dia += 5){
            if(gameSpace[dia] == 'x'){
                x_count++;
            }
            if(gameSpace[dia] == 'o'){
                o_count++;
            }
    }
    if(o_count == 4 ){
        return 'o';
    }

    if(x_count == 4){
        return 'x';
    }
    x_count = 0;
    o_count = 0;

    //Checking right diagonal
    for(int dia = 3;dia < 16; dia += 3){
      if(gameSpace[dia] == 'x'){
            x_count++;
            }
        if(gameSpace[dia] == 'o'){
                o_count++;
            }
        }

    if(o_count == 4 ){
        return 'o';
    }

    if(x_count == 4){
        return 'x';
    }
    x_count = 0;
    o_count = 0;
    return 'z';

}
char decide_winner(){
char check = 'z';
check = check_rows();
//cout<<The winner rows;
if(check == 'z'){
   check =  check_cols();
//cout<<"The winner cols "<<check<<"\n";

}
if(check == 'z'){
   check = check_diagonals();
//cout<<"The winner diagonals\

}
return check;
}
};
