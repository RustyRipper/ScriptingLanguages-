import java.io.File;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.Objects;

public class Paths {
    private static boolean param_R = false, param_d = false, param_s = false, sort = false;
    private static String sortOption;

    public static void main(String[] args) {

        for (int i = 0; i < args.length; i++) {
            if (args[i].equals("-R"))
                param_R = true;
            if (args[i].equals("-d"))
                param_d = true;
            if (args[i].equals("-s"))
                param_s = true;
            if (args[i].equals("--sort")) {
                sort = true;
                if (args[i + 1].equals("alpha")) {
                    sortOption = "alpha";
                } else if (args[i + 1].equals("date")) {
                    sortOption = "date";
                }
            }
        }
        final String path = System.getProperty("user.dir");
        System.out.println(path);
        printFiles(path, "");
    }

    public static void printFiles(String actualPath, String indentation) {

        File file = new File(actualPath);
        ArrayList<File> files = new ArrayList<>(Arrays.asList(Objects.requireNonNull(file.listFiles())));

        if (sort) {
            if (sortOption.equals("alpha")) {
                files.sort(Comparator.comparing(File::getName));
            } else if (sortOption.equals("date")) {
                files.sort(Comparator.comparing(File::lastModified));
            }
        }

        if (files.size() > 0) {
            for (File f : files) {

                StringBuilder s = new StringBuilder(f.getName());
                boolean check = true;

                if (param_d)
                    if (!f.isDirectory())
                        check = false;

                if (check) {
                    if (param_s)
                        s.append(" [ ").append(f.length()).append(" bytes ]");
                    System.out.println(indentation + s);
                }
                if (param_R && f.isDirectory())
                    printFiles(f.getAbsolutePath(), indentation + "-----");
            }
        }
    }
}