import java.util.Arrays;

public class CocktailShakerSort {
	public static void sort(int[] array) {
		/**
         * Sorts inputted list using the cocktail shaker sort algorithm.
         * Parameters:
         *     array(list): An unsorted list of items that needs to be sorted.
         */
        if (array == null || array.length < 2) {
			return;
		}

		int left = 0;
		int right = array.length - 1;

		while (left < right) {
			boolean swapped = false;

			for (int i = left; i < right; i++) {
				if (array[i] > array[i + 1]) {
					swap(array, i, i + 1);
					swapped = true;
				}
			}
			right--;
			if (!swapped) {
				break;
			}

			swapped = false;
			for (int i = right; i > left; i--) {
				if (array[i - 1] > array[i]) {
					swap(array, i - 1, i);
					swapped = true;
				}
			}
			left++;
			if (!swapped) {
				break;
			}
		}
	}

	private static void swap(int[] array, int first, int second) {
		/**
         * Swaps two elements in an array.
         * Parameters:
         *     array(list): The array containing the elements to be swapped.
         *     first(int): The index of the first element to be swapped.
         *     second(int): The index of the second element to be swapped.
         */
        int temporary = array[first];
		array[first] = array[second];
		array[second] = temporary;
	}
}
