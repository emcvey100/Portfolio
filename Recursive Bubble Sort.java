class RecursiveBubbleSort {
	public static void sort(int[] values) {
        /**
         * Sorts the input array using the recursive bubble sort algorithm.
         * Parameters:
         *     values(int[]): The array to be sorted.
         */
		if (values == null || values.length < 2) {
			return;
		}
		sort(values, values.length);
	}

	private static void sort(int[] values, int length) {
        /**
         * Recursively sorts the input array using the bubble sort algorithm.
         * Parameters:
         *     values(int[]): The array to be sorted.
         *     length(int): The length of the array to be sorted.
         */
		if (length < 2) {
			return;
		}

		boolean swapped = false;
		for (int i = 0; i < length - 1; i++) {
			if (values[i] > values[i + 1]) {
				int temp = values[i];
				values[i] = values[i + 1];
				values[i + 1] = temp;
				swapped = true;
			}
		}

		if (swapped) {
			sort(values, length - 1);
		}
	}
}
