
import numpy as np
import cv2


def main() :
    H,W = 600,1000
    L = 400
    R = 20
    angle = np.pi//2
    aVel = 0
    aAcc = 0

    origin = [W//2,0]
    bob = [W//2,L]

    while True:
        img = np.zeros((H,W), np.uint8)
        
        bob[0] = int(origin[0] + L*np.sin(angle))
        bob[1] = int(origin[1] + L*np.cos(angle))

        cv2.circle(img, (bob[0],bob[1],), R, (255,255,255),1)
        cv2.line(img,(origin[0],origin[1]),(bob[0],bob[1]),(255,255,255),1)

        cv2.imshow('pendulum', img)

        aAcc = -1*0.8/L*np.sin(angle)

        angle = angle + aVel
        aVel = aVel + aAcc

        aVel = aVel*0.99

        ch = cv2.waitKey(1)
        if ch == 27:
            break



if __name__ == '__main__':
    main()

cv2.destroyAllWindows()
cv2.waitKey(1)