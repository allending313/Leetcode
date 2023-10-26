type RandomizedSet struct {
    store map[int]int
    indexes []int
}


func Constructor() RandomizedSet {
    return RandomizedSet{store: make(map[int]int), indexes: make([]int, 0)}
}


func (this *RandomizedSet) Insert(val int) bool {
    if _, ok := this.store[val]; ok {
        return false
    }
    this.store[val] = len(this.indexes)
    this.indexes = append(this.indexes, val)
    return true
}


func (this *RandomizedSet) Remove(val int) bool {
    itemIndex, ok := this.store[val]
    if !ok {
        return false
    }
    lastIndex := len(this.indexes) -1
    lastElem := this.indexes[lastIndex]
    this.indexes[itemIndex] = lastElem
    this.store[lastElem] = itemIndex
    this.indexes = this.indexes[:len(this.indexes)-1]
    delete(this.store, val)
    return true
}

func (this *RandomizedSet) GetRandom() int {
    return this.indexes[rand.Intn(len(this.indexes))]
}