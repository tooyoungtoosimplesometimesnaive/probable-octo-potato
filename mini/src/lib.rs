mod mini;

#[cfg(test)]
mod tests {
    use mini::Node;
    use mini::List;
    use mini::TreeNode;

    #[test]
    fn it_works() {
        assert_eq!(2 + 2, 4);
    }

    #[test]
    fn test_node() {
        let mut x = Node { val: "m", l: None, r: None };
        x.insert("z");
        x.insert("b");
        x.insert("c");
        assert!(x == Node {
            val: "m",
            l: Some(Box::new(Node {
                val: "b",
                l: None,
                r: Some(Box::new(Node { val: "c", l: None, r: None })),
            })),
            r: Some(Box::new(Node { val: "z", l: None, r: None })),
        });
    }

    #[test]
    fn test_list() {
        use mini::len;
        let a = List::Cons(5, Box::new(List::Nil));
        assert_eq!(len(&a), 1);
    }

    #[test]
    fn test_list2() {
        use mini::len2;
        use mini::List2::Cons;
        use mini::List2::Nil;
        use std::rc::Rc;

        let a = Rc::new(Cons(5, Rc::new(Cons(10, Rc::new(Nil)))));
        let b = Cons(3, Rc::clone(&a));
        let c = Cons(4, Rc::clone(&a));

        assert_eq!(len2(&*a), 2);
        assert_eq!(len2(&b), 3);
        assert_eq!(len2(&c), 3);
    }

    #[test]
    fn test_tree_node() {
        use mini::total_node;
        use mini::depth;

        let r1 = TreeNode::Cons(Box::new(TreeNode::Nil), 5, Box::new(TreeNode::Nil));
        assert_eq!(total_node(&r1), 1);
        assert_eq!(depth(&r1), 1);

        let r2 = TreeNode::Cons(
            Box::new(TreeNode::Cons(
                    Box::new(TreeNode::Nil), 3, Box::new(TreeNode::Cons(Box::new(TreeNode::Nil), 2, Box::new(TreeNode::Nil)))
                    )), 1, Box::new(TreeNode::Cons(Box::new(TreeNode::Cons(Box::new(TreeNode::Nil), 4, Box::new(TreeNode::Nil))), 5, Box::new(TreeNode::Nil)))
                );
        assert_eq!(total_node(&r2), 5);
        assert_eq!(depth(&r2), 3);
    }
}

