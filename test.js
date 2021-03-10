const foo = () => {
    let x = 0;
    x += 500;
    x -= 250;
    return x;
}
const bar = (x, y) => {
    return (x < 10 || (false && x < 2)) && y;
}
let x = foo();
let z = 1;
z = -z;
let kek = bar(x, true);
let jaj = !(true && kek);
