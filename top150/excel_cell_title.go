func convertToTitle(columnNumber int) string {
    var result string
    for columnNumber > 0 {
        columnNumber--
        result = string('A' + columnNumber % 26) + result
        columnNumber /= 26
    }
    return result
}

/* Recursive
func convertToTitle(columnNumber int) string {
    if columnNumber == 0 {
        return ""
    }
    columnNumber--
    return convertToTitle(columnNumber/26) + string('A' + columnNumber % 26)
}
*/