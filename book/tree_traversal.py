"""
## 배열로 표현된 이진 트리의 인덱스 규칙
- 루트 노드는 배열의 첫번째 요소
- 인덱스 i에 있는 노드의 왼쪽 자식 노드는 2 * i + 1
- 인덱스 i에 있는 노드의 오른쪽 자식 노드는 2 * i + 2

## 왜 * 2 를 하는가?
이진 트리는 각 노드가 최대 두개의 자식을 가지는 트리
배열로 이진 트리 표현 시 부모와 자식 간의 관계를 명확히 하기 위함
"""


"""
전위 순회
"""


def preorder(nodes, idx):
    # idx 현재 방문 중인 노드의 인덱스
    # idx가 노드 리스트 길이보다 작을 때
    if idx < len(nodes):
        # 루트 드 출력 후
        # 왼쪽 서브 트리와 오른쪽 서브 트리를 재귀 호출해 출력 순서대로 붙이기
        result = str(nodes[idx]) + " "
        result += preorder(nodes, idx * 2 + 1)  # 왼쪽 자식노드
        result += preorder(nodes, idx * 2 + 2)  # 오른쪽 자식노드
        return result
    # idx >= len(nodes) 이면 빈 문자열 반환
    return ""


"""
중위 순회
"""


def inorder(nodes, idx):
    # idx 가 노드 리스트 길이보다 작을 때
    if idx < len(nodes):
        # 왼쪽 서브 트리 먼저 재귀 호출해 출력 순서대로 이어붙이기
        result = inorder(nodes, idx * 2 + 1)
        # 루트 노드 출력한 후, 오른쪽 서브 트리를 재귀 호출해 출력 순서대로 이어 붙이기
        result += str(nodes[idx]) + " "
        result += inorder(nodes, idx * 2 + 2)
        return result
    return ""


"""
후위 순회
"""


def postorder(nodes, idx):
    if idx < len(nodes):
        # 왼쪽 서브 트리와 오른쪽 서브 트리를 재귀 호출해 출력 순서대로 이어 붙이기
        result = postorder(nodes, idx * 2 + 1)
        result += postorder(nodes, idx * 2 + 2)
        # 루트 노드 출력
        result += str(nodes[idx]) + " "
        return result
    return ""


def solution(nodes):
    return [
        preorder(nodes, 0)[:-1],
        inorder(nodes, 0)[:-1],
        postorder(nodes, 0)[:-1]
    ]
