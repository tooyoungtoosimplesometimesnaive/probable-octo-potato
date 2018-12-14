package datastructures;

import java.util.Arrays;

public class MyHashMap<K, V> {
    public static class Node<K, V> {
        K key;
        V value;
        Node<K, V> next;
        public Node(K key, V value) {
            this.key = key;
            this.value = value;
        }

        public K getKey() {
            return key;
        }

        public void setKey(K key) {
            this.key = key;
        }

        public V getValue() {
            return value;
        }

        public void setValue(V value) {
            this.value = value;
        }
    }

    public static final int DEFAULT_CAPACITY = 16;
    public static final float DEFAULT_LOAD_FACTOR = 0.75f;

    private Node<K, V>[] array;
    private float loadFactor;
    private int size;

    public MyHashMap() {
        this(DEFAULT_CAPACITY, DEFAULT_LOAD_FACTOR);
    }

    public MyHashMap(int cap, float loadFactor) {
        if (cap < 0) {
            throw new IllegalArgumentException("Capacity must be positive");
        }
        this.size = 0;
        this.loadFactor = loadFactor;
        this.array = (Node<K, V>[]) new Node[cap];
    }

    public int size() {
        return size;
    }

    public boolean isEmpty() {
        return size == 0;
    }

    public void clear() {
        Arrays.fill(array, null);
        size = 0;
    }

    // Non negative
    private int hash(K key) {
        if (key == null) {
            return 0;
        }
        // hashCode()
        // int code = key.hashCode()
        // return code >= 0 ? code : -code;
        // int range = [-2^31, 2^31 - 1]
        // -Integer.MIN_VALUE = Integer.MIN_VALUE -> overflow
        return key.hashCode() & 0x7fffffff;
        // Reason: java's % return remainder rather than modulus, The remainder can be negative
    }

    private int getIndex(K key) {
        return hash(key) % array.length;
    }

    private boolean equalsValue(V v1, V v2) {
        // v1, v2 all possibly to be null
        if (v1 == null && v2 == null) {
            return true;
        }
        if (v1 == null || v2 == null) {
            return false;
        }
        return v1.equals(v2);
        // return v1 == v2 || v1 != null && v1.equals(v2)
    }

    public boolean containsValue(V value) {
        // special case
        if (isEmpty()) {
            return false;
        }

        for (Node<K, V> node : array) {
            while (node != null) {
                if (equalsValue(node.value, value)) {
                    return true;
                }
                node = node.next;
            }
        }
        return false;
    }

    private boolean equalsKey(K k1, K k2) {
        // k1, k2 all possibly to be null
        if (k1 == null && k2 == null) {
            return true;
        }
        if (k1 == null || k2 == null) {
            return false;
        }
        return k1.equals(k2);
        // return k1 == k2 || k1 != null && k1.equals(k2)
    }

    public boolean containsKey(K key) {
        // special case
        int index = getIndex(key);
        Node<K, V> node = array[index];
        while (node != null) {
            if (equalsKey(node.key, key)) {
                return true;
            }
            node = node.next;
        }
        return false;
    }

    public V get(K key) {
        int index = getIndex(key);
        Node<K, V> node = array[index];
        while (node != null) {
            if (equalsKey(node.key, key)) {
                return node.value;
            }
            node = node.next;
        }
        return null;
    }

    // insert/update
    // if the key already exists, return the old corresponding value
    // if the key not exists, return null
    public V put(K key, V value) {
        int index = getIndex(key);
        Node<K, V> head = array[index];
        Node<K, V> node = head;

        while (node != null) {
            if (equalsKey(node.key, key)) {
                V result = node.value;
                node.value = value; // Update
                return result;
            }
            node = node.next;
        }

        // append the new node before the head and update the new head
        // insert operation
        Node<K, V> newNode = new Node(key, value);
        newNode.next = head;
        array[index] = newNode;
        size ++;

        if (needRehashing()) {
            rehashing();
        }
        return null;
    }

    private boolean needRehashing() {
        float r = (size + 0.0f) / array.length;
        return r >= loadFactor;
    }

    private boolean rehashing() {
        // new double sized array
        // for each node in the old array
        // do the put() operation to the larger array
        return false;
    }

    // if the key exists, remove the <key, value> pair from the HashMap. return the value.
    // If the key not exists, return null
    public V remove(K key) {
        // get index
        // delete operation on the linked list
        // size --
        return null;
    }
}
