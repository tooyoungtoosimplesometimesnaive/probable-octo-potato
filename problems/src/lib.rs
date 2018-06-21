#[cfg(test)]
mod tests {
    use std::mem;
    #[test]
    fn it_works() {
        assert_eq!(2 + 2, 4);
    }


    #[test]
    fn t1() {
        assert_eq!(second_largest(vec![1]), None);
        assert_eq!(second_largest(vec![1,2]), Some(1));
        assert_eq!(second_largest(vec![3,1,2]), Some(2));
        assert_eq!(second_largest(vec![3,1,2,2,2]), Some(2));
        assert_eq!(second_largest(vec![3,1,2,100,99]), Some(99));
        assert_eq!(second_largest(vec![3,1,2,1,1,1]), Some(2));
        // assert_eq!(second_largest(vec![3,3,2,3,1,1]), Some(2));
    }

    #[test]
    fn t2() {
        assert_eq!(second_largest_2(vec![1]), None);
        assert_eq!(second_largest_2(vec![1,2]), Some(1));
        assert_eq!(second_largest_2(vec![3,1,2]), Some(2));
        assert_eq!(second_largest_2(vec![3,1,2,2,2]), Some(2));
        assert_eq!(second_largest_2(vec![3,1,2,100,99]), Some(99));
        assert_eq!(second_largest_2(vec![3,1,2,1,1,1]), Some(2));
        assert_eq!(second_largest_2(vec![3,3,2,3,1,1]), Some(2));
    }

    fn second_largest(a: Vec<u8>) -> Option<u8> {
        if a.len() < 2 {
            return None;
        }

        let mut l = a[0];
        let mut s = a[1];

        if l < s {
            mem::swap(&mut s, &mut l);
        }

        for i in a {
            if i > l {
                let m = l;
                l = i;
                s = m;
            } else if i < l && i > s {
                s = i;
            }
        }

        Some(s)
    }

    fn second_largest_2(a: Vec<u8>) -> Option<u8> {
        if a.len() < 2 {
            return None;
        }

        let mut l = a[0];
        for i in &a {
            if i > &l {
                l = *i;
            }
        }

        let mut s = 0;

        for i in &a {
            if i == &l {
                continue;
            }

            if i > &s {
                s = *i;
            }
        }

        Some(s)
    }

    #[test]
    fn t3() {
        assert_eq!(min_max_sum(vec![1,2,3,4,5]), (14, 10));
    }

    fn min_max_sum(a: Vec<u8>) -> (u8, u8) {
        let mut min = a[0];
        let mut max = a[0];
        let mut sum = 0;
        for i in a {
            if i > max {
                max = i;
            }
            if i < min {
                min = i;
            }
            sum += i;
        }
        (sum - min, sum - max)
    }
}
