import face_recognition as fr
import os

def qtd_fotos_cadastradas():
    # Contar quantas fotos há na pasta "Fotos Cadastradas"
    fotos_cadastradas_path = './venv/Fotos Cadastradas'
    for raiz, subpastas, arquivos in os.walk(fotos_cadastradas_path):
        quantidade_fotos = len(arquivos)
        print(f'TOTAL: {quantidade_fotos} arquivos.')
    return quantidade_fotos
        # for arquivo in arquivos:
        #     print(arquivo)
        #     print(f'TOTAL: {len(arquivos)} arquivos.')

def reconhece_face(url_foto):
    foto = fr.load_image_file(url_foto)   # Carregar foto
    rostos = fr.face_encodings(foto)      # Codificar as coordenadas dos rostos da foto
    if(len(rostos) > 0):                  # Se houver ao menos um rosto na foto, retornar as coordenadas do rosto
        return True, rostos

    return False, []


def get_rostos():
    rostos_conhecidos = []
    nomes_dos_rostos = []

    # nome_foto = 'AJUSTAR NOME DA FOTO'
    # nome_foto = reconhece_face(f'C:/Users/danil/PycharmProjects/TCC_Reconhecimento_Facial/venv/Fotos Cadastradas/{nome_foto}')
    # if(nome[0]):
    #     rostos_conhecidos.append(nome[1][0])
    #     nomes_dos_rostos.append(nome)

    danilo1 = reconhece_face('C:/Users/danil/PycharmProjects/TCC_Reconhecimento_Facial/venv/Fotos Cadastradas/111-Danilo Donizeti.png')
    if(danilo1[0]):
        rostos_conhecidos.append(danilo1[1][0])
        nomes_dos_rostos.append('Danilo')

    silvio1 = reconhece_face('C:/Users/danil/PycharmProjects/TCC_Reconhecimento_Facial/venv/Fotos Cadastradas/222-Silvio Santos.png')
    if(silvio1[0]):
        rostos_conhecidos.append(silvio1[1][0])
        nomes_dos_rostos.append('Silvio')

    elon1 = reconhece_face('C:/Users/danil/PycharmProjects/TCC_Reconhecimento_Facial/venv/Fotos Cadastradas/333-Elon Musk.png')
    if(elon1[0]):
        rostos_conhecidos.append(elon1[1][0])
        nomes_dos_rostos.append('Elon')

    ivete1 = reconhece_face('C:/Users/danil/PycharmProjects/TCC_Reconhecimento_Facial/venv/Fotos Cadastradas/444-Ivete Sangalo.png')
    if(ivete1[0]):
        rostos_conhecidos.append(ivete1[1][0])
        nomes_dos_rostos.append('Ivete')

    return  rostos_conhecidos, nomes_dos_rostos

pessoas = get_rostos()
# print(f'Códigos: {pessoas[0]} --> Códigos')
# print(f'Nomes das pessoas: {pessoas[1]}')
