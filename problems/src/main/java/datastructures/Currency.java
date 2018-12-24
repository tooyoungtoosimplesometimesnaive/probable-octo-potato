package datastructures;


import java.util.HashMap;
import java.util.Map;

class Currency {
    private Map<String, String> root = new HashMap<>();
    private Map<String, Double> dist = new HashMap<>();
    public Currency(String[] currency1, String[] currency2, Double[] value) {
        int len = currency1.length;
        for (int i = 0; i < len; i ++) {
            String p1 = findRoot(currency1[i]);
            String p2 = findRoot(currency2[i]);
            root.put(p1, p2);
            dist.put(p1, dist.get(currency2[i]) * value[i] / dist.get(currency1[i]));
        }
    }

    public Double[] getQuery(String[][] q) {
        Double[] result = new Double[q.length];

        for (int i = 0; i < q.length; i ++) {
            String q1 = q[i][0];
            String q2 = q[i][1];
            if (!root.containsKey(q1) || !root.containsKey(q2)) {
                result[i] = null;
                continue;
            }
            String r1 = findRoot(q1);
            String r2 = findRoot(q2);
            if (r1.equals(r2)) {
                result[i] = dist.get(q1) / dist.get(q2);
            } else {
                result[i] = null;
                continue;
            }
        }
        return result;
    }


    //
    private String findRoot(String s) {
        if (!root.containsKey(s)) {
            root.put(s, s);
            dist.put(s, 1.0);
            return s;
        }

        if (root.get(s).equals(s))
            return s;

        String parent = root.get(s);
        String p = findRoot(parent);
        root.put(s, p);
// calculate distance:
        dist.put(s, dist.get(s) * dist.get(parent));
        return p;
    }
}

