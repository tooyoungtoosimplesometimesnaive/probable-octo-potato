package common;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/*
 * T is the type of the Node, this is a undirected unweighted graph
 */
public class Graph<T extends Comparable> {
    public Map<T, List<T>> adjacencyList;
    public Map<T, Integer> indegree;
    public Graph() {
        adjacencyList = new HashMap<>();
        indegree = new HashMap<>();
    }

    public void addEdge(T fromVertex, T toVertex) {
        addVertex(fromVertex);
        addVertex(toVertex);
        // Do adding
        adjacencyList.get(fromVertex).add(toVertex);
        indegree.put(toVertex, indegree.get(toVertex) + 1);
    }

    public void addVertex(T vertex) {
        if (!adjacencyList.containsKey(vertex)) {
            adjacencyList.put(vertex, new ArrayList<>());
        }
        if (!indegree.containsKey(vertex)) {
            indegree.put(vertex, 0);
        }
    }
}
