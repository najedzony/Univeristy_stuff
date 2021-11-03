class MergeSort implements Runnable {
    protected int arr[];
    protected static int głodny[];
    protected int l, r;

    MergeSort(int arr[], int l, int r) {
        this.arr = arr;
        this.l = l;
        this.r = r;
    }

    protected static void initialize(int length){
        głodny = new int[length];
    }

    private void merge(int l, int m, int r) {

        for (int i = l; i <= r; i++) {
            głodny[i] = arr[i];
        }

        int i = l, j = m + 1;
        int k = l;
        while (i <= m && j <= r) {
            if (głodny[i] <= głodny[j]) {
                arr[k] = głodny[i];
                i += 1;
            } else {
                arr[k] = głodny[j];
                j += 1;
            }
            k += 1;
        }
        while (i <= m) {
            arr[k] = głodny[i];
            k += 1;
            i += 1;
        }
        while (j <= r) {
            arr[k] = głodny[j];
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
        if (this.l < this.r) {
            int m = (this.l + this.r) / 2;
            MergeSort left = new MergeSort(arr, this.l, m);
            MergeSort right = new MergeSort(arr, m + 1, this.r);
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
            this.merge(this.l, m, this.r);
        }
    }
}


public class zad_1 {

    public static void main(String[] args) {
        int arr[] = {4, 3, 2, 1};
        MergeSort mergeSort = new MergeSort(arr, 0, 3);
        MergeSort.initialize(arr.length);

        Thread t = new Thread(mergeSort);

        t.start();
        try {
            t.join();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        for (int i = 0; i < 4; i++)
            System.out.printf("%d ", arr[i]);


    }
}