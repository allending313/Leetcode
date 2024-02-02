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

func postorderTraversal(root *TreeNode) []int {
    r := Res{}
    r.traversal(root)
    return r.Res
}

func (r *Res) traversal(node *TreeNode) {
    if node != nil {
        r.traversal(node.Left)
        r.traversal(node.Right)
        r.Res = append(r.Res, node.Val)
    }
}
*/

// Iterative via stack
func postorderTraversal(root *TreeNode) []int {
    stack := []*TreeNode{root}
    postorder := []int{}
    for len(stack) != 0 {
        node := stack[len(stack)-1]
        stack = stack[:len(stack)-1]
        if node == nil {
            continue
        }
        postorder = append([]int{node.Val}, postorder...)
        stack = append(stack, node.Left)
        stack = append(stack, node.Right)
    }
    return postorder
}
