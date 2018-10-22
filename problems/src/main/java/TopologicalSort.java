import java.util.*;
import java.util.stream.Collectors;

public class TopologicalSort<T extends Comparable> {

    private Graph<T> graph;
    public TopologicalSort(Graph graph) {
        this.graph = graph;
    }

    /**
     * Get all the topological sort of the graph
     * @return a list of list of node
     */
    public List<List<T>> sort() {
        int numOfVertices = graph.adjacencyList.size();
        List<T> initialZeroInDegrees = graph.indegree.keySet()
                .stream().filter(k -> graph.indegree.get(k) == 0).collect(Collectors.toList());
        List<List<T>> result = new ArrayList<>();
        for (T start : initialZeroInDegrees) {
            List<T> list = new ArrayList<>();
            list.add(start);
            sort(start, numOfVertices, list, result);
        }
        System.out.println(result);
        return result;
    }

    public void sort(T start, int numOfVertices, List<T> current, List<List<T>> result) {
        if (current.size() == numOfVertices) {
            result.add(new ArrayList<>(current));
            return;
        }

        for (T i : graph.adjacencyList.get(start)) {
            graph.indegree.put(i, graph.indegree.get(i) - 1);
        }

        List<T> zeroInDegrees = graph.indegree.keySet()
                .stream().filter(k -> graph.indegree.get(k) == 0)
                .collect(Collectors.toList());

        for (T next : zeroInDegrees) {
            if (!current.contains(next)) {
                current.add(next);
                sort(next, numOfVertices, current,result);
                current.remove(current.size() - 1);
            }
        }
        for (T i : graph.adjacencyList.get(start)) {
            graph.indegree.put(i, graph.indegree.get(i) + 1);
        }
    }
}
