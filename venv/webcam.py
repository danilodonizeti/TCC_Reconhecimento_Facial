import numpy as np
import face_recognition as fr
import cv2 #opencv # Visão computacional
from engine import get_rostos

def verificar_pessoa():
    rostos_conhecidos, nome_dos_rostos = get_rostos()

    video_capture = cv2.VideoCapture(0)

    while True:
        ret, frame = video_capture.read()

        rgb_frame = frame[:, :, ::-1]

        face_locations = fr.face_locations(rgb_frame)
        face_encodings = fr.face_encodings(rgb_frame, face_locations)

        for(top, right, bottom, left), face_encodings in zip(face_locations, face_encodings):
            resultados = fr.compare_faces(rostos_conhecidos,face_encodings)
            print(resultados)

            face_distances = fr.face_distance(rostos_conhecidos, face_encodings) # Distância entre os rostos

            melhor_id = np.argmin(face_distances)
            if resultados[melhor_id]:
                nome = nome_dos_rostos[melhor_id]
            else:
                nome = 'Desconhecido'

            # Desenhar quadrado nas faces

            # Quadrado ao redor do rosto
            cv2.rectangle(frame, (left+10, top+10), (right+10, bottom+10), (0, 0, 255), 2)

            # Embaixo
            cv2.rectangle(frame, (left, bottom -25), (right, bottom), (0, 0, 255), cv2.FILLED) #cv2.FILLED é que a expessura da linha completa o retângulo
            font = cv2.FONT_HERSHEY_SIMPLEX

            # Texto
            cv2.putText(frame, nome, (left + 3, bottom - 3), font, 0.5, (255, 255, 255), 1)

            cv2.imshow('Reconhecimento Facial', frame)

        if cv2.waitKey(5) & 0xFF == ord('q'): # or key == 27:
            break

    video_capture.release()
    cv2.destroyAllWindows()

    return nome