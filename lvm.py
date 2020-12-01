import os 
import subprocess
while True:
        os.system('cls')
        os.system('tput setaf 7')
        print("")
        print("\t\t\t\t LOGICAL VOLUME MANAGEMENT MENU")
        print("\t\t\t\t********************************")
        os.system("tput setaf 4")
        print("""
                PRESS 1:TO CHECK TOTAL DISK
                PRESS 2:TO CREATE PHYSICAL VOLUME
                PRESS 3:TO DISPLAY PHYSICAL VOLUME
                PRESS 4:TO CREATE VOLUME GROUP
                PRESS 5:TO DISPLAY VOLUME GROUP
                PRESS 6:TO CREATE LOGICAL VOLUME
                PRESS 7:TO DISPLAY LOGICAL VOLUME
                PRESS 8:TO EXTEND SIZE OF LOGICAL VOLUME
                PRESS 9:TO FORMAT THE PARTITION
                PRESS 10:TO ATTACH ONE MORE HARD DISK
                PRESS 11:TO RETURN TO MAIN MENU
                PRESS 12:TO EXIT
                """)
        choice= input("Enter your choice:")
        if choice=="1":
                os.system("fdisk -l")
                input=("Enter to continue..........")
        elif choice=="2":
                hd1=input("Enter your hard disk 1 name: ")
                hd2=input("Enter your hard disk 2 name: ")
                os.system("pvcreate {}".format(hd1))
                os.system("pvcreate {}".format(hd2))
                input=("Enter to continue..........")
        elif choice=="3":
                pv=input("Enter the name of the volume group: ")
                os.system("pvdisplay {}".format(pv))
                input=("Enter to continue..........")
        elif choice=="4":
                vg=input("Enter the name of the volume group: ")
                epv=input("Enter your physical volume that you have created: ")
                os.system("vgcreate {} {}".format(vg,epv))
                input=("Enter to continue..........")
        elif choice=="5":
                vgd=input("Enter the name of the volume group: ")
                os.system("vgdisplay {}".format(vgd))
                input=("Enter to continue..........")
        elif choice=="6":
                vg=input("Enter the name of the volume group: ")
                size=input("Enter the size of your logical volume: ")
                lv=input("Enter the name of the logical group: ")
                os.system("lvcreate --size {} --name {} {}".format(size,lv,vg))
                input=("Enter to continue..........")
        elif choice=="7":
                os.system("lvdisplay")
                input=("Enter to continue..........")
        elif choice=="8":
                vg1=input("Enter the name of the volume group: ")
                lv1=input("Enter the name of the logical volume group: ")
                os.system("mkfs.ext4 /dev/{}/{}".format(vg1,lv1))
                print("\n\n !!NOW WE WILL CREATE A DIRECTORY!!")
                dir=input("Enter the name of the drive you want to create:")
                os.system("mkdir /{}".format(dir))
                print("\nSUCCESSFULLY FORMATTED!!")
                esize=input("\nEnter the size you want to extend: ")
                lve=input("Enter the name of logical volume group : ")
                vge=input("Enter the name of the volume group: ")
                os.system("lvextend --size {} /dev/{}/{}".format(esize,vge,lve))
                print("\n\t\t\t\tEXTENTED SUCCESSFULLY!!\n")
                input=("Enter to continue..........")
        elif choice=="9":
                vg1=input("Enter the name of the volume group: ")
                lve=input("Enter the name of logical volume group : ")
                os.system("resize2fs /dev/{}/{}".format(vg1,lve))
                input=("Enter to continue..........")
        elif choice=="10":
                hd=input("Enter the name of the hard disk: ")
                vg=input("Enter the name of the volume group: ")
                os.system("vgextend {} /dev/{}".format(vg,hd))
                input=("Enter to continue..........")
		
        elif choice=="11":
                break
        else:
                print("Wrong choice!!")
                input("Enter to continue...........")
			


		