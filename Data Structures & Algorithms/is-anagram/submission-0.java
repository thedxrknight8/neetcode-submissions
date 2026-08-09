class Solution {
    public boolean isAnagram(String s, String t) {
        char[] chars = s.toCharArray();
        char[] chart = t.toCharArray();

        if(chars.length != chart.length) {
            return false;
        }

        Arrays.sort(chars);
        Arrays.sort(chart);

        
        for(int i = 0; i < chars.length; i++) {
            if(chars[i] != chart[i]) {
                return false;
            }
        }

        return true;
    }
}
