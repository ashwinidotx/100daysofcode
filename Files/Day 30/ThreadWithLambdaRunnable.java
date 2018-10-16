
public class ThreadWithLambdaRunnable {

    public static void main(String[] args) {
        Runnable first = new Runnable() {
            @Override
            public void run() {
                for (int i = 0; i < 5; i++) {
                    System.out.println("Value = " + i);
                    try {
                        Thread.sleep(500);
                    } catch (Exception e) {
                        System.out.println(e);
                    }
                }
            } // end of run
        }; // end of first

        Runnable second = () -> {
            for (int i = 0; i < 5; i++) {
                System.out.println("Remaining Value = " + (5 - i));
                try {
                    Thread.sleep(500);
                } catch (Exception e) {
                    System.out.println(e);
                }
            }
        } // end of run
        ; // end of second

        Thread t1 = new Thread(first);
        Thread t2 = new Thread(second);

        t1.start();
        try {
            Thread.sleep(100);
        } catch (Exception e) {
            System.out.println(e);
        }
        t2.start();

    } // End of Main
} // End of ThreadWithLambdaRunnable Class
