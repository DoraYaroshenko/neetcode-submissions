class Solution {
    public boolean isPalindrome(String s) {
        String without_spaces = "";
        for(int i=0;i<s.length();i++){
            if(((s.charAt(i)>=65 && s.charAt(i)<=122) && !(s.charAt(i)<=96&&s.charAt(i)>=91)) || (s.charAt(i)>=48 && s.charAt(i)<=57)){
                without_spaces+=s.charAt(i);
            }
        }
        without_spaces = without_spaces.toLowerCase();
        for(int i=0;i<without_spaces.length()/2;i++){
            if(without_spaces.charAt(i)!=without_spaces.charAt(without_spaces.length()-i-1)){
                return false;
            }
        }
        return true;
    }
}
