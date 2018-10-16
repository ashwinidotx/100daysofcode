class counter {
    int count;

    public synchronized void count() {
        count++;
    }
}

public class ThreadSyn {

    public static void main(String[] args) throws Exception {

        counter c = new counter();
        Thread t1 = new Thread(new Runnable() {
            @Override
            public void run() {
                for (int i = 0; i < 100; i++)
                    c.count();
            }
        });

        Thread t2 = new Thread(new Runnable() {

            @Override
            public void run() {
                for (int i = 0; i < 150; i++)
                    c.count();
            }
        });

        t1.start();
        t2.start();
        t1.join();
        t2.join();
        System.out.println(c.count);

    } // end of main
} // end of ThreadSyn
