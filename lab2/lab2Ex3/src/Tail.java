import java.util.ArrayList;
import java.util.Scanner;

public class Tail {
    private static int paramLines;
    private static boolean paramE;
    private static int sizeOfFile;

    public static void main(String[] args) {
        int errorCode = 0;
        getParams(args);
        ArrayList<String> lines = readLines();
        int difference = paramLines - sizeOfFile;

        for (int i = 0; i < paramLines; i++) {
            try {
                if (lines.get(i) == null)
                    throw new IndexOutOfBoundsException("Error index = null");
                System.out.println(lines.get(i));
            } catch (IndexOutOfBoundsException e) {
                if (!paramE)
                    System.out.println(e.getMessage());
                i = paramLines;
            }
        }

        if (difference > 0 && !paramE) {
            errorCode = 2;
            System.out.println("Zabraklo " + difference + " linii do wypisania");
        }

        System.out.println("ErrorCode " + errorCode);
        System.exit(errorCode);
    }

    private static void getParams(String[] args) {
        for (String arg : args) {
            if (arg.equals("-e")) {
                paramE = true;
            } else if (arg.contains("=") && arg.contains("--")) {
                String[] split = arg.split("=");
                if (split.length > 1) {
                    try {
                        if ("--lines".equals(split[0])) {
                            paramLines = Integer.parseInt(split[1]);
                        }
                    } catch (NumberFormatException ex) {
                        System.out.println("Error with parse");
                    }
                }
            }
        }
    }

    public static ArrayList<String> readLines() {
        Scanner scanner = new Scanner(System.in);
        ArrayList<String> lines = new ArrayList<>(paramLines);
        ArrayList<String> finalLines = new ArrayList<>(paramLines);

        for (int i = 0; i < paramLines; i++) {
            lines.add(null);
        }
        int index = 0;
        for (int i = 0; scanner.hasNextLine(); i++) {
            String line = scanner.nextLine();
            if (i < lines.size()) {
                lines.set(i, line);
                index = i;
            }
            sizeOfFile++;
            if (i == paramLines - 1)
                i = -1;
        }

        if(paramLines>sizeOfFile){
            index=-1;
        }

        for(int i=index+1;finalLines.size()!=paramLines;i++){
            if(i>=paramLines){
                i=-1;
            }
            else{
                if(lines.get(i)!=null)
                    finalLines.add(lines.get(i));
                else
                    finalLines.add(null);
            }
        }
        return finalLines;
    }


}
