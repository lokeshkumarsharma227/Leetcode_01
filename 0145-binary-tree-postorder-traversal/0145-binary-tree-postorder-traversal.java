/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public List<Integer> postorderTraversal(TreeNode root) {
        ArrayList<Integer> list=new ArrayList<>();
        solve(root,list);
        return list;
    }
    void solve(TreeNode root,ArrayList<Integer> list) {
        if(root==null) return;
        solve(root.left,list);
        solve(root.right,list);
        list.add(root.val);
    }
}