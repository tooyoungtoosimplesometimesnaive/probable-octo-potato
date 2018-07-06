pub struct ListNode<T> {
    pub val: T,
    pub next: Option<Box<ListNode<T>>>,
}

pub struct LinkedList<T> {
    pub head: Option<ListNode<T>>,
    pub size: u8
}

impl<T> LinkedList<T> {
    pub fn add(&mut self, node: ListNode<T>) {
        self.size += 1;
        match self.head {
            Some(n) => {
            loop {
                match n.next {
                    Some(n_next) => {
                        n = *n_next;
                    },
                    None => {
                        n.next = Some(Box::new(node));
                    }
                }
            }
            },
            None => {
            self.head = Some(node);
            }
        }
    }
}

pub fn work() {
    println!("it works");
}
