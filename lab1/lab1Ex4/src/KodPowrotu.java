import java.util.*;
import java.util.stream.Collectors;

public class KodPowrotu {

    public static void main(String[] args) {

        Map<String, Integer> map = Arrays
                .stream(args)
                .collect(Collectors.toMap(e -> e, e -> 0));

        Scanner scanner = new Scanner(System.in);
        String text = scanner.nextLine();
        String[] array = text.split(" ");

        for (String s : array) {
            if (map.containsKey(s)) {
                map.put(s, map.get(s) + 1);
            }
        }

        LinkedHashMap<String, Integer> sortedMap = map.entrySet()
                .stream()
                .sorted(Map.Entry.comparingByValue(Comparator.reverseOrder()))
                .collect(Collectors.toMap(
                        Map.Entry::getKey,
                        Map.Entry::getValue,
                        (oldValue, newValue) -> oldValue,
                        LinkedHashMap::new));

        Optional<String> firstKey = sortedMap.keySet().stream().findFirst();

        int index = 0;

        if (firstKey.isPresent() && sortedMap.get(firstKey.get()) != 0) {
            for (int i = 0; i < args.length; i++) {
                if (args[i].equals(firstKey.get())) {
                    index = i + 1;
                }
            }
        }
        System.exit(index);
    }
}
