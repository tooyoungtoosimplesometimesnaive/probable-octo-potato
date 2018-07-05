pub struct List_node<T> {
    pub val: T,
    pub next: Option<Box<List_node<T>>>,
}

struct Linked_list<T> {
    head: List_node<T>
}

pub fn work() {
    println!("it works");
}
