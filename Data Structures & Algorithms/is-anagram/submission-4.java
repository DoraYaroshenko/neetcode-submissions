class Solution {
    public boolean isAnagram(String s, String t) {
        Map<Character, Integer> s_map = new HashMap<>();
        for(int i=0;i<s.length();i++){
            int num_of_appearences = s_map.get(s.charAt(i))==null?0:s_map.get(s.charAt(i));
            s_map.put(s.charAt(i),++num_of_appearences);
        }
        Map<Character, Integer> t_map = new HashMap<>();
        for(int i=0;i<t.length();i++){
            int num_of_appearences = t_map.get(t.charAt(i))==null?0:t_map.get(t.charAt(i));
            t_map.put(t.charAt(i),++num_of_appearences);
        }
        return t_map.equals(s_map);
    }
}
