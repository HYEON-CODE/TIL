import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n, m;
        int[][] array_a;
        int[][] result;
        n = sc.nextInt();
        m = sc.nextInt();
        array_a = new int[n][m];
        result = new int[n][m];

        for(int i=0; i<n; i++){
            for(int j=0; j<m; j++){
                    array_a[i][j]=sc.nextInt();
            }
        }

        for(int i=0; i<n; i++){
            for(int j=0; j<m; j++){
                result[i][j] = sc.nextInt() + array_a[i][j];
                System.out.print(result[i][j]);
                if(!(i==n-1 && j==m-1)){
                    System.out.print(' ');
                }
            }
            System.out.println();
        }
        sc.close();
    }
}