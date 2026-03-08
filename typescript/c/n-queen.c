#include <stdlib.h>
#include <string.h>

void backtrack(int row, int n, char **board,
               int *cols, int *diag1, int *diag2,
               char ****result, int *returnSize, int **returnColumnSizes) {

    if (row == n) {
        (*result)[*returnSize] = (char **)malloc(n * sizeof(char *));
        (*returnColumnSizes)[*returnSize] = n;

        for (int i = 0; i < n; i++) {
            (*result)[*returnSize][i] = strdup(board[i]);
        }

        (*returnSize)++;
        return;
    }

    for (int col = 0; col < n; col++) {

        if (cols[col] || diag1[row - col + n] || diag2[row + col])
            continue;

        board[row][col] = 'Q';
        cols[col] = 1;
        diag1[row - col + n] = 1;
        diag2[row + col] = 1;

        backtrack(row + 1, n, board, cols, diag1, diag2,
                  result, returnSize, returnColumnSizes);

        board[row][col] = '.';
        cols[col] = 0;
        diag1[row - col + n] = 0;
        diag2[row + col] = 0;
    }
}

char *** solveNQueens(int n, int* returnSize, int** returnColumnSizes) {

    *returnSize = 0;
    char ***result = malloc(1000 * sizeof(char **));
    *returnColumnSizes = malloc(1000 * sizeof(int));

    char **board = malloc(n * sizeof(char *));
    for (int i = 0; i < n; i++) {
        board[i] = malloc((n + 1) * sizeof(char));
        memset(board[i], '.', n);
        board[i][n] = '\0';
    }

    int *cols = calloc(n, sizeof(int));
    int *diag1 = calloc(2 * n, sizeof(int));
    int *diag2 = calloc(2 * n, sizeof(int));

    backtrack(0, n, board, cols, diag1, diag2,
              &result, returnSize, returnColumnSizes);

    return result;
}
