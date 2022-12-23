/* 14/06/2017 */
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

char* findMonth(const char* month){
    const char lookup[12][4] = {"Jan", "Feb", "Mar", "Apr", "May", "Jun", 
                                "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"};

    char* result = malloc(sizeof(char) * 4);
    for(int i = 0; i < 12; i++){
        if(strcmp(lookup[i], month) == 0){
            snprintf(result, 3, "%02d", i+1);
            return result;
        }
    }
    return NULL;
}

char* getCompleteYear(const char* year){
    char* result = malloc(sizeof(char) * 4);
    if(year[0] > 52){
        strcpy(result, "19");
    } else {
        strcpy(result, "20");
    }
    strcat(result, year);
    return result;
}

char* parseDate(char* date){
    char* final = malloc(sizeof(char) * 11);
    char day[3], month[4], year[5];
    char tell = date[2];

    switch(tell){
        case '/': {
            sscanf(date, "%2s/%2s/%2s", &month, &day, &year);
            strcpy(year, getCompleteYear(year));
            break;
        }
        case '#': {
            sscanf(date, "%2s#%2s#%2s", &month, &year, &day);
            strcpy(year, getCompleteYear(year));
            break;
        }
        case '*': {
            sscanf(date, "%2s*%2s*%4s", &day, &month, &year);
            break;
        }
        default : {
            if(tell > 'a' && tell < 'z'){
                if(strlen(date) == 11){ //pesky '\n'
                    sscanf(date, "%3s %2s, %2s", &month, &day, &year);
                    strcpy(month, findMonth(month));
                    strcpy(year, getCompleteYear(year));
                } else{
                    sscanf(date, "%3s %2s, %4s", &month, &day, &year);
                    strcpy(month, findMonth(month));
                }
            } else{
                sscanf(date, "%4s-%2s-%2s", &year, &month, &day);
            }
        }
    }

    sprintf(final, "%4s-%2s-%2s", year, month, day);
    return final;
}

int main(void){
    FILE *f;
    f = fopen("messedDates.txt", "r");

    char buff[256];
    while(fgets(buff, 256, f)){
        puts(parseDate(buff));
    }
}