public class passengers {

    private int checkedBags, freebags;
    private double perBagFee;

    public int getCheckedBags() {
        return checkedBags;
    }

    public void setCheckedBags(int checkedBags) {
        this.checkedBags = checkedBags;
    }

    public int getFreebags() {
        return freebags;
    }

    public void setFreebags(int freebags) {
        this.freebags = freebags;
    }

    public double getPerBagFree() {
        return perBagFee;
    }

    public void setPerBagFree(double perBagFree) {
        this.perBagFee = perBagFree;
    }

    // CONSTRUCTORS

    public passengers() {
        System.out.println("No Bags Allocated.");
    }

    public passengers(int freebags) {
        this(freebags > 1 ? 0.25d : 0.50d);
        this.freebags = freebags;
    }

    public passengers(int freebags, int checkedbags) {
        this(freebags); // this.freebags=freebags;
        this.checkedBags = checkedbags;
    }
    // Since 2nd and 3rd constructor have some redundancy in them, we
    // chain them to avoid duplicate code.

    private passengers(double perBagFee) {
        this.perBagFee = perBagFee;
    }

}// end of passengers class
