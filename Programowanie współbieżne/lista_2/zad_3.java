class MergeSort implements Runnable {
    protected int arr[];
    protected static int arr_pom[];
    protected int l, r;
    protected static final int N = 2;
    protected static int threadsCounter = 1;
    protected static final int MAX_THREADS = 3;

    MergeSort(int arr[], int l, int r) {
        this.arr = arr;
        this.l = l;
        this.r = r;
    }

    protected static void initialize(int length) {
        arr_pom = new int[length];
    }

    private void merge(int l, int m, int r) {

        for (int i = l; i <= r; i++) {
            arr_pom[i] = arr[i];
        }

        int i = l, j = m + 1;
        int k = l;
        while (i <= m && j <= r) {
            if (arr_pom[i] <= arr_pom[j]) {
                arr[k] = arr_pom[i];
                i += 1;
            } else {
                arr[k] = arr_pom[j];
                j += 1;
            }
            k += 1;
        }
        while (i <= m) {
            arr[k] = arr_pom[i];
            k += 1;
            i += 1;
        }
        while (j <= r) {
            arr[k] = arr_pom[j];
            k += 1;
            j += 1;
        }
    }

    public void sort(int l, int r) {
        if (l < r) {
            int m = (l + r) / 2;
            sort(l, m);
            sort(m + 1, r);
            merge(l, m, r);
        }
    }

    @Override
    public void run() {
        boolean parallel = false;
        synchronized (MergeSort.class) {
            if (threadsCounter < MAX_THREADS) {
                threadsCounter++;
                parallel = true;
            }
        }

        if (r - l + 1 > N && parallel) {
            int m = (this.l + this.r) / 2;
            MergeSort left = new MergeSort(arr, this.l, m);
            MergeSort right = new MergeSort(arr, m + 1, this.r);
            Thread t1 = new Thread(left);
            t1.start();
            right.run();
            try {
                t1.join();
                synchronized (MergeSort.class) {
                    threadsCounter--;
                }
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            this.merge(this.l, m, this.r);
        } else {
            sort(l, r);
        }
    }
}


public class zad_3 {

    public static void main(String[] args) {
        int arr[] = {4, 3, 2, 1,4523,4123,7,342,6736,8,23,1,245,7,23,67,23,6,8,23,2345,57,457,235,235,6};
        MergeSort mergeSort = new MergeSort(arr, 0, arr.length-1);
        MergeSort.initialize(arr.length);

        Thread t = new Thread(mergeSort);

        t.start();
        try {
            t.join();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        for (int i = 0; i < arr.length; i++)
            System.out.printf("%d ", arr[i]);


    }
}