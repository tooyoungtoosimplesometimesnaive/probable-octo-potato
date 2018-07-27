use std::io;

struct State {
    board: [[i32; 3];3],
    turn: i32,
}

fn init() -> State {
    return State {
        board: [[-1; 3]; 3],
        turn: 0,
    }
}

fn display(s: &State) {
    for i in 0..3 {
        for j in 0..3 {
            if s.board[i][j] == -1 {
                print!(" {} ", i * 3 + j + 1);
            } else if s.board[i][j] == 0 {
                print!(" O ");
            } else {
                print!(" X ");
            }

            if j < 2 {
                print!("|");
            } else {
                println!("");
            }
        }

        if i < 2 {
            println!("---+---+---");
        } else {
            println!("");
        }
    }
}

// move is a keyword in rust, so use this name istead
fn move_pos(s: &mut State, i: usize, j: usize) -> i32 {
    if s.board[j][i] != -1 {
        return 0;
    }

    s.board[j][i] = s.turn % 2;
    s.turn += 1;

    return 1;
}

fn human(s: &mut State) {
    loop {
        println!("{}'s turn: ", if s.turn % 2 == 0 { "O" } else { "X" });
        let mut input = String::new();
        match io::stdin().read_line(&mut input) {
            Ok(_) => {
                println!("the input : {}", input);
                let chr = input.chars().next().unwrap();
                let d = chr.to_digit(10).unwrap();
                if d >= 1 && d <= 9 && move_pos(s, ((d - 1) % 3) as usize, ((d - 1) / 3) as usize) == 1 {
                    break;
                }
            },
            Err(error) => {
                println!("Error: {}", error);
                break;
            }
        }
    }
}

fn check(s: &State, j1: usize, i1: usize, j2: usize, i2: usize, j3: usize, i3: usize) -> i32 {
    if s.board[j1][i1] != -1 && s.board[j1][i1] == s.board[j2][i2] && s.board[j1][i1] == s.board[j3][i3] {
        if s.board[j1][i1] == 0 {
            1
        } else {
            -1
        }
    } else {
        0
    }
}

fn evaluate(s: &State) -> i32 {
    for i in 0..3 {
        let c = check(s, i, 0, i, 1, i, 2);
        if c != 0 {
            return c;
        }
        let c2 = check(s, 0, i, 1, i, 2, i);
        if c2 != 0 {
            return c;
        }
    }
    let d_check_1 = check(s,0, 0, 1, 1, 2, 2);
    if d_check_1 != 0 {
        return d_check_1;
    }

    let d_check_2 = check(s, 0, 2, 1, 1, 2, 0);
    if d_check_2 != 0 {
        return d_check_2;
    }

    0
}
        

fn main() {
    let mut state = init();
    display(&state);
    while state.turn < 9 {
        human(&mut state);
        display(&state);
        let result = evaluate(&state);
        if result == 1 {
            println!("O win!");
            return;
        } else if result == -1 {
            println!("X win!");
            return;
        }
    }
    println!("Draw!");
}

