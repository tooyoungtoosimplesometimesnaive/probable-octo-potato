pub struct list_node<T> {
    pub val: T,
    pub next: Option<Box<list_node<T>>>,
}

struct Linked_list<T> {
    head: list_node<T>
}

pub fn work() {
    println!("it works");
}
