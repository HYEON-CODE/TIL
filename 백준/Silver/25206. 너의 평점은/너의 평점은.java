import java.util.Scanner;

public class Main{

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        double score[] = {4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0.0};
        String rank[] = {"A+", "A0", "B+", "B0", "C+", "C0", "D+", "D0", "F"};
        double result_score=0, result_sum=0;
        for(int i=0; i<20; i++){
            sc.next();
            double input_score = sc.nextDouble(); 
            String input_rank = sc.next();
            if (input_rank.equals("P")){
                continue;
            }
            else{
                result_sum += input_score;
                for(int j=0; j<9; j++){
                    if(input_rank.equals(rank[j])){
                        result_score += (score[j]*input_score);
                        break;
                    }
                }
            }
        }
        System.out.printf("%.6f\n", result_score/result_sum);
    }
}