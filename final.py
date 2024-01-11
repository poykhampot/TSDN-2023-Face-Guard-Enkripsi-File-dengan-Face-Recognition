from tkinter import *
import tkinter as tk
from tkinter import filedialog
from tkinter_webcam import webcam
import subprocess



# Inisialisasi Tkinter
root = tk.Tk()
root.title("home")
root.geometry("940x671")

# Image yang akan digunakan
b_home = tk.PhotoImage(file="img/b_home.png")
b_lock = tk.PhotoImage(file="img/b_lock.png")
b_unlock = tk.PhotoImage(file="img/b_unlock.png")
b_kembali1 = tk.PhotoImage(file="img/Polygon 1.png")
b_kembali2 = tk.PhotoImage(file="img/Polygon 2.png")
btn_home1 =tk.PhotoImage(file="img/btn_encrypt.png")
btn_home2 =tk.PhotoImage(file="img/btn_decrypt.png")
btn_choose = tk.PhotoImage(file="img/t_CHOOSE FILE.png")
btn_lock = tk.PhotoImage(file="img/btn_encrypt_2.png")
btn_unlock = tk.PhotoImage(file="img/btn_decrypt_2.png")
btn_exit1 = tk.PhotoImage(file="img/btn_exit.png")


#Fungsi Search File
def search_file():
    global file_path
    file_path = filedialog.askopenfilename(title="Pilih File")
    if file_path:
        # Lakukan sesuatu dengan file_path, seperti membaca isi file
        print("File yang dipilih:", file_path)

#Fungsi Encrypt
def run_encrypt():
    subprocess.run(["python", "main.py", "-f", file_path, "-m","encrypt" ])
    tk.messagebox.showinfo("Message", "Selamat file anda telah berhasi di encrpyt" + file_path)

#Fungsi Decrypt     
def run_decrypt():
    subprocess.run(["python", "main.py", "-f", file_path, "-m","decrypt" ])
    #window = tk.Tk()  # Sets up GUI
    #window.title("Example")  # Titles GUI
    #window.geometry("1000x1000")  # Sizes GUI
    #video = webcam.Box(window, width=450, height=450)
    #video.show_frames()
    tk.messagebox.showinfo("Message", "Selamat file anda berhasil di decrypt")

#Fungsi LockFile
def lockfile():
    root.withdraw()
    global lock_window
    lock_window = tk.Toplevel(root)
    lock_window.title("LOCK FILE")
    lock_window.geometry("940x671")
    background_label_utama = tk.Label(lock_window, image=b_lock)
    background_label_utama.place(x=0, y=0, relwidth=1, relheight=1)
    
    button_lock = tk.Button(lock_window,image=btn_choose,bg="white",activebackground='white',border=0,command=search_file)
    button_lock.pack()
    button_lock.place(x=550,y=250)

    button_lock = tk.Button(lock_window,image=btn_lock,bg="white",activebackground='white',border=0,command=run_encrypt)
    button_lock.pack()
    button_lock.place(x=550,y=350)

    tombol_kembali1 = tk.Button(lock_window, image=b_kembali1,bg="white",activebackground='white',border=0,command=kembali_kemain1)
    tombol_kembali1.pack()
    tombol_kembali1.place(x=20, y=20)



#Fungsi UnLockFile
def unlockfile():
    root.withdraw()
    global unlock_window
    unlock_window = tk.Toplevel(root)
    unlock_window.title("UNLOCK FILE")
    unlock_window.geometry("940x671")
    background_label_utama = tk.Label(unlock_window, image=b_unlock)
    background_label_utama.place(x=0, y=0, relwidth=1, relheight=1)
    
    button_unlock = tk.Button(unlock_window,image=btn_choose,bg="white",activebackground='white',border=0,command=search_file)
    button_unlock.pack()
    button_unlock.place(x=580,y=250)

    button_unlock = tk.Button(unlock_window,image=btn_unlock,bg="white",activebackground='white',border=0,command=run_decrypt)
    button_unlock.pack()
    button_unlock.place(x=580,y=350)

    tombol_kembali2 = tk.Button(unlock_window, image=b_kembali2,bg="#4DA0B4",activebackground='#4DA0B4',border=0,command=kembali_kemain2)
    tombol_kembali2.pack()
    tombol_kembali2.place(x=20, y=20)

# Fungsi Kembali ke Window Utama
def kembali_kemain1():
    root.deiconify()
    lock_window.destroy()
    if kembali_kemain2:
        tombol_unlock = tk.Button(root, image=btn_exit1,bg="#4DA0B4",activebackground='#4DA0B4',border=0, command=root.destroy)
        tombol_unlock.pack()
        tombol_unlock.place(x=650,y=600)

# Fungsi Kembali ke Window Utama
def kembali_kemain2():
    root.deiconify()
    unlock_window.destroy()
    if kembali_kemain2:
        tombol_unlock = tk.Button(root, image=btn_exit1,bg="#4DA0B4",activebackground='#4DA0B4',border=0, command=root.destroy)
        tombol_unlock.pack()
        tombol_unlock.place(x=650,y=600)


# Tambahkan gambar latar belakang pada jendela utama
background_label_utama = tk.Label(root, image=b_home)
background_label_utama.place(x=0, y=0, relwidth=1, relheight=1)

# Tombol untuk membuka jendela baru
tombol_lock = tk.Button(root, image=btn_home1,bg="#4DA0B4",activebackground='#4DA0B4',border=0, command=lockfile)
tombol_lock.pack()
tombol_lock.place(x=550,y=250)

# Tombol untuk membuka jendela baru
tombol_unlock = tk.Button(root, image=btn_home2,bg="#4DA0B4",activebackground='#4DA0B4',border=0, command=unlockfile)
tombol_unlock.pack()
tombol_unlock.place(x=550,y=350)




# Jalankan aplikasi
root.mainloop()
