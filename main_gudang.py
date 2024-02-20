from tabulate import tabulate
import regex as re
import sys

# -------------------------MENU ADMIN-------------------------
def menu_admin(): # pakai return karena agar output berada dibawah kata hello
    return(f'''
---------------------------------
>> MAIN MENU
1. Dashboard
2. Data User
3. Data Barang
4. Logout
---------------------------------
''')

# -------------------------MENU USER-------------------------
def menu_user(): # pakai return karena agar output berada dibawah kata hello
    return(f'''
---------------------------------
>> MENU UTAMA
1. Dashboard
2. Sorting Data Barang
3. Searching Data Barang
4. Logout
---------------------------------
''')
# -------------------------DATA USER-------------------------
data_user = [
    {'no' : 1, 'user id' : 'ADMIN001', 'username' : 'admin', 'department' : 'Admin', 'password' : '12345', 'role' : 'admin'},
    {'no' : 2, 'user id' : 'USER001', 'username' : 'malik', 'department' : 'Produksi', 'password' : '123', 'role' : 'user'},
    {'no' : 3, 'user id' : 'USER002', 'username' : 'indah', 'department' : 'Riset dan Pengembangan', 'password' : '123', 'role' : 'user'},
    {'no' : 4, 'user id' : 'USER003', 'username' : 'zack', 'department' : 'Pemasaran', 'password' : '123', 'role' : 'user'},
    {'no' : 5, 'user id' : 'USER004', 'username' : 'yuke', 'department' : 'Kualitas dan Pengawasan', 'password' : '123', 'role' : 'user'},
    {'no' : 6, 'user id' : 'USER005', 'username' : 'lola', 'department' : 'Logistik dan Distribusi', 'password' : '123', 'role' : 'user'}
]

# -------------------------SHOW DATA USER-------------------------
def read_data_user():
    print(f'Jumlah Data User : {len(data_user)}')
    print(tabulate(data_user, headers='keys', tablefmt='pretty'))

# -------------------------DATA BARANG-------------------------
data_barang = [
    {'no' : 1, 'barang id' : 'BRG001', 'nama barang' : 'TEPUNG', 'satuan' : 'KG', 'harga satuan(IDR)' : '20000', 'stok awal' : 100, 'stok masuk' : 0, 'stok keluar' : 0, 'stok akhir' : 100},
    {'no' : 2, 'barang id' : 'BRG002', 'nama barang' : 'KEMASAN SNACK ANGGUR', 'satuan' : 'PCS', 'harga satuan(IDR)' : '10000', 'stok awal' : 90, 'stok masuk' : 0, 'stok keluar' : 0, 'stok akhir' : 90},
    {'no' : 3, 'barang id' : 'BRG003', 'nama barang' : 'PERASA BUAH ANGGUR', 'satuan' : 'KG', 'harga satuan(IDR)' : '25000', 'stok awal' : 50, 'stok masuk' : 0, 'stok keluar' : 0, 'stok akhir' : 50}
]

# -------------------------MENU DATA BARANG-------------------------
def menu_barang(): # pakai return karena agar output berada dibawah kata hello
    return(f'''
---------------------------------
>> MENU DATA BARANG
1. Dashboard
2. Show Data Barang
3. Add Data Barang
4. Edit Data Barang
5. Delete Data Barang
6. Stock in Data Barang
7. Stock out Barang
8. Sorting Data Barang
9. Searching Data Barang
---------------------------------
''')

# -------------------------VALIDASI HURUF-------------------------
def validasi_huruf(label, info):
    while True:
        print(info)
        inputan = input(label)
        if re.fullmatch("[a-zA-Z]+", inputan):
            inputan = inputan.upper()
            return inputan
        elif re.fullmatch("[\w]+", inputan):
            print("Input is invalid")
        else:
            print('Input cannot be empty')

# -------------------------VALIDASI ANGKA-------------------------
def validasi_angka(label, info):
    while True:
        print(info)
        inputan = input(label)
        if re.fullmatch("[\d]+", inputan):
            inputan = int(inputan)
            return inputan
        elif re.fullmatch("[\w]+", inputan):
            print("Input is invalid")
        else:
            print('Input cannot be empty')

