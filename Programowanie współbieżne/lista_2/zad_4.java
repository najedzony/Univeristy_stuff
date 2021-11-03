
class NSP implements Runnable {
    protected int arr[];
    protected int l, r;
    protected Result result;

    public class Result {
        int leftCount;
        int rightCount;
        int globalCount;
        int leftCountNumber;
        int rightCountNumber;
        int globalCountNumber;
        int length;
    
        public Result(int leftCount, int rightCount, int globalCount, int leftCountNumber, int rightCountNumber, int globalCountNumber, int length) {
            this.leftCount = leftCount;
            this.rightCount = rightCount;
            this.globalCount = globalCount;
            this.leftCountNumber = leftCountNumber;
            this.rightCountNumber = rightCountNumber;
            this.globalCountNumber = globalCountNumber;
            this.length = length;
        }
        public Result(){}
    }
    
    
    
    NSP(int arr[], int l, int r) {
        this.arr = arr;
        this.l = l;
        this.r = r;
    }

    // L= 2224222 R = 222
    //ile na lewo, ile najwiecej, ile na prawo, co na lewo, co na srodku, co na prawo, dlugosc
    protected Result getResult() {
        return result;
    }

    private void merge(NSP nspLeft, NSP nspRight) {
        result = new Result();

        result.leftCount = nspLeft.getResult().leftCount;
        result.rightCount = nspRight.getResult().rightCount;
        result.leftCountNumber = nspLeft.getResult().leftCountNumber;
        result.rightCountNumber = nspRight.getResult().rightCountNumber;
        result.length = nspLeft.getResult().length + nspRight.getResult().length;
        result.globalCount = nspLeft.getResult().globalCount;
        result.globalCountNumber = nspLeft.getResult().globalCountNumber;

        if (nspLeft.getResult().leftCount == nspLeft.getResult().length &&
                nspRight.getResult().leftCountNumber == nspLeft.getResult().leftCountNumber){
            result.leftCount += nspRight.getResult().leftCount;
        }
        if (nspRight.getResult().rightCount == nspRight.getResult().length &&
                nspLeft.getResult().rightCountNumber == nspRight.getResult().rightCountNumber){
            result.rightCount += nspLeft.getResult().rightCount;
        }
        if (result.globalCount < nspRight.getResult().globalCount){
            result.globalCount = nspRight.getResult().globalCount;
            result.globalCountNumber = nspRight.getResult().globalCountNumber;
        }
        if (nspLeft.getResult().rightCountNumber == nspRight.getResult().leftCountNumber &&
            nspLeft.getResult().rightCount + nspRight.getResult().leftCount > result.globalCount){
            result.globalCount = nspLeft.getResult().rightCount + nspRight.getResult().leftCount;
            result.globalCountNumber = nspRight.getResult().leftCountNumber;
        }


    }

    @Override
    public void run() {
        if (this.l < this.r) {
            int m = (this.l + this.r) / 2;
            NSP left = new NSP(arr, this.l, m);
            NSP right = new NSP(arr, m + 1, this.r);
            Thread t1 = new Thread(left);
            Thread t2 = new Thread(right);
            t1.start();
            t2.start();
            try {
                t1.join();
                t2.join();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            this.merge(left, right);
        } else {
            result = new Result(1, 1, 1, arr[this.l], arr[this.l], arr[this.l], 1);
        }
    }
}


public class zad_4 {

    public static void main(String[] args) {
        int arr[] = {4, 3, 2, 1, 1, 1, 4, 2, 7, 7, 7, 7, 12, 45, 7};
        NSP nsp = new NSP(arr, 0, arr.length - 1);

        Thread t = new Thread(nsp);
        t.start();
        try {
            t.join();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        for (int i = 0; i < nsp.result.globalCount; i++){
            System.out.print(nsp.result.globalCountNumber + " ");
        }

    }
}