public class Shop {
    public static void main(String[] args){
        Dog trevor=new Dog("Trevor","Corgi",12);
        String name=trevor.getName();
        String breed=trevor.getBreed();
        int age=trevor.getAge();
        System.out.println(name);
        System.out.println(breed);
        System.out.println(age);
        trevor.bark();
        trevor.eatBiscuit();
        trevor.getOlder();

    }

}
