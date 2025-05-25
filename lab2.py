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

def calc_median_temperature(tempList):
    tempList.sort()
    n = len(tempList)

    if n % 2 == 1:
        # Odd number of elements → return middle one
        return tempList[n // 2]
    else:
        # Even number of elements → average the two middle ones
        mid1 = tempList[n // 2]
        mid2 = tempList[n // 2 - 1]
        return (mid1 + mid2) / 2
