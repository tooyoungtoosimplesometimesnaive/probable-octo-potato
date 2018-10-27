package common;

import java.util.List;
import java.util.Set;

public class DFSParadigms {

  public DFSParadigms() {
  }


  public static void allSubsets_1(List<Integer> input, List<Integer> current, int i) {
    if (i == input.size()) {
      System.out.println(current);
      return;
    }
    allSubsets_1(input, current, i + 1);
    current.add(input.get(i));
    allSubsets_1(input, current, i + 1);
    current.remove(current.size() - 1);
  }

  public static void allSubsets_2(List<Integer> input, List<Integer> current, int i) {
    System.out.println(current);
    for (int k = i; k < input.size(); k++) {
      current.add(input.get(k));
      // This k + 1 is very important.
      allSubsets_2(input, current, k + 1);
      current.remove(current.size() - 1);
    }
  }

  public static void allPermutation(List<Integer> input, int i) {
    if (i == input.size()) {
      System.out.println(input);
    }
    for (int k = i; k < input.size(); k++) {
      swap(input, k, i);
      allPermutation(input, i + 1);
      swap(input, k, i);
    }
  }

  public static void swap(List<Integer> input, int i, int j) {
    int t = input.get(i);
    input.set(i, input.get(j));
    input.set(j, t);
  }

  public static void allPermutation_2(List<Integer> input, List<Integer> current, Set<Integer> visited) {
    if (current.size() == input.size()) {
      System.out.println(current);
      return;
    }
    for (int i : input) {
      if (!visited.contains(i)) {
        visited.add(i);
        current.add(i);
        allPermutation_2(input, current, visited);
        current.remove(current.size() - 1);
        visited.remove(i);
      }
    }
  }
}
