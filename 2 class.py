class Kalkulator:
    """contoh kelas kalkulator sederhana"""
    i = 12345

    def f(self):
        return 'hello world'

    @staticmethod
    def kali_angka(angka1, angka2):
        return '{} x {} = {}'.format(angka1, angka2, angka1 * angka2)

Kalkulator.i = 1024
print(Kalkulator.i)

k = Kalkulator()
print(k.f())
print(Kalkulator.f(k))

a = k.kali_angka(2, 3)
print(a)