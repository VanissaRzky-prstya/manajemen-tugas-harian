from prettytable import PrettyTable
from datetime import datetime

# Basic Stack buat nyimpen history
class Stack:
    def __init__(self, ukuran=100):
        self.ukuran = ukuran
        self.data = [None] * ukuran
        self.top = -1
    
    def push(self, item):  
        if self.top < self.ukuran - 1:
            self.top += 1
            self.data[self.top] = item
            
    def pop(self): 
        if not self.isEmpty():
            item = self.data[self.top]
            self.data[self.top] = None
            self.top -= 1
            return item
        return None
    
    def isEmpty(self): 
        return self.top == -1
        
    def lihat(self): 
        hasil = []
        for i in range(self.top + 1):
            if self.data[i]:
                hasil.append(self.data[i])
        return hasil

# Queue buat antrian tugas
class Queue:
    def __init__(self, ukuran=100):
        self.ukuran = ukuran
        self.data = [None] * ukuran
        self.depan = 0
        self.belakang = -1
        self.jumlah = 0
    
    def enqueue(self, item):
        if self.jumlah < self.ukuran:
            self.belakang = (self.belakang + 1) % self.ukuran
            self.data[self.belakang] = item
            self.jumlah += 1
    
    def dequeue(self):
        if not self.isEmpty():
            item = self.data[self.depan]
            self.data[self.depan] = None
            self.depan = (self.depan + 1) % self.ukuran
            self.jumlah -= 1
            return item
        return None
    
    def isEmpty(self):
        return self.jumlah == 0