# -------------------------OPSI MENU BARANG-------------------------
def opsi_menu_barang():
    print(f'{menu_barang()}')
    while True:
        try:
            opsi_menu_barang = validasi_angka('Choose a number from menu barang \t: ', '\nEx. 1')
            if opsi_menu_barang == 1:
                print(f'{menu_admin()}')
                break
            elif opsi_menu_barang == 2:
                print('>> Show Data Barang')
                read_data_barang()
                print(f'{menu_barang()}')
            elif opsi_menu_barang == 3:
                print('>> Add Data Barang')
                read_data_barang()
                create_data_barang()
                print(f'{menu_barang()}')
            elif opsi_menu_barang == 4:
                print('>> Edit Data Barang')
                read_data_barang()
                update_data_barang()
                print(f'{menu_barang()}')
            elif opsi_menu_barang == 5:
                print('>> Delete Data Barang')
                read_data_barang()
                delete_data_barang()
                print(f'{menu_barang()}')
            elif opsi_menu_barang == 6:
                print('>> Stok In Data Barang')
                read_data_barang()
                stokin_databarang()
                print(f'{menu_barang()}')
            elif opsi_menu_barang == 7:
                print('>> Stok Out Data Barang')
                read_data_barang()
                stokout_databarang()
                print(f'{menu_barang()}')
            elif opsi_menu_barang == 8:
                print('>> Sorting Data Barang')
                read_data_barang()
                opsi_sorting_databarang()
                print(f'{menu_barang()}')
            elif opsi_menu_barang == 9:
                print('>> Searching Data Barang')
                read_data_barang()
                opsi_searching_databarang()
                print(f'{menu_barang()}')
            else:
                print('Input a number in the Menu Data Barang')
        except ValueError:
            print('error')
            break
    return

# -------------------------SHOW DATA BARANG-------------------------
def read_data_barang():
    print(f'Total Data Barang : {len(data_barang)}')
    for i in range (len(data_barang)):
        data_barang[i]['no'] = i+1
    print(tabulate(data_barang, headers='keys', tablefmt='pretty'))

# -------------------------ADD DATA BARANG-------------------------
def create_data_barang():
    global data_barang
    no = len(data_barang)+1
    barangid_tmp = data_barang[-1]['barang id']
    angka_id = int(barangid_tmp[-1])+1
    # print(barangid_tmp, type(barangid_tmp))
    # print(angka_id, type(angka_id))
    barang_id = f'BRG00{angka_id}' if angka_id <= 9 else (f'BRG0{angka_id}' if angka_id <=99 else (f'BRG{angka_id}' if angka_id == 100 else f'Data Overload'))
               
    while True: # nama_barang
        try:
            print('\n(i) The first character must be a alphabet and at least 4 characters ')
            nama_barang = input('Nama Barang \t: ')
            len_barang = len(nama_barang)
            first_character = nama_barang[0]
            if len_barang >= 4 and first_character.isalpha():
                nama_barang = nama_barang.upper()
                break
            else:
                print('__Input is invalid__')
        except:
            print('__Input cannot be empty__')
            
    satuan = validasi_huruf('Satuan \t: ', '\n(i)Ex. Satuan : Kg')
    harga_satuan = validasi_angka('Harga Satuan(IDR) \t: ', '\n(i)Ex. Harga Satuan(IDR) : 25000')
    stok_awal = validasi_angka('Stok Awal \t: ', '\n(i)Ex. Stok Awal : 50')
    stok_masuk = 0
    stok_keluar = 0
    stok_akhir = stok_awal + stok_masuk - stok_keluar
    
    new_data = {'no' : no, 'barang id' : barang_id, 'nama barang' : nama_barang, 'satuan' : satuan, 'harga satuan(IDR)' : harga_satuan, 'stok awal' : stok_awal, 'stok masuk' : stok_masuk, 'stok keluar' : stok_keluar, 'stok akhir' : stok_akhir}
    data_barang.append(new_data)
    print(f'__Data successfully added__')
    read_data_barang()
    return

