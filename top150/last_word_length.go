func lengthOfLastWord(s string) int {
    // words := strings.Split(strings.TrimSpace(s), " ")
    // return len(words[len(words)-1])

    s = strings.TrimRight(s, " ")
    return len(s) - 1 - strings.LastIndex(s, " ")
}