import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Process {

    private static int paramIgnoreFirst, paramIgnoreLast;
    private static ArrayList<Integer> paramProject;
    private static String paramDelimiter, paramSeparator, paramSelect;

    public static List<String> readLines() {
        Scanner scanner = new Scanner(System.in);
        List<String> lines = new ArrayList<>();
        String line;
        while (scanner.hasNextLine() && !((line = scanner.nextLine()).equals(""))) {
            lines.add(line);
        }
        return lines;

    }

    public static void main(String[] args) {
        getParams(args);
        List<String> lines = readLines();
        System.out.println(lines);

        System.out.println(paramIgnoreFirst);
        System.out.println(paramIgnoreLast);
        System.out.println(paramSeparator);
        System.out.println(paramDelimiter);
        System.out.println(paramProject);
        System.out.println(paramSelect);



    }

    private static void getParams(String[] args) {
        for (String arg : args) {
            if (arg.contains("=") && arg.contains("--")) {
                String[] split = arg.split("=");
                if (split.length > 1) {
                    try {
                        switch (split[0]) {
                            case "--ignorefirst" -> paramIgnoreFirst = Integer.parseInt(split[1]);
                            case "--ignorelast" -> paramIgnoreLast = Integer.parseInt(split[1]);
                            case "--delimiter" -> paramDelimiter = split[1];
                            case "--separator" -> paramSeparator = split[1];
                            case "--select" -> paramSelect = split[1];
                            case "--project" -> {
                                paramProject = new ArrayList<>();
                                String[] columns = split[1].split(",");
                                for(String column: columns){
                                    paramProject.add(Integer.valueOf(column));
                                }
                            }
                        }
                    } catch (NumberFormatException ex) {
                        System.out.println("Error with parse");
                    }
                }
            }


        }
    }
}
