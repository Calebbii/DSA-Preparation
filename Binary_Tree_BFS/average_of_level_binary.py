from collections import deque

def averageOfLevels(root):
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        level_sum = 0
        level_count = 0
        size = len(queue)

        for _ in range(size):
            node = queue.popleft()
            level_sum += node.val
            level_count += 1

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(level_sum / level_count)

    return result