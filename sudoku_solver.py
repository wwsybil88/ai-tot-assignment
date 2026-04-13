import numpy as np

class SudokuToT:
    def __init__(self, board):
        self.board = np.array(board)

    def is_valid(self, r, c, k):
        """
        ToT 评估器：判断在 (r, c) 填入 k 是否符合数独规则（局部评估）
        """
        # 检查行
        if k in self.board[r, :]: return False
        # 检查列
        if k in self.board[:, c]: return False
        # 检查 3x3 宫格
        start_r, start_c = 3 * (r // 3), 3 * (c // 3)
        if k in self.board[start_r:start_r+3, start_c:start_c+3]: return False
        return True

    def solve(self):
        """
        ToT 核心：搜索思维树
        """
        for r in range(9):
            for c in range(9):
                if self.board[r, c] == 0:  # 找到一个未填写的“思维节点”
                    for k in range(1, 10):  # 探索 9 个可能的分支
                        if self.is_valid(r, c, k):
                            self.board[r, c] = k  # 尝试走这条路径
                            
                            # 继续向下探索思维树
                            if self.solve():
                                return True
                            
                            # 如果下游路径（思维分支）死掉，则回溯（剪枝）
                            self.board[r, c] = 0
                    return False  # 所有分支都不可行
        return True

# 根据你上传的图片录入的数据（0代表空格）
initial_board = [
    [1, 0, 0, 0, 0, 0, 9, 0, 0],
    [0, 6, 9, 0, 8, 1, 3, 4, 5],
    [0, 3, 0, 0, 5, 0, 0, 0, 6],
    [8, 0, 0, 1, 4, 0, 0, 0, 7],
    [7, 1, 0, 6, 0, 8, 5, 0, 0],
    [0, 0, 0, 0, 0, 5, 0, 0, 0],
    [0, 8, 0, 0, 0, 0, 0, 0, 0],
    [0, 9, 1, 8, 0, 7, 0, 5, 0],
    [3, 0, 7, 0, 0, 6, 8, 0, 0]
]

solver = SudokuToT(initial_board)
if solver.solve():
    print("成功解出数独：")
    print(solver.board)
else:
    print("无解")
