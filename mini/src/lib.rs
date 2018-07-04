mod mini;

#[cfg(test)]
mod tests {
    use mini;

    #[test]
    fn it_works() {
        assert_eq!(2 + 2, 4);
        mini::work();
    }
}

