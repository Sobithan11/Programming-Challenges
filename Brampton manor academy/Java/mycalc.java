public class Main {
  private static int addition(int a,int b){
    int answer=a+b;
    return answer;
  }
  private static int subtraction(int a,int b){
    int answer=a-b;
    return answer;
  }
  private static int multiplication(int a,int b){
    int answer=a*b;
    return answer;
  }
  private static int division(int a,int b){
    int answer=a/b;
    return answer;
  private static int power(int a,int b){
    int answer=lang.Math.pow( a,b);
    return answer;
  }
  public static void main(String[] args){
      
      String choice=args[0];
      switch(choice){
          case "addition":
              int firstvalue=Integer.parseInt(args[1]);
              int secondvalue=Integer.parseInt(args[2]);
              int answer=addition(firstvalue,secondvalue);
              System.out.println(answer);
              break;
          case "subtraction":
              int firstvalue=Integer.parseInt(args[1]);
              int secondvalue=Integer.parseInt(args[2]);
              int answer=subtraction(firstvalue,secondvalue);
              System.out.println(answer);
              break;
          case" multiplication":
              int firstvalue=Integer.parseInt(args[1]);
              int secondvalue=Integer.parseInt(args[2]);
              int answer=multiplication(firstvalue,secondvalue);
              System.out.println(answer);
              break;
          case "division":
              int firstvalue=Integer.parseInt(args[1]);
              int secondvalue=Integer.parseInt(args[2]);
              int answer=division(firstvalue,secondvalue);
              System.out.println(answer);
              break;
          case "power":
              int firstvalue=Integer.parseInt(args[1]);
              int secondvalue=Integer.parseInt(args[2]);
              int answer=power(firstvalue,secondvalue);
              System.out.println(answer);
              break;
       
      }
  }
}
