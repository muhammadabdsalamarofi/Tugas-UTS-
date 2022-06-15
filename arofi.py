class Identitas():
    def __init__(self, Nama, Tempat_Tanggal_lahir, Alamat, Desa, Rt_Rw, Jenis_Kelamin,):
        self.Nama = Nama
        self.Tempat_Tanggal_lahir = Tempat_Tanggal_lahir
        self.Alamat = Alamat
        self.Desa = Desa
        self.Rt_Rw = Rt_Rw
        self.Jenis_Kelamin = Jenis_Kelamin
    def masuk (self, Nama, Tempat_Tanggal_lahir, Alamat, Desa, Rt_Rw, Jenis_Kelamin):
        self.Nama = Nama
        self.Tempat_Tanggal_lahir = Tempat_Tanggal_lahir
        self.Alamat = Alamat
        self.Desa = Desa
        self.Rt_Rw = Rt_Rw
        self.Jenis_Kelamin = Jenis_Kelamin
    def keluar (self):
        print('Nama Lengkap     :' + self.Nama)
        print('Tempat_Tanggal_lahir           :' + self.Tempat_Tanggal_lahir)
        print('Alamat           :' + self.Alamat)
        print('Desa           :' + self.Desa)
        print('Rt_Rw           :' + self.Rt_Rw)
        if self.Jenis_Kelamin in [ 'L', 'l']:
            Jenis_Kelamin = 'laki-laki'
        else:
            Jenis_Kelamin ='perempuan'
        print('Jenis_Kelamin   :' + Jenis_Kelamin)
        

print('=================================')
print('.................................')
print('          IDENTITAS DIRI         ')
print(' ')
Nama    = input('Nama Lengkap              :')
Tempat_Tanggal_lahir  = input('Tempat_Tanggal_lahir           :')
Alamat  =input('Alamat             :')
Desa  =input('Desa             :')
Rt_Rw  =input('Rt_Rw             :')
Jenis_Kelamin  = input('gender L/P   :')
print('.................................')
print('=================================')
print(' ')

proses = Identitas (Nama, Tempat_Tanggal_lahir, Alamat, Desa, Rt_Rw, Jenis_Kelamin)
print(proses.keluar())