/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

 /* Recursive
type Res struct {
	Res []int
}

func preorderTraversal(root *TreeNode) []int {
	r := Res{}
	r.traversal(root)
	return r.Res
}

func (r *Res) traversal(node *TreeNode) {
	if node != nil {
		r.Res = append(r.Res, node.Val)
		r.traversal(node.Left)
		r.traversal(node.Right)
	}
}
*/

// Iterative via Stack
func preorderTraversal(root *TreeNode) []int {
    stack := []*TreeNode{root}
    preorder := []int{}
    for len(stack) != 0 {
        node := stack[len(stack)-1]
        stack = stack[:len(stack)-1]
        if node == nil {
            continue
        }
        preorder = append(preorder, node.Val)
        stack = append(stack, node.Right)
        stack = append(stack, node.Left)
    }
    return preorder
}