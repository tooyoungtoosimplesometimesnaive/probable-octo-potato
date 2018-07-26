fn main() {
    println!("Hello, world!");
    let board: [[i32;3];3] = [[-1; 3]; 3];
    for r in board.iter() {
        for c in r.iter() {
            println!("{}", *c);
        }
    }
}
