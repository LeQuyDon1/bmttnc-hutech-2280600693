def dao_nguoc_list(lst):
    return lst[::-1]
input_list = input("Nhập danh sách các số, cách nhau bằng đáu phẩy: ")
numbers = list(map(int, input_list.split(',')))
list_daonguoc = dao_nguoc_list(numbers)
print("List sau khi đảo ngược ", list_daonguoc)