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
    public List<List<Integer>> levelOrder(TreeNode root) {
       List<List<Integer>> list=new ArrayList<>();
       if (root == null) return list;
       Queue<TreeNode> q=new LinkedList<>();
        q.add(root);
        while(!q.isEmpty()) {
             int n=q.size();
             List<Integer> temp=new ArrayList();
             for(int i=0;i<n;i++) {
                TreeNode x=q.remove();
                temp.add(x.val);
                if(x.left!=null) {
                    q.add(x.left);
                }
                if(x.right!=null) {
                    q.add(x.right);
                }
             }
             list.add(temp);
        }  
       return list;
    }
}