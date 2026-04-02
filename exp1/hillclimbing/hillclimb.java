import java.util.*;

public class HillClimbing {

    static Map<String, List<String>> graph = new HashMap<>();
    static Map<String, Integer> heuristic = new HashMap<>();

    public static void main(String[] args) {

        graph.put("A", Arrays.asList("B", "C"));
        graph.put("B", Arrays.asList("D", "E"));
        graph.put("C", Arrays.asList("F"));
        graph.put("D", Arrays.asList("G"));
        graph.put("E", Arrays.asList("G"));
        graph.put("F", Arrays.asList("G"));
        graph.put("G", new ArrayList<>());

        heuristic.put("A", 7);
        heuristic.put("B", 6);
        heuristic.put("C", 5);
        heuristic.put("D", 4);
        heuristic.put("E", 2);
        heuristic.put("F", 3);
        heuristic.put("G", 0);

        hillClimb("A", "G");
    }

    static void hillClimb(String start, String goal) {
        String current = start;
        System.out.print("Best path: " + current);

        while (!current.equals(goal)) {
            List<String> neighbors = graph.get(current);
            String best = current;

            for (String node : neighbors) {
                if (heuristic.get(node) < heuristic.get(best)) {
                    best = node;
                }
            }

            if (best.equals(current)) {
                System.out.println("\nReached local maximum. Stopping.");
                break;
            }

            current = best;
            System.out.print(" -> " + current);
        }
    }
}
