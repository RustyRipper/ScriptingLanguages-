import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Process {

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

        List<String> lines = readLines();
        System.out.println(lines);


    }
}
