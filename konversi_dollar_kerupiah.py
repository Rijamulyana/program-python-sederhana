def main():
    print("\nkonversi dollar ke rupiah")
    print("===========================")

    dollar = float(input("Masukkan uang dollar: \n"))
    print("uang kamu :", dollar, "dolar")
    rp = convert_to_rupiah(dollar)

    print("konversi ke Rupiah:", rp, "Rupiah.")
    print("===========================\n")


def convert_to_rupiah(dollar):
    return dollar * 15500, 00


main()
