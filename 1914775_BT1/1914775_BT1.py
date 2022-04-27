from os import system
from pip import main
from graph import Graph

from vertex import Vertex

g = Graph()

def graph(g):
    """ Function to print a graph as adjacency list and adjacency matrix. """
    return str(g.adjacencyList()) + '\n' + '\n' + str(g.adjacencyMatrix())

def themDinh():
    print('Vui lòng nhập số đỉnh:')
    n = int(input())
    for item in range(n):
        print('Nhập giá trị của đỉnh thứ ' + str(item+1) + '\n')
        val = input()
        vertex = Vertex(val)
        g.add_vertices([vertex])
    print('Thêm đỉnh thành công, danh sách các đỉnh: ')    
    print(graph(g))
    
def themCanh():
    print('Vui lòng chọn đỉnh cần thêm cạnh')
    print(g.vertices.keys())
    vertex = Vertex(input())
    vertexb = Vertex(input('Vui lòng nhập đỉnh cần nối: '))
    weight = int(input('Vui lòng nhập trọng số của đỉnh: '))
    g.add_edge(vertex, vertexb, weight)
    print('Thêm cạnh thành công!')
    print(vertex.neighbors)
    print(g.adjacencyList())
    
def findWeigtMin():
    for vertex in g.vertices:
        print(vertex)
        
# a = Vertex('A')
# b = Vertex('B')
# c = Vertex('C')
# d = Vertex('D')
# e = Vertex('E')

# a.add_neighbors([b,c,e])
# b.add_neighbors([a,c])
# c.add_neighbors([b,d,a,e])
# d.add_neighbor(c)
# e.add_neighbors([a,c])


# g = Graph()
# print(graph(g))
# print("\n")
# g.add_vertices([a,b,c,d,e])
# g.add_edge(b,d)
# print("\n")
# print(graph(g))
while True:
    print('Chọn chức năng muốn thực hiện: ')
    print('Nhập 1: Thêm đỉnh')
    print('Nhập 2: Thêm cạnh')
    print('Nhập 3: Tìm cạnh có trọng số nhỏ nhất')
    print('Nhập 4: Thiết lập lại trạng thái visited của các đỉnh trên đồ thị')
    print('Nhập 5: Kiểm tra 2 đỉnh có kề nhau hay không')
    print('Nhập 6: Đọc đô thị từ file')
    print('Nhập 7: Duyệt đồ thị theo chiều rộng')
    print('Nhập 0: Thoát chương trình')
    try:
        action = int(input())
        if action == 0:
            break
        elif type(action) != int:
            print('XIN MỜI NHẬP LẠI')
            action = int(input())
            system("CLS")
            print('Chọn chức năng muốn thực hiện: ')
            print('Nhập 1: Thêm đỉnh')
            print('Nhập 2: Thêm cạnh')
            print('Nhập 3: Tìm cạnh có trọng số nhỏ nhất')
            print('Nhập 4: Thiết lập lại trạng thái visited của các đỉnh trên đồ thị')
            print('Nhập 5: Kiểm tra 2 đỉnh có kề nhau hay không')
            print('Nhập 6: Đọc đô thị từ file')
            print('Nhập 7: Duyệt đồ thị theo chiều rộng')
            print('Nhập 0: Thoát chương trình')
    except:
        print('CHÚNG TÔI HIỆN CHƯA PHÁT TRIỂN TÍNH NĂNG ĐÓ, XIN MỜI NHẬP LẠI')
        action = 0

    match action:
        case 1:
            system("CLS")
            print('===========================')
            print("THÊM ĐỈNH")
            print('===========================')
            themDinh()
            print('===========================')

        case 2:
            system("CLS")
            print('===========================')
            print("THÊM CẠNH")
            print('===========================')
            themCanh()
            print('===========================')

        case 3:
            system("CLS")
            print('===========================')
            print("TÌM CẠNH CÓ TRỌNG SỐ NHỎ NHẤT")
            print('===========================')
            findWeigtMin()
            print('===========================')

        case 4:
            system("CLS")
            print('===========================')
            print("Thiết lập lại trạng thái visited của các đỉnh trên đồ thị")
            print('===========================')
            print('===========================')

        case 5:
            system("CLS")
            print('===========================')
            print("Kiểm tra 2 đỉnh có kề nhau hay không")
            print('===========================')
            print('===========================')

        case 6:
            system("CLS")
            print('===========================')
            print("Đọc đô thị từ file")
            print('===========================')
            print('===========================')
        case 7:
            system("CLS")
            print('===========================')
            print("Duyệt đồ thị theo chiều rộng")
            print('===========================')
            print('===========================')
