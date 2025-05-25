print("ET0735 (Devops for AIOT) -Lab2- Introduction to Python")
def display_m_m():
    print("ENter some numbers seperated by commas")

def get_user_input():
    numInp = input("Enter numbers separated by commas: ")  # add prompt
    inpList = numInp.split(",")
    floatList = list(map(float, inpList))  # convert strings to floats
    return floatList
def calc_average_temperature(tempList):
    return sum(tempList) / len(tempList)
def calc_min_max_temperature(tempList):
    est_list = list(map(int, tempList))
    min_max_list = [max(est_list), min(est_list)]
    return min_max_list

def sort():
    print("sort")
def med():
    print("med")