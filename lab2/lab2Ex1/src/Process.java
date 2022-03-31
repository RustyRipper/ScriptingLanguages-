import java.util.ArrayList;
import java.util.Scanner;

public class Process {

    private static int paramIgnoreFirst, paramIgnoreLast;
    private static ArrayList<Integer> paramProject;
    private static String paramDelimiter=",", paramSeparator="", paramSelect="";
    private static int errorCode = 2;


    public static void main(String[] args) {
        paramProject = new ArrayList<>();
        getParams(args);
        ArrayList<String> lines = readLines();

        if (lines.size() == 0) {
            System.exit(errorCode);
        }
        errorCode = 1;

        ArrayList<String> newLines = new ArrayList<>(lines.size());
        for (String s : lines) {
            s = ignoreFirstLast(s);
            if (!paramDelimiter.equals(""))
                s = delimiter(s);
            if (!paramSeparator.equals(""))
                s = separator(s);
            newLines.add(s);
        }

        lines = newLines;

        if (!paramProject.isEmpty())
            project(lines);


        if(!paramSelect.equals(""))
            select(lines);
        System.exit(errorCode);

    }


    public static ArrayList<String> readLines() {
        Scanner scanner = new Scanner(System.in);
        ArrayList<String> lines = new ArrayList<>();

        while (scanner.hasNextLine() ) {
            lines.add(scanner.nextLine());
        }
        return lines;

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
                                for (String column : columns) {
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

    private static String ignoreFirstLast(String s) {
        if(paramIgnoreFirst+paramIgnoreLast>s.length())
            return "";
        return s.substring(paramIgnoreFirst, s.length() - paramIgnoreLast);
    }

    private static String delimiter(String s) {

        return s.replace(paramDelimiter, "\t");
    }

    private static String separator(String s) {

        return s.replace("\t", paramSeparator);
    }

    private static void project(ArrayList<String> strings) {


        for (String s : strings) {
            String[] array = s.split(String.format("[ t%s]",paramSeparator));
            StringBuilder stringBuilder = new StringBuilder();
            for (Integer i : paramProject) {

                if (i <= array.length && i >=1)
                    stringBuilder.append(array[i-1]).append(" ");
            }
            if (!stringBuilder.toString().equals("")){
                errorCode = 0;
            }
            System.out.println(stringBuilder);
        }
    }

    private static void select(ArrayList<String> strings) {


        for (String s : strings) {
            if (s.contains(paramSelect)) {
                errorCode = 0;
                System.out.println(s);
            }
        }
    }
}
