mod mini;

#[cfg(test)]
mod tests {
    use mini;

    #[test]
    fn it_works() {
        assert_eq!(2 + 2, 4);
        mini::work();
    }

    #[test]
    fn test_list_node() {
        let n1 = mini::ListNode {val: 1, next:None};
        assert_eq!(n1.val, 1);

        let mut l = mini::LinkedList {head: None, size: 0};
        let n2 = mini::ListNode {val: 2, next: None};
        l.add(n2);

        assert_eq!(l.size, 1);
    }
}