# -------------------------EDIT DATA BARANG-------------------------
def update_data_barang():
    global data_barang
    keys = ['no', 'barang id', 'nama barang', 'satuan', 'harga satuan(IDR)', 'stok awal', 'stok masuk', 'stok keluar', 'stok akhir']
    
    select_barangid = input('Input barang id for editing \t: ') # check barang id
    found = 'not found'
    for barang in data_barang:
        if barang['barang id'] == select_barangid:
            found = 'found'
            break

    if found == 'found':
        print('Data barang before update')
        print(tabulate([barang.values()], headers=keys, tablefmt='pretty'))
        print(f'''
---------------------------------
>> Atribute
1. Nama Barang
2. Satuan
3. Harga Barang(IDR)
4. Stok Awal
---------------------------------
        ''')
        while True:
            select_atribute = validasi_angka('Input no atribute for editing \t: ', '\n(i) Ex. 1')
            try:
                if select_atribute == 1:
                    print('>> Edit Nama Barang')
                    while True: # nama_barang
                        try:
                            print('\n(i) The first character must be a alphabet and at least 4 characters ')
                            new_value = input('Nama Barang \t: ')
                            len_barang = len(new_value)
                            first_character = new_value[0]
                            if len_barang >= 4 and first_character.isalpha():
                                new_value = new_value.upper()
                                barang['nama barang'] = new_value
                                print(f'__Data successfully updated__')
                                print('Data barang after update')
                                print(tabulate([barang.values()], headers=keys, tablefmt='pretty'))
                                break
                            else:
                                print('__Input is invalid__')
                        except:
                            print('__Input cannot be empty__')
                    break
                elif select_atribute == 2:
                    print('>> Edit Satuan')
                    new_value = validasi_huruf('Satuan \t: ', '\n(i)Ex. Satuan : Kg')
                    barang['satuan'] = new_value
                    print(f'__Data successfully updated__')
                    print('Data barang after update')
                    print(tabulate([barang.values()], headers=keys, tablefmt='pretty'))
                    break
                elif select_atribute == 3:
                    print('>> Edit Harga Barang(IDR)')
                    new_value = validasi_angka('Harga Satuan(IDR) \t: ', '\n(i)Ex. Harga Satuan(IDR) : 25000')
                    barang['harga satuan(IDR)'] = new_value
                    print(f'__Data successfully updated__')
                    print('Data barang after update')
                    print(tabulate([barang.values()], headers=keys, tablefmt='pretty'))
                    break
                elif select_atribute == 4:
                    print('>> Stok Awal')
                    new_value = validasi_angka('Stok Awal \t: ', '\n(i)Ex. Stok Awal : 50')
                    stok_masuk = barang['stok masuk']
                    stok_keluar = barang['stok keluar']

                    
                    barang['stok awal'] = new_value
                    barang['stok akhir'] = new_value + stok_masuk - stok_keluar
                    print(f'__Data successfully updated__')
                    print('Data barang after update')
                    print(tabulate([barang.values()], headers=keys, tablefmt='pretty'))
                    break
                else:
                    print('__No atribute is invalid__')
            except:
                print('')
            break
    else:
        print('__Barang Id is invalid__')
            
# -------------------------DELETE DATA BARANG-------------------------
def delete_data_barang():
    global data_barang
    while True:
        print('(i) Ex : BRG001')
        delete_barangid = input('Input barang id for deleting \t: ')
        index_to_remove = None
        try:
            for index, barang in enumerate(data_barang):
                if barang['barang id'] == delete_barangid:
                    index_to_remove = index
                    break
            if index_to_remove is not None:
                deleted_barang = data_barang.pop(index_to_remove)
                print(f"__Data barang with barang id {delete_barangid} successfully deleted__")
                read_data_barang()
                return deleted_barang
        except:
            print('__Barang id is invalid__')
            return None
        break
    print('__Barang id is invalid__')