# Node buat Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Linked List buat nyimpan tugas
class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def tambah(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = new_node
        self.size += 1
    
    def hapus(self, idx):
        if idx < 0 or idx >= self.size:
            return None
            
        if idx == 0:
            hapus = self.head.data
            self.head = self.head.next
            self.size -= 1
            return hapus
            
        curr = self.head
        for i in range(idx - 1):
            curr = curr.next
            
        hapus = curr.next.data
        curr.next = curr.next.next
        self.size -= 1
        return hapus
    
    def lihat(self):
        hasil = []
        curr = self.head
        while curr:
            hasil.append(curr.data)
            curr = curr.next
        return hasil

# Node buat Tree
class TreeNode:
    def __init__(self, data):
        self.data = data  
        self.children = []
        
# Tree buat visualisasi tugas
class Tree:
    def __init__(self):
        self.root = None

    def buatTree(self, tugas):
        # Group tugas per matkul
        matkul_grup = {}
        for t in tugas:
            mk = t['Matkul']
            if mk not in matkul_grup:
                matkul_grup[mk] = []
            matkul_grup[mk].append(t)

        # Bikin root
        self.root = TreeNode({"Matkul": "Semua Tugas", "Ket": "Root"})
        
        # Bikin cabang per matkul
        for mk, tugas_mk in matkul_grup.items():
            node_mk = TreeNode({
                "Matkul": mk,
                "Ket": f"Ada {len(tugas_mk)} tugas"
            })
            self.root.children.append(node_mk)
            
            # Tambahin tugas ke cabang
            for t in tugas_mk:
                node_tugas = TreeNode(t)
                node_mk.children.append(node_tugas)

    def tampil(self, node=None, level=0):
        if not node:
            if not self.root:
                return "Tree kosong"
            node = self.root

        spasi = "  " * level + ("-> " if level > 0 else "")
        
        if node == self.root:
            hasil = f"{spasi}Daftar Tugas:\n"
        else:
            if "Ket" in node.data and node.children:
                hasil = f"{spasi}{node.data['Matkul']} ({node.data['Ket']}):\n"
            else:
                status = "~SELESAI" if node.data.get('Status', False) else "~Belom Selesai"
                hasil = f"{spasi}{node.data['Ket']} ({node.data['Deadline']}) {status}\n"

        for anak in node.children:
            hasil += self.tampil(anak, level + 1)
        return hasil

# Graph buat relasi antar tugas 
class Graph:
    def __init__(self):
        self.graph = {}
        
    def tambahTugas(self, tugas):
        if tugas['Matkul'] not in self.graph:
            self.graph[tugas['Matkul']] = []
        self.graph[tugas['Matkul']].append(tugas)
    
    def cariTugasTerkait(self, matkul):
        if matkul in self.graph:
            return self.graph[matkul]
        return []

# Sorting 
def sort_tugas(arr, key):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if isinstance(arr[j][key], str) and isinstance(arr[j+1][key], str):
                if arr[j][key].lower() > arr[j+1][key].lower():
                    arr[j], arr[j+1] = arr[j+1], arr[j]
            else:
                tgl1 = datetime.strptime(arr[j][key], "%d-%m-%y")
                tgl2 = datetime.strptime(arr[j+1][key], "%d-%m-%y")
                if tgl1 > tgl2:
                    arr[j], arr[j+1] = arr[j+1], arr[j]

# Search 
def cari_tugas(arr, cari, key):
    for i, item in enumerate(arr):
        if item[key].lower() == cari.lower():
            return i
    return -1

# Data awal
tugas_list = [    
    {
        "Matkul": "basisdata 2",
        "Jenis": "Individu", 
        "Ket": "modul 6",
        "Deadline": "13-12-24",
        "Status": True
    },
    {
        "Matkul": "strukdata",
        "Jenis": "Individu",
        "Ket": "Project",
        "Deadline": "17-12-24", 
        "Status": True
    },
    {
        "Matkul": "arkom",
        "Jenis": "Individu",
        "Ket": "PBL",
        "Deadline": "17-12-24",
        "Status": True
    },
    {
        "Matkul" : "kewarganegaraan",
        "Jenis" : "individu",
        "Ket" : "tugas pancasila-1",
        "Deadline" : "19-12-24",
        "Status" : True
    },
    {
        "Matkul" : "matematika diskrit",
        "Jenis" : "individu",
        "Ket" : "latihan",
        "Deadline" : "24-12-24",
        "Status" : True
    },
    {
        "Matkul" : "arkom",
        "Jenis" : "kelompok",
        "Ket" : "tugas PJBL",
        "Deadline" : "25-12-24",
        "Status" : True
    },
    {
        "Matkul" : "basisdata 2",
        "Jenis" : "individu",
        "Ket" : "tugas praktikum",
        "Deadline" : "25-12-24",
        "Status" : False
    },
    {
        "Matkul" : "basisdata 2",
        "Jenis" : "kelompok",
        "Ket" : "laprak modul 7",
        "Deadline" : "31-12-24",
        "Status" : True
    },
    {
        "Matkul" : "matematika diskrit",
        "Jenis" : "individu",
        "Ket" : "kerjakan soal kumpulkan didrive",
        "Deadline" : "31-12-24",
        "Status" : False
    },
    {
        "Matkul" : "basisdata 2",
        "Jenis" : "individu",
        "Ket" : "langkah praktikum",
        "Deadline" : "31-12-24",
        "Status" : False
    } 
]     

# Inisialisasi
daftar = LinkedList()
history = Stack()
antrian = Queue()  
graph = Graph()

# Masukin data awal
for t in tugas_list:
    daftar.tambah(t.copy())
    graph.tambahTugas(t.copy())

# Main Program
while True:
    print("===== Manager Tugas =====")
    print("1. Tambah Tugas")
    print("2. Lihat Tugas") 
    print("3. Hapus Tugas")
    print("4. Cari Tugas")
    print("5. History")
    print("6. Lihat Graph")
    print("0. Keluar")

    menu = input("Pilih menu: ")

    if menu == "0":
        print("Bye bye! :D")
        break

    elif menu == "1":
        print("== Tambah Tugas Baru ==")
        matkul = input("Matkul: ")
        jenis = input("Jenis: ")
        ket = input("Keterangan: ")
        deadline = input("Deadline (DD-MM-YY): ")

        tugas_baru = {
            "Matkul": matkul,
            "Jenis": jenis,
            "Ket": ket,
            "Deadline": deadline,
            "Status": False
        }

        daftar.tambah(tugas_baru)
        antrian.enqueue(tugas_baru)
        graph.tambahTugas(tugas_baru)
        print("Tugas ditambahkan!")

    elif menu == "2":
        print("== Tampilan Tugas ==")
        print("1. Tabel")
        print("2. Tree")
        sub = input("Pilih (1/2): ")
        
        tugas = daftar.lihat()
        if tugas:
            if sub == "1":
                tabel = PrettyTable()
                tabel.field_names = ['No', 'Matkul', 'Jenis', 'Ket', 'Deadline', 'Status']
                for i, t in enumerate(tugas, 1):
                    status = "~SELESAI" if t["Status"] else "~Belom Selesai"
                    tabel.add_row([i, t['Matkul'], t['Jenis'], t['Ket'], t['Deadline'], status])
                print(tabel)
            elif sub == "2":
                pohon = Tree()
                pohon.buatTree(tugas)
                print("Tree Tugas:")
                print(pohon.tampil())
            else:
                print("Input salah!")
        else:
            print("Belum ada tugas kakaaa...")

    elif menu == "3":
        print("== Hapus Tugas ==")
        tugas = daftar.lihat()
        if tugas:
            matkul = input("Matkul yang mau dihapus apa nihh: ")
            cocok = []
            for i, t in enumerate(tugas):
                if t["Matkul"].lower() == matkul.lower():
                    cocok.append((i, t))
            
            if cocok:
                print("Tugas yang bisa dihapus:")
                tabel = PrettyTable()
                tabel.field_names = ['No', 'Matkul', 'Jenis', 'Ket', 'Deadline', 'Status']
                for i, (idx, t) in enumerate(cocok, 1):
                    status = "~SELESAI" if t["Status"] else "~Belom Selesai"
                    tabel.add_row([i, t['Matkul'], t['Jenis'], t['Ket'], t['Deadline'], status])
                print(tabel)

                try:
                    pilih = int(input("Pilih nomor tugas: "))
                    if 1 <= pilih <= len(cocok):
                        idx_hapus = cocok[pilih-1][0]
                        tugas_hapus = daftar.hapus(idx_hapus)
                        if tugas_hapus:
                            history.push(tugas_hapus)
                            print("Tugas dihapus!")
                        else:
                            print("Gagal hapus.")
                    else:
                        print("Nomor invalid.")
                except:
                    print("Input salah.")
            else:
                print(f"Ga jumpa matkul {matkul}")
        else:
            print("Mana tugasnya....")

    elif menu == "4":
        print("== Cari Tugas ==")
        print("1. Cari Status")
        print("2. Cari Deadline")
        sub = input("Pilih (1/2): ")
       
        if sub == "1":
            tugas = daftar.lihat()
            if tugas:
                print("Status:")
                print("1. Selesai")
                print("2. Belom Selesai")
                status = input("Pilih (1/2): ")
         
                if status == "1":
                    cari = True
                    txt = "~SELESAI"
                elif status == "2":
                    cari = False
                    txt = "~Belom Selesai"
                else:
                    print("Invalid!")
                    continue

                hasil = []
                for t in tugas:
                    if t["Status"] == cari:
                        hasil.append(t)
         
                if hasil:
                    print(f"Tugas {txt}:")
                    tabel = PrettyTable()
                    tabel.field_names = ['No', 'Matkul', 'Jenis', 'Ket', 'Deadline', 'Status']
                    for i, t in enumerate(hasil, 1):
                        status = "~SELESAI" if t["Status"] else "~Belom Selesai"
                        tabel.add_row([i, t['Matkul'], t['Jenis'], t['Ket'], t['Deadline'], status])
                    print(tabel)
                else:
                    print(f"Ga ada tugas uhuyy {txt}.")

        elif sub == "2":
            deadline = input("Deadline (DD-MM-YY): ")
            tugas = daftar.lihat()
            hasil = []
            for t in tugas:
                if t["Deadline"] == deadline:
                    hasil.append(t)
            
            if hasil:
                print(f"\nTugas deadline {deadline}:")
                tabel = PrettyTable()
                tabel.field_names = ['Matkul', 'Jenis', 'Ket', 'Status']
                for t in hasil:
                    status = "~SELESAI" if t["Status"] else "~Belom Selesai"
                    tabel.add_row([t['Matkul'], t['Jenis'], t['Ket'], status])
                print(tabel)
            else:
                print(f"wisss ga ada deadline {deadline}")
        else:
            print("Salah Input Woy!")

    elif menu == "5":
        print("== History Tugas ==")
        print("Dari stack:")
        items = history.lihat()
        if items:
            tabel = PrettyTable()
            tabel.field_names = ['No', 'Matkul', 'Jenis', 'Ket', 'Deadline', 'Status']
            tampil = items[::-1]  
            for i, t in enumerate(tampil, 1):
                if t:  # Cek kalau ada isinya
                    status = "~SELESAI" if t["Status"] else "~Belom Selesai"
                    tabel.add_row([i, t['Matkul'], t['Jenis'], t['Ket'], t['Deadline'], status])
            print(tabel)
        else:
            print("Kosong lahh :( ...")

    elif menu == "6":
        print("== Graph Tugas ==")
        print("Hubungan antar tugas per matkul:")
        for matkul, tugas in graph.graph.items():
            print(f"\nMatkul: {matkul}")
            if tugas:
                tabel = PrettyTable()
                tabel.field_names = ['Jenis', 'Ket', 'Deadline', 'Status']
                for t in tugas:
                    status = "~SELESAI" if t["Status"] else "~Belom Selesai"
                    tabel.add_row([t['Jenis'], t['Ket'], t['Deadline'], status])
                print(tabel)
            else:
                print("Gak ada tugas cuyy")
    
    else:
        print("salah menu kakaaaa!")
        