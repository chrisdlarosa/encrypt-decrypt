from cryptography.fernet import Fernet

# Genera una clave de cifrado aleatoria
key = Fernet.generate_key()
# Se crea un objeto Fernet con la clave
cipher_suite = Fernet(key)
#Se guacrda clave en clave.key
with open("clave.key", "wb") as key_file:
    key_file.write(key)

# Introduce Texto que deseas encriptar
texto_original = input("Intoduce texto a cifrar:  ")

# Convierte el texto en bytes
texto_bytes = texto_original.encode('utf-8')
# Encripta el texto
texto_encriptado = cipher_suite.encrypt(texto_bytes)

# Guarda el texto encriptado en un archivo txt
with open("texto_encriptado.txt", "wb") as file:
    file.write(texto_encriptado)

print("Texto encriptado y guardado en texto_encriptado.txt")
print("Clave generada y guardada en clave.key")
input()