# -------------------------STOK IN DATA BARANG-------------------------
def stokin_databarang():
    global data_barang
    keys = ['no', 'barang id', 'nama barang', 'satuan', 'harga satuan(IDR)', 'stok awal', 'stok masuk', 'stok keluar', 'stok akhir']
    
    while True:
        select_barangid = input('Input barang id for stok in \t: ').upper()
        found = 'not found'
        for barang in data_barang:
            if barang['barang id'] == select_barangid:
                found = 'found'
                break
        
        if found == 'found':
            print('Data barang before stok in')
            print(tabulate([barang.values()], headers=keys, tablefmt='pretty'))
            new_stokin = validasi_angka('Stok Masuk \t: ', '\n(i)Ex. Stok Masuk : 50')
            stok_awal = barang['stok awal']
            stok_masuk = barang['stok masuk']
            stok_keluar = barang['stok keluar']

            barang['stok masuk']= stok_masuk + new_stokin
            barang['stok akhir'] = stok_awal + stok_masuk - stok_keluar + new_stokin
            print('__Stok in successfully added__')
            print('Data barang after stok in')
            print(tabulate([barang.values()], headers=keys, tablefmt='pretty'))
            break
        else:
            print('__Barang id is invalid__')
            break

# -------------------------STOK OUT DATA BARANG-------------------------
def stokout_databarang():
    global data_barang
    keys = ['no', 'barang id', 'nama barang', 'satuan', 'harga satuan(IDR)', 'stok awal', 'stok masuk', 'stok keluar', 'stok akhir']
    
    while True:
        select_barangid = input('Input barang id for stok out \t: ').upper()
        found = 'not found'
        for barang in data_barang:
            if barang['barang id'] == select_barangid:
                found = 'found'
                break
        
        if found == 'found':
            print('Data barang before stok out')
            print(tabulate([barang.values()], headers=keys, tablefmt='pretty'))
            new_stokout = validasi_angka('Stok Keluar \t: ', '\n(i)Ex. Stok Keluar  : 50')
            stok_awal = barang['stok awal']
            stok_masuk = barang['stok masuk']
            stok_keluar = barang['stok keluar']
            stok_akhir = barang['stok akhir']

            if stok_akhir < new_stokout:
                print('__Stok akhir not enough__')
                break
            else:
                barang['stok keluar']= stok_keluar + new_stokout
                barang['stok akhir'] = stok_awal + stok_masuk - stok_keluar - new_stokout
                print('__Stok out successfully added__')
                print('Data barang after stok out')
                print(tabulate([barang.values()], headers=keys, tablefmt='pretty'))
                break
        else:
            print('__Barang id is invalid__')
            break
        
# -------------------------OPSI SORTING-------------------------
def opsi_sorting_databarang():
    global data_barang

    print(f'''
---------------------------------
>> SORTING DATA BARANG
1. ASC Barang Id
2. ASC Nama Barang
3. ASC Harga Satuan
4. ASC Stok Akhir
5. DESC Barang Id
6. DESC Nama Barang
7. DESC Harga Satuan
8. DESC Stok Akhir
---------------------------------
''')
    while True:
        select_no = validasi_angka('Choose a number in sorting data barang \t: ', '\nEx. 1')
        if select_no == 1:
            data_barang = sorted(data_barang, key=lambda data : data['barang id'])
            print('>> ASC Barang Id')
            read_data_barang()
            break
        elif select_no == 2:
            data_barang = sorted(data_barang, key=lambda data : data['nama barang'])
            print('>> ASC Nama Barang')
            read_data_barang()
            break
        elif select_no == 3:
            data_barang = sorted(data_barang, key=lambda data : data['harga satuan(IDR)'])
            print('>> ASC Harga Satuan')
            read_data_barang()
            break
        elif select_no == 4:
            data_barang = sorted(data_barang, key=lambda data : data['stok akhir'])
            print('>> ASC Stok Akhir')
            read_data_barang()
            break
        elif select_no == 5:
            data_barang = sorted(data_barang, key=lambda data : data['barang id'], reverse=True)
            print('>> DESC Barang Id')
            read_data_barang()
            break
        elif select_no == 6:
            data_barang = sorted(data_barang, key=lambda data : data['nama barang'], reverse=True)
            print('>> DESC Nama Barang')
            read_data_barang()
            break
        elif select_no == 7:
            data_barang = sorted(data_barang, key=lambda data : data['harga satuan(IDR)'], reverse=True)
            print('>> DESC Harga Satuan')
            read_data_barang()
            break
        elif select_no == 8:
            data_barang = sorted(data_barang, key=lambda data : data['stok akhir'], reverse=True)
            print('>> DESC Stok Akhir')
            read_data_barang()
            break
        else:
            print('__Number is invalid__')

