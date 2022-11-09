public class lesson2 {
    public static void main(String[] args) {
        for_loop_yes();
        list_of_cars();
    }

    public static void for_loop_yes() {
        for (int i = 0; i < 5; i++) {
            System.out.println("Yes");
        }
    }

    public static void list_of_cars() {
        String[] cars={"Volvo", "BMW", "Ford", "Mazda"};
        for (int i=0; i<4; i++) {
            System.out.println(cars[i]);

            }

        }
    }

