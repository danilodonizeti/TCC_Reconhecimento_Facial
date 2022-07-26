# from deepface import DeepFace as deepface
# import reconhecimento_facial
# import webcam
import shutil

# fotos_cadastradas = r'C:\Users\danil\PycharmProjects\TCC_Reconhecimento_Facial\venv\Fotos Cadastradas'
#
# models = ["VGG-Face", "Facenet", "Facenet512", "OpenFace", "DeepFace", "DeepID", "ArcFace", "Dlib", "SFace"]
#
# # deepface.stream(db_path=fotos_cadastradas)
# # deepface.stream(db_path=fotos_cadastradas, model_name=models[4])
#
# reconhecimento_facial.comparar_imagens()

# # TESTE WEBCAM
# verificar = webcam.verificar_pessoa()
# nome_pessoa = webcam.verificar_pessoa()
# # nome_pessoa = verificar.nome
#
# if nome_pessoa != 'Desconhecido':
#     print(f'Segredo revelado para {nome_pessoa}')
# else:
#     print('Pessoa não identificada. Segredo não revelado')
#
# print(f'Pessoa: {nome_pessoa}')




# TESTE SHUTIL


cpf = 7889
nome = 'Alexandre'
nome_foto = f'{cpf}-{nome}'
foto_para_mover = 'C:/Users/danil/PycharmProjects/TCC_Reconhecimento_Facial/'
foto_para_mover = f'{foto_para_mover}{nome_foto}.png'
print('DE:')
print(foto_para_mover)
# foto_para_mover = 'C:/Users/danil/PycharmProjects/TCC_Reconhecimento_Facial/7889-Alexandre.png'
pasta_onde_colar = 'C:/Users/danil/PycharmProjects/TCC_Reconhecimento_Facial/venv/Fotos Cadastradas'
print('PARA:')
print(pasta_onde_colar)
# pasta_onde_colar = pasta_onde_colar + nome_foto
# Mover foto para fotos cadastradas
shutil.move(foto_para_mover, pasta_onde_colar)
print('FOTO MOVIDA COM SUCESSO.')
