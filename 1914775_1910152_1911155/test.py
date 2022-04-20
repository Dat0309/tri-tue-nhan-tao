# '''
# 1. Kiểu dữ liệu cơ bản
# ''' 

# dat = "Dat dep trai"

# so = 12

# '''
# Khi muốn chỉ định kiểu dữ liệu:
#     TenBien = kieuDuLieu(giaTri)
#     str,
#     int, float, complex,
#     bool,...
#     bytes,...
# '''

# dat = str("Dat dep trai")
# so = int(20)

# print(dat)
# print(type(dat))
# print(so)
# print(type(so))


'''
 Cấu trúc điều khiển
    if else
    for
    while
    match: - case:
'''


from os import system

listStudents = []

# Ham them Sinh vien
def addStudent():
    ''' Them sinh vien '''
    print('THEM SINH VIEN')
    infor ={
        'id' : '',
        'name' :''
    }
    
    # Nhap ID
    print('Nhập ID sinh viên: ')
    id = input()
    
    while True:
        student = findStudent(id)
        if student != False:
            print('Sinh vien da ton tai trong danh sach, vui long nhap lai: ')
            id = input()
        else:
            break
        
    infor['id'] = id
    
    # Nhap Ten
    print('Nhập tên sinh viên: ')
    infor['name'] = input()
    
    listStudents.append(infor)
    
        
def findStudent(id):
    for i in range(0, len(listStudents)):
        if listStudents[i]['id'] == id:
            return [i, listStudents[i]]
    return False

def sortStudent(key):
    match key:
        case 1:
            listStudents.sort( key = lambda a:a['name'])
            showStudent()
        case 2:
            listStudents.sort(key= lambda a:a['name'],reverse=True)
            showStudent()

def deleteStudent():
    ''' Ham xoa sinh vien '''
    print('XOÁ SINH VIÊN')
    print('Nhập id sinh viên cần xoá: ')
    id = input()
    
    student = findStudent(id)
    if student:
        listStudents.remove(student[1])
        print('XOÁ SINH VIÊN THÀNH CÔNG!!')
    else:
        print('KHÔNG TÌM THẤY SINH VIÊN')
        
def showStudent():
    '''Ham hien thi dssv'''
    print('DANH SÁCH SINH VIÊN')
    for i in range(0, len(listStudents)):
        print("MÃ SV: ", listStudents[i]['id'], "TÊN SV: ",listStudents[i]['name'])
        
def editStudent():
    '''Ham sua sinh vien'''
    print('SỬA THÔNG TIN SINH VIÊN')
    print('Nhập thông tin sinh viên cần sửa: ')
    id = input()
    student = findStudent(id)
    
    if student:
        print('Nhập tên sinh viên')
        name = input()
        student[1]['name'] = name
        listStudents[student[0]] = student[1]
    else:
        print('Không tìm thấy SINH VIÊN', id)

while True:
    print('Chọn chức năng muốn thực hiện: ')
    print('Nhập 1: Thêm Sinh viên')
    print('Nhập 2: Xoá Sinh viên')
    print('Nhập 3: Sửa Sinh viên')
    print('Nhập 4: Xem danh sách Sinh viên')
    print('Nhập 5: Sắp xếp danh sách Sinh viên tăng dần')
    print('Nhập 6: Sắp xếp danh sách Sinh viên giảm dần')
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
            print('Nhập 1: Thêm Sinh viên')
            print('Nhập 2: Xoá Sinh viên')
            print('Nhập 3: Sửa Sinh viên')
            print('Nhập 4: Xem danh sách Sinh viên')
            print('Nhập 5: Sắp xếp danh sách Sinh viên tăng dần')
            print('Nhập 6: Sắp xếp danh sách Sinh viên giảm dần')
            print('Nhập 0: Thoát chương trình')
    except:
        print('CHÚNG TÔI HIỆN CHƯA PHÁT TRIỂN TÍNH NĂNG ĐÓ, XIN MỜI NHẬP LẠI')
        action = 0
    
    match action:
        case 1: 
            system("CLS")
            print('===========================')
            print("THEM SINH VIEN")
            print('===========================')
            addStudent()
            print('===========================')
            
        case 2:
            system("CLS")
            print('===========================')
            print("XOA SINH VIEN")
            print('===========================')
            deleteStudent()
            print('===========================')
            
        case 3:
            system("CLS")
            print('===========================')
            print("CHINH SUA SINH VIEN")
            print('===========================')
            editStudent()
            print('===========================')
            
        case 4:
            system("CLS")
            print('===========================')
            print("XUAT SINH VIEN")
            print('===========================')
            showStudent()
            print('===========================')
        
        case 5:
            system("CLS")
            print('===========================')
            print("SAP XEP DANH SACH TANG")
            print('===========================')
            sortStudent(1)
            print('===========================')
            
        case 6:
            system("CLS")
            print('===========================')
            print("SAP XEP DANH SACH GIAM")
            print('===========================')
            sortStudent(2)
            print('===========================')
            
        
    
        