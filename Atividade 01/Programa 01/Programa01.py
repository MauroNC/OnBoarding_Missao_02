import cv2

# Carregar a imagem
imagem = cv2.imread('caminho/para/imagem.jpg')

# Exibir a imagem
cv2.imshow('Imagem', imagem)
cv2.waitKey(0)
cv2.destroyAllWindows()