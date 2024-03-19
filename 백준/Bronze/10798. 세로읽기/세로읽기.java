import java.util.Scanner;

public class Main{

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String arr[] = new String[5];
        
        for(int i=0; i<5; i++){
            arr[i] = sc.next();
        }

        for(int i=0; i<15; i++){
            for(int j=0; j<5; j++){
                if(arr[j].length()>i){
                    System.out.print(arr[j].charAt(i));
                }
            }
        }
    }
}