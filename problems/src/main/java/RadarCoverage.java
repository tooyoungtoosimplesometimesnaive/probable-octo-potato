import common.UnionFind;
import java.util.Arrays;
import java.util.Collections;
import java.util.Comparator;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class RadarCoverage {
  public RadarCoverage() {
  }

  public static class Radar implements Comparable<Radar>, Comparator<Radar> {
    public double x;
    public double y;
    public double radius;
    public Radar(double x, double y, double radius) {
      this.x = x;
      this.y = y;
      this.radius = radius;
    }

    public double distance(double px, double py) {
      return Math.sqrt((px - x) * (px - x) + (py - y) * (py - y));
    }

    public double distance(Radar r) {
      return distance(r.x, r.y);
    }

    /**
     * A simple implementation of the compareTo.
     */
    @Override
    public int compareTo(Radar r) {
      return r.distance(0, 0) > distance(0, 0) ? -1 : 1;
    }

    @Override
    public int compare(Radar a, Radar b) {
      return (int)(a.y - b.y);
    }

    @Override
    public String toString() {
      return "R{" + x + "," + y + "," + radius + "}";
    }
  }

  // Imagine the two lines that represents the road are:
  // y = 0 and y = roadWidth
  // in the 2D coordinate
  public boolean canPass(List<Radar> radars, double roadWidth) {

    // Construct the union find:
    UnionFind uf = new UnionFind(radars.size());
    for (int i = 0; i < radars.size() - 1; i++) {
      for (int j = i + 1; j < radars.size(); j++) {
        if (radars.get(i).distance(radars.get(j)) < radars.get(i).radius + radars.get(j).radius) {
          uf.union(i, j);
        }
      }
    }

    // Collect all components:
    Map<Integer, List<Radar>> components = new HashMap<>();
    for (int i = 0; i < radars.size(); i++) {
      int root = uf.root(i);
      if (components.containsKey(root)) {
        components.get(root).add(radars.get(i));
      } else {
        components.put(root, Arrays.asList(radars.get(i)));
      }
    }

    for (Map.Entry<Integer, List<Radar>> entry : components.entrySet()) {
      List<Radar> radarList = entry.getValue();
      // Since this is already connected, maybe we don't need this.
      // Collections.sort(radarList);

      double start = 0;
      double end = 0;
      for (Radar r : radarList) {

        if (r.y - r.radius <= start) {
          start = r.y - r.radius;
        }
        if (r.y + r.radius >= end) {
          end = r.y + r.radius;
        }
      }

      if (start <= 0 && end >= roadWidth) {
        return false;
      }
    }

    return true;
  }

}
