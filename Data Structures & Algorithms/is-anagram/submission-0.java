class Solution {
    public boolean isAnagram(String s, String t) {
        Map<Character,Integer> map = new HashMap<>();
        for(int i = 0; i<s.length();i++){
            if(map.containsKey(s.charAt(i))){
                map.replace(s.charAt(i),map.get(s.charAt(i))+1);
            } else {
                map.put(s.charAt(i),1);
            }
        }
        for(int i = 0; i<t.length();i++){
            if(map.containsKey(t.charAt(i))){
                map.replace(t.charAt(i),map.get(t.charAt(i))-1);
            } else {
                return false;
            }
        }
        for (Integer i: map.values()){
            if (i!= 0) return false;
        }
        return true;
    }
}
