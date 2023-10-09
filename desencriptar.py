from cryptography.fernet import Fernet

#Abrimo llave en archivo clave.key
with open("clave.key", "rb") as key_file:
    key = key_file.read()
cipher_suite = Fernet(key)

# Para recuperar el texto encriptado del archivo más adelante:
with open("texto_encriptado.txt", "rb") as file:
     texto_encriptado = file.read()

texto_desencriptado_bytes = cipher_suite.decrypt(texto_encriptado)
texto_desencriptado = texto_desencriptado_bytes.decode('utf-8')

# Guarda el texto encriptado en un archivo txt
with open("texto_desencriptado.txt", "w") as file:
    file.write(texto_desencriptado)

print("Texto desencriptado y guardado en texto_desencriptado.txt")
input()
