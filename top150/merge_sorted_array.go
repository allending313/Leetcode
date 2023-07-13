func merge(nums1 []int, m int, nums2 []int, n int)  {
    /* sort the union of nums1 + nums2

    nums1 = append(nums1[:n], nums2...)
    sort.Ints(nums1)

    */

    // O(m+n) three pointer solution
    var x, y, xy int
    for x, y, xy = m-1, n-1, m+n-1; x >= 0 && y >= 0; xy-- {
        if nums2[y] >= nums1[x] {
            nums1[xy] = nums2[y]
            y--
        } else {
            nums1[xy] = nums1[x]
            x--
        }
    }

    if y >= 0 {
        copy(nums1[:xy+1], nums2[:y+1])
    }
}