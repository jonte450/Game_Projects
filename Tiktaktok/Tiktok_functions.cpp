#include <iostream>
#include <string>
#include <fstream>

void print_Blank_Board(string);
void print_the_board(Gameboard board);
void get_names_players(string &p1,string &p2);
void check_board_response(Gameboard&,char);
int user_input();
void update_board(Gameboard);
void print_prompt(string,char);
void get_Winner(Gameboard,string,string);

using namespace std;


void get_Winner(Gameboard board,string name_x,string name_o){
    char decide;
    decide = board.decide_winner();
    if(decide == 'x'){
      cout<<"Congratulations "<<name_x<<" you are the winner!\n\n";
    }
    if(decide == 'o'){
      cout<<"Congratulations "<<name_o<<" you are the winner!\n\n";
    }
}

void print_prompt(string name,char symbol){
    cout<<name<<" where would you like to place your mark: "<<symbol<<"\n";
    cout<<"\n\n";
}

void update_board(Gameboard board){
cout<<"\n\n";
for(int draw = 0; draw < 16; draw++){
    cout<<"|"<<board.getGameSpace()[draw];
    if(draw % 4 ==  3){
        cout<<"|\n";
    }
}
cout <<"\n\n\n";
}

void check_board_response(Gameboard &board,char user_position){
    int get_input;
    int get_response;
do {
    get_input = user_input();
    get_response = board.set_space(get_input,user_position);
    if(get_response == -1){
        cout<<"Sorry this space was taken by your opponent!";
    }
}while(get_response == -1);    
}

int user_input(){
    int wished_position; 
    cout<<"Please enter a number between 0-15!:\n ";
    cout<<"\n\n";
    cin>>wished_position;
    while(wished_position > 15 || wished_position < 0){
        cin.clear();
        cout<< "That value is invalid!.\n";
        cout<<"Please enter a valid number between 0-15:\n";
        cin.clear();
        cin>>wished_position;
    }
}



void get_names_players(string &p1,string &p2){
    cout<<"Enter the name of player x:\n";
    cin>>p1;
    cout<<"Enter the name of player o:\n";
    cin>>p2;
    cout<<"\n\n";
}

void print_Blank_Board(){
    for(int draw = 0; draw < 16; draw++){
        cout<<"|"<<draw<<":";
        if(draw<=9){
        cout<<" ";    
        }
        if(draw%4 == 3){
        //cout<< draw;
        cout<<"|"<<"\n";
        }
    }
    cout<<"\n\n\n";

}

void print_the_board(Gameboard board){
    print_Blank_Board();
    for(int draw = 0; draw < 16;draw++){
        cout<<"|"<< board.getGameSpace()[draw];
        if(draw%4 == 3){
          cout<<"|"<<"\n";
        }
        
    }
    cout<<"\n\n\n";
}
