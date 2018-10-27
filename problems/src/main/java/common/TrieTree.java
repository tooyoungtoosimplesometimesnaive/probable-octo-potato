package common;

import java.util.*;

public class TrieTree {
    public static class Node {
        public boolean isWord = false;
        public Map<Character, Node> children = new HashMap<>();
        @Override
        public String toString() {
            return "{isWord=" + isWord + ",children={" + children + "}}";
        }
    }

    private Node root;

    public TrieTree() {
        root = new Node();
    }

    public TrieTree(List<String> words) {
        root = new Node();
        for (String word : words) {
            insert(word);
        }

    }

    public void insert(String word) {
        if (word == null) {
            return;
        }
        Node cur = root;
        for (int i = 0; i < word.length(); i++) {
            char c = word.charAt(i);
            if (!cur.children.containsKey(c)) {
                cur.children.put(c, new Node());
            }

            cur = cur.children.get(c);

            if (i == word.length() - 1) {
                cur.isWord = true;
                break;
            }
        }
    }

    public void delete(String word) {
        // Assume that the word to be deleted is in the Trie Tree
        Deque<Node> stack = new ArrayDeque<>();
        Node cur = root;
        for (int i = 0; i < word.length(); i++) {
            char c = word.charAt(i);
            Node next = cur.children.get(c);
            if (next == null) {
                return;
            }
            stack.offerFirst(next);
            cur = next;
        }
        cur.isWord = false;
        remove(word, stack);
    }

    private void remove(String word, Deque<Node> stack) {
        for (int i = 0; i < word.length(); i++) {
            Node cur = stack.pollFirst();
            if (!cur.isWord && cur.children.size() == 0) {
                Node parent = stack.peekFirst();
                char c = word.charAt(word.length() - 1 - i);
                parent.children.remove(c);
            } else {
                break;
            }
        }
    }

    public boolean search(String word) {
        if (word == null || word.length() == 0) {
            return false;
        }
        Node cur = root;
        for (int i = 0; i < word.length(); i++) {
            char c = word.charAt(i);
            cur = cur.children.get(c);
            if (cur == null) {
                return false;
            }
        }
        return cur.isWord;
    }

    public List<String> searchPrefix(String prefix) {
        Node cur = root;
        List<String> result = new ArrayList<>();
        char[] array = prefix.toCharArray();
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < array.length; i++) {
            char c = array[i];
            sb.append(c);
            if (cur.children.get(c) == null) {
                return result;
            } else {
                cur = cur.children.get(c);
            }
        }

        dfsSearch(cur, sb, result);
        return result;
    }

    private void dfsSearch(Node current, StringBuilder sb, List<String> result) {
        if (current.isWord) {
            result.add(sb.toString());
        }
        for (Map.Entry<Character, Node> entry : current.children.entrySet()) {
            sb.append(entry.getKey());
            dfsSearch(entry.getValue(), sb, result);
            sb.deleteCharAt(sb.length() - 1);
        }
    }
}
