func setZeroes(matrix [][]int) {
    firstRow, firstCol := false, false
    rows, cols := len(matrix), len(matrix[0])

    for i := 0; i < rows; i++ {
        if matrix[i][0] == 0 {
            firstCol = true
        }
    }

    for j := 0; j < cols; j++ {
        if matrix[0][j] == 0 {
            firstRow = true
        }
    }

    for i := 1; i < rows; i++ {
        for j := 1; j < cols; j++ {
            if matrix[i][j] == 0 {
                matrix[i][0] = 0
                matrix[0][j] = 0
            }
        }
    }

    for i := 1; i < rows; i++ {
        for j := 1; j < cols; j++ {
            if matrix[i][0] == 0 || matrix[0][j] == 0 {
                matrix[i][j] = 0
            }
        }
    }

    if firstRow {
        for j := 0; j < cols; j++ {
            matrix[0][j] = 0
        }
    }

    if firstCol {
        for i := 0; i < rows; i++ {
            matrix[i][0] = 0
        }
    }
}
