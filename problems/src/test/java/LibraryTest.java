/*
 * This Java source file was generated by the Gradle 'init' task.
 */
import common.ConnectedComponents;
import common.DFSParadigms;
import common.Graph;

import java.util.*;

import org.junit.Assert;
import org.junit.Test;

public class LibraryTest {

    @Test
    public void testTopologicalSort() {
        Assert.assertEquals(new TopologicalSort(new Graph() {{ addEdge(1, 3); addEdge(1, 2); addEdge(3, 2); addEdge(4, 2); }})
                .sort().toString()
                ,
                "[[1, 3, 4, 2], [1, 4, 3, 2], [4, 1, 3, 2]]"
        );

        Assert.assertEquals(new TopologicalSort(new Graph() {{ addEdge(1, 2); addEdge(2, 3); addEdge(3, 4); addEdge(4, 5);}})
                .sort().toString(),
                "[[1, 2, 3, 4, 5]]"
        );

        Assert.assertEquals(new TopologicalSort(new Graph() {{ addEdge(1, 2); addEdge(2, 3); addEdge(3, 4);addVertex(5);}})
                .sort().toString(),
                "[[1, 2, 3, 4, 5], [1, 2, 3, 5, 4], [1, 2, 5, 3, 4], [1, 5, 2, 3, 4], [5, 1, 2, 3, 4]]"
        );
    }

    @Test
    public void testToggleLightBulbs() {
        ToggleLightBulbs tlb = new ToggleLightBulbs(4);
        tlb.solve();
    }

    @Test
    public void testConnectedComponents() {
        Graph<Integer> graph = new Graph<Integer>() {{
            addEdge(1, 2);
            addEdge(2, 3);
            addEdge(4, 5);
            addEdge(4, 6);
            addEdge(7, 8);
        }};
        ConnectedComponents c = new ConnectedComponents(graph);
        List<Set<Integer>> components = c.getConnectedComponents();
        for (Set<Integer> component : components) {
            for (Integer v : component) {
                System.out.print(v + " ");
            }
            System.out.println();
        }
    }


    @Test
    public void allSubsets() {
//        DFSParadigms.allSubsets_1(Arrays.asList(1,2,3,4), new ArrayList<Integer>(), 0);
//        DFSParadigms.allSubsets_2(Arrays.asList(1,2,3,4), new ArrayList<Integer>(), 0);
      DFSParadigms.allPermutation(Arrays.asList(1,2,3), 0);
      System.out.println("---");
      DFSParadigms.allPermutation_2(Arrays.asList(1,2,3), new ArrayList<>(), new HashSet<>());
    }
}
