#[derive(PartialEq)]
pub struct Node<'a> {
    pub val: &'a str,
    pub l: Option<Box<Node<'a>>>,
    pub r: Option<Box<Node<'a>>>,
}

impl<'a> Node<'a> {
    pub fn insert(&mut self, new_val: &'a str) {
        if self.val == new_val {
            return
        }
        let target_node = if new_val < self.val { &mut self.l } else { &mut self.r };
        match target_node {
            &mut Some(ref mut subnode) => subnode.insert(new_val),
            &mut None => {
                let new_node = Node { val: new_val, l: None, r: None };
                let boxed_node = Some(Box::new(new_node));
                *target_node = boxed_node;
            }
        }
    }
}

pub enum List {
    Cons(i32, Box<List>),
    Nil,
}

pub fn len(l: &List) -> u8 {
    match l {
        List::Cons(_, tl) => len(&*tl) + 1,
        List::Nil => 0,
    }
}

pub enum TreeNode {
    Cons(Box<TreeNode>, i32, Box<TreeNode>),
    Nil,
}

pub fn total_node(root: &TreeNode) -> u8 {
    match root {
        TreeNode::Cons(left, _, right) => 1 +  total_node(&*left) + total_node(&*right),
        TreeNode::Nil => 0,
    }
}

pub fn depth(root: &TreeNode) -> u8 {
    use std::cmp;

    match root {
        TreeNode::Cons(left, _, right) => 1 + cmp::max(depth(&*left), depth(&*right)),
        TreeNode::Nil => 0,
    }
}

