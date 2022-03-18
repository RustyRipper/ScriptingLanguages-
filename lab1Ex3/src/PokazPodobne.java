import java.util.*;
import java.util.stream.Collectors;

public class PokazPodobne {
    public static void main(String[] args) {

        if (args.length == 0) {
            args = new String[1];
            args[0] = "";
        }

        for (int i = 0; i < Objects.requireNonNull(args).length; i++) {
            System.out.println("Zmienne srodowiskowe");

            Map<String, String> env = System.getenv();
            String arg = args[i];

            LinkedHashMap<String, String> collect = env.entrySet()
                    .stream()
                    .filter(x -> x.getKey().contains(arg))
                    .sorted(Map.Entry.comparingByKey(Comparator.reverseOrder()))
                    .collect(Collectors.toMap(
                            Map.Entry::getKey,
                            Map.Entry::getValue,
                            (oldValue, newValue) -> oldValue,
                            LinkedHashMap::new)
                    );

            if (collect.isEmpty()) {
                System.out.println(args[i].toUpperCase() + " = NONE");

            } else {
                collect.forEach((k, v) -> {
                            String[] array = v.split(";");
                            System.out.print(k.toUpperCase() + " = ");
                            if (array.length == 1) {
                                System.out.println(array[0]);
                            } else {
                                System.out.println();
                                for (String a : array) {
                                    System.out.println("   " + a);
                                }
                            }
                            System.out.println("----------------");
                        }
                );
            }
        }
    }
}
