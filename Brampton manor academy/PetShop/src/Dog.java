public class Dog {
    private String name;
    private String breed;
    private int age;

    public Dog(String n, String b, int a){
        name=n;
        breed=b;
        age=a;

    }

    public String getName(){
        return name;
    }
    public String getBreed(){
        return breed;
    }
    public int getAge(){
        return age;
    }
    public void bark(){
        System.out.println(name+" says 'bark'");
    }
    public void eatBiscuit(){
        System.out.println(name+" says 'yum'");
    }
    public void getOlder(){
        age++;
        System.out.println(age);
    }


}
