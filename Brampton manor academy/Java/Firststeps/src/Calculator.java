public class Calculator {

    private static int addition(int a, int b){
        int answer=a+b;
        return answer;
    }
    private static int subtraction(int a,int b){
        int answer=a-b;
        return answer;
    }
    private static int multiplication(int a,int b) {
        int answer = a * b;
        return answer;
    }
    private static float division(int a,int b) {
        int answer = a / b;
        return answer;
    }
    private static double power(int a,int b){
        return Math.pow(a,b);
    }


    public static void main(String[] args){
        String choice=args[0];
        int firstValue=Integer.parseInt(args[1]);
        int secondValue=Integer.parseInt(args[2]);
        switch(choice){
            case "addition":
                System.out.println(addition(firstValue,secondValue));
                break;
            case "subtraction":
                System.out.println(subtraction(firstValue,secondValue));
                break;
            case "multiplication":
                System.out.println(multiplication(firstValue,secondValue));
                break;
            case "division":
                System.out.println(division(firstValue,secondValue));
                break;
            case "power":
                System.out.println(power(firstValue,secondValue));
                break;

        }



    }
}
