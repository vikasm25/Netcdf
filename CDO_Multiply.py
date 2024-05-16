import os

#Read the Annual Folder Directory and List Annual Folders Directory

out=input("Enter mask name : ") # Enter mask region name to create output folder in Result folder
mask="/home/Desktop/Untitled_Folder/Mask/India.nc"  # change name of mask file here eg. instead if India.nc
# Do not change anything other than the mentioned comment. 

start_dir="/home/Desktop/Untitled_Folder/Input_Dir/"
start=os.listdir(start_dir)

path="/home/Desktop/Untitled_Folder/Result/"
os.system("cd "+path)
os.system("mkdir "+out)

Out_path="/home/Desktop/Untitled_Folder/Result/"+out+"/"
print(Out_path)

for i in range(len(start)):
    input_dir=start_dir+start[i]
    os.system("cdo mul, "+start_dir+start[i]+" "+mask+" "+Out_path+mask[49:-3]+start[i]) 
    #print("cdo mul, "+start_dir+start[i]+" "+mask+" "+Out_path+mask[-13:-4]+start[i])
