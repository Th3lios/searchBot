def get_string(img_path):

    # Si no hay imagen en el desktop, termina el loop
    if(img_path == "/Users/macbook/Desktop/Elias"):
        print("No hay imagen disponible")
        exit(1)

    # Read image with opencv
    img = cv2.imread(img_path)

    # Convert to gray
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply dilation and erosion to remove some noise
    kernel = np.ones((1, 1), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1)
    img = cv2.erode(img, kernel, iterations=1)

    # Write image after removed noise
    cv2.imwrite(src_path + r"/removed_noise.png", img)

    #  Apply threshold to get image with only black and white
    img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)

    # Write the image after apply opencv to do some ...
    cv2.imwrite(src_path + r"/thres.png", img)

    # Recognize text with tesseract for python
    a = Image.open(src_path + r"/thres.png")
    result = image_to_string(a, lang='eng')
    #   list_of_word = re.findall(r'\w+', result)

    #print(result)
    string2 = []
    for i in result.split("\n\n"):
        string2.append(i.replace('\n', ' '))

    return string2