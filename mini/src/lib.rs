mod mini;

#[cfg(test)]
mod tests {
    use mini::Node;

    #[test]
    fn it_works() {
        assert_eq!(2 + 2, 4);
    }

    #[test]
    fn test_list_node() {
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
}

