#[derive(Copy, Clone)]
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
        if self.head.is_none() {
            self.head = Some(node);
        } else {

            let mut n = self.head.unwrap();
            loop {
                match n.next {
                    Some(n_next) => {
                        n = *n_next;
                        break;
                    },
                    None => {
                        n.next = Some(Box::new(node));
                    }
                }
            }
        }
    }
}

pub fn work() {
    println!("it works");
}
