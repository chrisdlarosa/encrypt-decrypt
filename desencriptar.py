from cryptography.fernet import Fernet

#Abrimo llave en archivo clave.key
with open("clave.key", "rb") as key_file:
    key = key_file.read()
cipher_suite = Fernet(key)

# Para recuperar el texto encriptado del archivo más adelante:
with open("mensaje.txt", "rb") as file:
     texto_encriptado = file.read()

texto_desencriptado_bytes = cipher_suite.decrypt(texto_encriptado)
texto_desencriptado = texto_desencriptado_bytes.decode('utf-8')

# Guarda el texto encriptado en un archivo txt
with open("mensaje.txt", "w") as file:
    file.write(texto_desencriptado)

print("Texto desencriptado y guardado en mensaje.txt")
input()
