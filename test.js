const foo = () => {
    let x = 0;
    x += 500;
    x -= 250;
    return x;
}
const bar = (y, x) => {
    return x < 10 && y;
}
let x = foo();
let z = 1;
z = -z;
let kek = bar(true, x);
let jaj = !(true && kek);
