def swapFile():
    file_A = input("Enter The Location Of the First File: ")
    file_B = input("Enter The Location Of The Second File: ")

    open_file_1 = open(file_A,"r")
    data_1 = open_file_1.read()
    open_file_2 = open(file_B,"r")
    data_2 = open_file_1.read()
    
    open_file_1 = open(file_A,"w")
    open_file_2 = open(file_B,"w")
    open_file_1.write(data_2)
    open_file_2.write(data_1)
  

swapFile()
