

from src.rsa import RSAKey, import_key
import src.interface as interface


import time

def main():
    start_time = time.time()
    bit_size = 1024
    pub_key = None
    prv_key = None

    c = True
    while c:
        if not (pub_key or prv_key):
            print("Public and Private key not found, you should generate one to continue.")
        interface.print_menu()
        c = input("Select an option: ")
        if c == '1':
           
            print('--------------------------------------Key Generator Module--------------------------------------')
                    # generate new key 1024 bits:
            bit_size =  input("Select a key size in bits (needs to be a power of 2 bigger than 256): ")
            bit_size =  int(bit_size)

            print("generating new key with primes of size " + str(bit_size)+ " bits... (this can take a while)")

            key_pairs = RSAKey(bit_size)
            # get public key
            pub_key = key_pairs.public_key
            # get private key
            prv_key = key_pairs.private_key
            print('Public Key: ', pub_key.get_key())
            print('Private Key: ', prv_key.get_key())
        elif c == '2':
        # importing/exporting keys section:
            interface.import_export(pub_key=pub_key, prv_key=prv_key)   

        elif c == '3':
        # Basic Encrypting Section:
            interface.basicEncryption()
            
        elif c == '4':
        # verification section
            interface.verification()

        elif c == '5':
        # oaep section
            try:
                interface.rsaoaep()
            except:
                print("An error ocurred, int too big to convert.")  
        elif c == '6':
            interface.key_values()
        elif c == '7':
            break
        else:
            print('Opcao inválida.')



if __name__ == '__main__':
    start_time = time.time()
    main()
    print("--- %s Total seconds ---" % (time.time() - start_time))