# -------------------------OPSI SEARCHING-------------------------
def opsi_searching_databarang():
    print(f'''
---------------------------------
>>  SEARCHING DATA BARANG
1. Barang Id
2. Nama Barang
---------------------------------
''')
    while True:
        select_no = validasi_angka('Choose a number in searching data barang \t: ', '\nEx. 1')
        
        if select_no == 1:
            search('barang id')
        elif select_no == 2:
            search('nama barang')
        else: 
            print('__Number is invalid__')
        break
# -------------------------SEARCH-------------------------
def search(atribute):
    global data_barang, found, barang, results
    keys = ['no', 'barang id', 'nama barang', 'satuan', 'harga satuan(IDR)', 'stok awal', 'stok masuk', 'stok keluar', 'stok akhir']
    found = 'not found'
    results = []
    
    while True:
        search = input(f'\nInput {atribute} you want to search \t: ')
        search = search.upper()

        if not search.strip():
            print("__Input not be empty__")
            continue

        try:
            for barang in data_barang:
                atribute_search = barang[atribute]
                if re.search(search, atribute_search):
                    found = 'found'
                    results.append(barang)

            if found == 'found':
                for result in results:
                    print('--Result search data barang--')
                    print(tabulate([result.values()], headers=keys, tablefmt='pretty'))
                break
            else:
                print('__Data Not Found__')
                break
        except:
            print(f'__{atribute} is invalid__')
            break
        

# -------------------------MAIN-------------------------
def main():
    print(f'\tAPLIKASI GUDANG PT. FRESH FOOD\n-----------------------------------------------\n')
    while True:
        print(f'>> LOGIN')
        user_id = input('Username \t: ')
        password = input('Password \t: ')
        print('---------------------------------')
        for user in data_user:
            if user['user id'] == user_id and user['password'] == password:
                role = user.get('role')
                username = user.get('username')
                department = user.get('department')
                if role == 'admin':
                    print(f'\tHello "{username}"\n{menu_admin()}')
                    while True:
                        try:
                            opsi_menu = int(input('Choose a number from main menu \t: '))
                            if opsi_menu == 1: # Dashboard
                                print(f'{menu_admin()}')
                            elif opsi_menu == 2: # Data User
                                read_data_user()
                                print(f'{menu_admin()}')
                            elif opsi_menu == 3: # Data Barang
                                opsi_menu_barang()
                            elif opsi_menu == 4: # Logout
                                logout()
                                print(f'{menu_admin()}')
                            else:
                                print('__Please input a number in the main menu__\n') 
                        except ValueError:        
                            print('__Please input a number, not an alphabet or empty__\n')       
                elif role == 'user':
                    print(f'\tHello "{username}"')
                    print(f'     Department : "{department}"\n{menu_user()}')
                    while True:
                        try:
                            opsi_menu = int(input('Choose a number from main menu \t: '))
                            if opsi_menu == 1: # Dashboard
                                print(f'{menu_user()}')
                            elif opsi_menu == 2: # Sorting
                                opsi_sorting_databarang()
                                print(f'{menu_user()}')
                            elif opsi_menu == 3: # Searching
                                opsi_searching_databarang()
                                print(f'{menu_user()}')
                                print('history')
                            elif opsi_menu == 4: # Logout
                                logout()
                                print(f'{menu_user()}')
                            else:
                                print('__Please input a number in the main menu__\n') 
                        except ValueError:        
                            print('__Please input a number, not an alphabet or empty__\n')

        print('__Login is invalid, please input the correct username and password__')

# -------------------------LOGOUT-------------------------
def logout():
    while True:
        confirm = input('Do you really want to logout? (Y/N) \t: ')
        confirm = confirm.upper()
        if confirm == 'Y':
            print('__Thank You__')
            sys.exit()
        elif confirm == 'N':
            break
        else:
            print('__Input is invalid__')
            break

main()