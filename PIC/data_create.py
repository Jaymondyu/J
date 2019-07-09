
import cv2
import os


def generate(dirname):
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
    # 带眼镜的时候可以用下面这个
    # eye_cascade = cv2.CascadeClassifier('D:/opencv/sources/data/haarcascades/haarcascade_eye_tree_eyeglasses.xml')

    # 创建目录
    if (not os.path.isdir(dirname)):
        os.makedirs(dirname)

    # 打开摄像头进行人脸图像采集
    camera = cv2.VideoCapture(0)
    count = 0
    while (True):
        ret, frame = camera.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray,1.3,5)
        for (x, y, w, h) in faces:
            img = cv2.rectangle(frame,(x,y),(x+w, y+h),(255,0,0), 2)
            # 重设置图像尺寸
            200 * 200
            f = cv2.resize(gray[y:y+h,x:x+w], (200, 200))
            cv2.imwrite(dirname + '/%s.pgm' % str(count), f)
            print(count)
            count += 1

        cv2.imshow("camera", frame)
        if cv2.waitKey(100) & 0xff == ord("q"):
            break

        # 下面是你想要多少张图片就停止
        if count > 20:
            break


    camera.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    generate("C:/Users/Administrator/Desktop/mygit/J/PIC/cam_data")
    # 你生成的图片放在的电脑中的地方
