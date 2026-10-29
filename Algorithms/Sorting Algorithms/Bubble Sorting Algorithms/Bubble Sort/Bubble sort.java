/**
 * Bubble Sort
 * An algorithm that compares the item next to it until the list is sorted.
*/
import java.util.Arrays;

public class BubbleSort {
	public static void sort(int[] sorting_list) {
        /**
         * Sorts inputted list using the bubble sort algorithm.
         * Parameter:
         *      sorting_list(list): An unsorted list of items that needs to be sorted.
         */
		for (int end = sorting_list.length - 1; end > 0; end--) {//loops decreasing end to reduce list size
			boolean swapped = false;
			for (int i = 0; i < end; i++) {//traverse list up to end amount
				if (sorting_list[i] > sorting_list[i + 1]) {//swap if bigger
					int temporary = sorting_list[i];
					sorting_list[i] = sorting_list[i + 1];
					sorting_list[i + 1] = temporary;
					swapped = true;
				}
			}
			if (!swapped) {
				break;
			}
		}
	}
    public static void decrease_sort(int[] sorting_list) {
        /**
         * Sorts in decreasing order inputted list using the bubble sort algorithm.
         * Parameters:
         *      sorting_list(list): An unsorted list of items that needs to be sorted.
         */
		for (int end = sorting_list.length - 1; end > 0; end--) {//loops decreasing end to reduce list size
			boolean swapped = false;
			for (int i = 0; i < end; i++) {//traverse list up to end amount
				if (sorting_list[i] < sorting_list[i + 1]) {//swap if smaller
					int temporary = sorting_list[i];
					sorting_list[i] = sorting_list[i + 1];
					sorting_list[i + 1] = temporary;
					swapped = true;
				}
			}
			if (!swapped) {
				break;
			}
		}
	}
}
