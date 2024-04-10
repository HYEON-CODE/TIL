import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int max = 0, temp;
        int[] index = new int[2];
    
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                temp = sc.nextInt();
                if (max <= temp) {
                    max = temp;
                    index[0] = i + 1;
                    index[1] = j + 1;
                }
            }
        }
        System.out.println(max);
        System.out.println(index[0] + " " + index[1]);
        sc.close();
    }
}
