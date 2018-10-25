package common;

import common.Graph;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Deque;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;

public class ConnectedComponents<T extends Comparable> {
  private Graph<T> graph;

  public ConnectedComponents(Graph g) {
    graph = g;
  }

  public List<Set<T>> getConnectedComponents() {
    Set<T> allVertices = new HashSet<>();
    for (Map.Entry<T, List<T>> entry : graph.adjacencyList.entrySet()) {
      allVertices.add(entry.getKey());
    }

    Set<T> visited = new HashSet<>();
    List<Set<T>> listOfConnectedComponents = new ArrayList<>();
    int numOfComponents = 0;
    for (T vertex : allVertices) {
      if (!visited.contains(vertex)) {
        numOfComponents += 1;
        Deque<T> queue = new ArrayDeque<>();
        queue.offerLast(vertex);
        Set<T> component = new HashSet<>();
        component.add(vertex);
        while (!queue.isEmpty()) {
          T top = queue.pollFirst();
          visited.add(top);
          for (T neighbor : graph.adjacencyList.get(top)) {
            if (!visited.contains(neighbor)) {
              queue.offerLast(neighbor);
              component.add(neighbor);
              visited.add(neighbor);
            }
          }
        }
        listOfConnectedComponents.add(component);
      }
    }

    System.out.println(numOfComponents);
    return listOfConnectedComponents;
  }
}
