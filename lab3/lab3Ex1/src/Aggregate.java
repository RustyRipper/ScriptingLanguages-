import java.util.*;

public class Aggregate {
    private static ArrayList<Double> dataList;

    public static void main(String[] args) {

        String paramOption = getParam(args);
        dataList = getDataList();

        if (!(paramOption.equals("") || dataList.isEmpty())) {
            Double value = 0.0;
            switch (paramOption) {
                case "-min" -> value = min();
                case "-max" -> value = max();
                case "-avg" -> value = average();
                case "-sum" -> value = sum();
                case "-median" -> value = median();
                case "-variance" -> value = variance();
            }
            if (paramOption.equals("-count"))
                System.out.println(count());
            else
                System.out.println(value);
        } else {
            System.out.println("Bad param or bad input");
            System.exit(1);
        }

    }

    private static Double min() {
        if (dataList.isEmpty())
            return 0.0;

        Double min = dataList.get(0);
        for (Double d : dataList) {
            if (min > d)
                min = d;
        }
        return min;
    }

    private static Double max() {
        if (dataList.isEmpty())
            return 0.0;

        Double max = dataList.get(0);
        for (Double d : dataList) {
            if (max < d)
                max = d;
        }
        return max;
    }

    private static Double average() {
        if (dataList.isEmpty())
            return 0.0;
        return sum() / count();
    }

    private static Double sum() {
        Double sum = 0.0;
        for (Double d : dataList) {
            sum += d;
        }
        return sum;
    }

    private static int count() {
        return dataList.size();
    }

    private static Double median() {
        if (dataList.isEmpty())
            return 0.0;
        Collections.sort(dataList);
        int count = count();
        if (count % 2 == 0) {
            return (dataList.get((count / 2)) + dataList.get((count / 2) - 1)) / 2;
        }
        else {
            return dataList.get((count / 2));
        }
    }

    private static Double variance() {
        if(dataList.isEmpty())
            return 0.0;
        Double avg = average();
        int count = count();
        double variance = 0.0;
        for(Double d: dataList){
            variance+=Math.pow(d-avg,2);
        }
        return variance/count;
    }

    private static ArrayList<Double> getDataList() {
        Scanner scanner = new Scanner(System.in);
        ArrayList<Double> lines = new ArrayList<>();

        while (scanner.hasNextLine()) {
            try {
                lines.add(Double.valueOf(scanner.nextLine()));
            } catch (NumberFormatException e) {
                //System.out.println("problem with parse");
            }
        }
        return lines;
    }

    private static String getParam(String[] args) {
        if (args.length > 0)
            return args[0];
        else return "";
    }
}
