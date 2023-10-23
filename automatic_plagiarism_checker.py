from difflib import SequenceMatcher
def plagiarism_checker(f1,f2):
    with open(f1,errors="ignore") as file1,open(f2,errors="ignore") as file2:
        f1_data=file1.read()
        f2_data=file2.read()
        res=SequenceMatcher(None, f1_data, f2_data).ratio()
        return res
        

f1=input("Enter file_1 path: ")
f2=input("Enter file_2 path: ")
similarity  = plagiarism_checker(f1, f2)
print(f"These files are {similarity *100} % similar")