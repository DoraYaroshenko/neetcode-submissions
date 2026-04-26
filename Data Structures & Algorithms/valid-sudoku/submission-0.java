class Solution {
    public boolean isValidSudoku(char[][] board) {
        HashSet<Character> boxSet0 = new HashSet<>();
        HashSet<Character> boxSet1 = new HashSet<>();
        HashSet<Character> boxSet2 = new HashSet<>();
        HashSet [] arrBoxes = {boxSet0, boxSet1, boxSet2};
        for(int i=0;i<9;i++){
            HashSet<Character> rowSet = new HashSet<>();
            for(int j=0;j<9;j++){
                char c = board[i][j];
                int boxNum = j/3;
                if(c!='.'){
                    if(rowSet.contains(c)||arrBoxes[boxNum].contains(c)){
                        return false;
                    }
                    rowSet.add(c);
                    arrBoxes[boxNum].add(c);
                }
            }
            if(i%3==2){
                for(HashSet box:arrBoxes){
                    box.clear();
                }
            }
        }
        for(int i=0;i<9;i++){
            HashSet<Character> colSet = new HashSet<>();
            for(int j=0;j<9;j++){
                char c = board[j][i];
                if(c!='.'){
                    if(colSet.contains(c)){
                        return false;
                    }
                    colSet.add(c);
                }
            }
        }
        return true;
    }
}
