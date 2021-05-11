/* In Javascript you define 
a function and give it an identity
you can call */
// function b(){} where b is the identity
// Value Return Example
var c = 5;
function f (x) {
    return (x * 2 ** c),
    console.log(x * 2 ** c ) // console.log prints out in the console
}
f(2);
// Statement return value

function even_odd (x){
    if (x % 2 == 0){
        console.log("even")
    }
    else {
        console.log("odd")
    }
}
even_odd(2);
even_odd(3);
// functions with empty parameters

function b() {
    return(3 + 1)
}
var result = b();
console.log(result)

// functions with multiple parameters

function multiple(x,y,z){
    return(x + y + z)
}
var d = b(3,5,4);
console.log(d);

/* instead of using"return" you can use console.log to sinplify things
and avoid too much variable assigning
*/

// for Exmaple
function brid(e,f){
    console.log(e+f,"Myname is rad")
}
brid(3,4);
