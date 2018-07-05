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
        let a = mini::list_node {val: 1, next:None};
        assert_eq!(a.val, 1);
    }
}

