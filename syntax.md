# OwOScript Syntax 

## Terminology
A/B -> either A or B can be used to declare a type.

## Primitives
waifu/husbando -> number (-?0...9*)  
catgirl/catboy -> bool   (uwu:True, owo:False)  
senpai/kouhai -> string ("anything in here wrapped by a double quotation")  

## Arrays
waifu/husbando harem -> number array.  
catgirl/catboy harem -> bool array.  
senpai/kouhai harem -> string array.  

## Declare Variables
waifu/husbando var_name; -> declare a num variables  
catgirl/catboy var_name; -> declare a bool variable  
senpai/kouhai var_name; -> declare a string variable  

waifu/husbando harem arr_name; -> declare a num array  
catgirl/catboy harem arr_name; -> declare a bool array  

real waifu/husband const_var_name; -> declare a constant variable of type num

## Initialize Variables
waifu x = 5;  
catgirl y = uwu;  
real senpai z = "Hello";   
waifu harem x_array = [5,1,2,3,7,40,-100,90,0];  

## Operations
waifu addition = 5+5;  
addition += 5;  
addition++;  

catgirl bool_op = addition >= 10;  
catgirl bool_op2 = bool_op || owo;  
catboy bool_num_op = bool_op != uwu;  

senpai word1 = "Hello ";  
senpai word2 = "Word";  
kouhai word = word1 + word2; (concatenation)  

husbando harem y_array = [1000];  
x_array = x_array + y_array; (list concatenation)  

## If statements 
```
nani (uwu && uwu){               -> if  
    baka(uwu);   
} noU nani (owo || uwu) {        -> else if  
    baka(owo);  
} noU {                          -> else  
    baka(111);  
}  
```

## For/while loops   
```
waifu hours = 0;
husbando the_blade = 0;

whileU (hours < 10000) iStudied{
    the_blade += hours;
    hours++;  
}  

waifu x = 10;  
shi (waifu y = 0; y < x; y++) {  
    x--;  
}  

waifu harem y = [1,2,3,4,5,6,10];  
shi (real waifu i : y){               -> list iteration  
    baka(i+100);  
}  
```

## Functions 
```
catboy varname = 0;
yokai-chan foo() {                   -> (return type)~sama/chan/san func_name(type args){ statements }  
    varname++;
}

catgirl~sama bar(waifu arg1, catgirl arg2){
    catgirl~san baz(waifu x){  
        baka(x);  
        x>10 desu;  
    }  
    (x < 10 || (baz(x/2) && x<2)) && y desu;  
}  

waifu x = bar(0,0);  
```
