 // This Javascript file is for you to practice your scripts and see examples of how code works
console.log('This code doesnot affect  the program');
var l = 2;
var w = 3;
var d = ((l^2 +w^2)^0.5);
console.log(d);


for (var i = 2 ;i<2;) {   
     console.log('Hello World')
}
for (var i = 2 ;i<2;) {   
    console.log(d)
}


 


var country = "Nigeria";
if (country=="Nigeria"){
    console.log("Hello",country)
}
else {
    console.log('Hello Foreign Land')
}

var x = 10;
var y = 11;
//nested if=else statements
 if (x==10){
     if (y==11){
         console.log(x+y)
     }
     else {
         console.log(x)
     }
 }
 else{
     console.log('Cannot run')
 }
// optional parameters
 function f(x=10){
     if (x==10){
         console.log('x is ten')
     }
     else if (x < 5){
       console.log('x is less than 5')
     }
     else{
         console.log('x is not ten')
     }
 }
 f(10);
 f(3);
 f(11);
 // since there was no return statement the function can be called without being defined

 // using both requred and optional parameters
 function required_optional (x,y=13){
     return(x+y)
 }
 f = required_optional(3,); // required x + optional y
 g = required_optional(3,18);
 console.log(f);
 console.log(g);
 console.log(f+g);

 