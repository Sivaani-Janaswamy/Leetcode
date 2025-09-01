class Solution {
    public String reverseVowels(String s) {
        int low = 0;
        int high = s.length() - 1;
        char[] charArray = s.toCharArray();

        while (low < high) {
            if (isVowel(charArray[low]) && isVowel(charArray[high])) {
                char temp = charArray[low];
                charArray[low] = charArray[high];
                charArray[high] = temp;
                low++;
                high--;
            } else if (isVowel(charArray[low])) {
                high--;
            } else {
                low++;
            }
        }

        return new String(charArray);
    }

    static boolean isVowel(char c) {
        return "aeiouAEIOU".indexOf(c) != -1;
    }
}
