from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def initFun():
    #Memberihkan layar dan memberikan warna
    glClearColor(1.0,1.0,1.0,0.0)
    #Menentukan warna
    glColor3f(1.0, 1.0, 1.0)
    #Spesifikasikan diameter dari pixel yang akan digammbar
    glPointSize(10.0)
    #Set origin dari grid dan ukurannya 100 x 100
    gluOrtho2D(0,100,0,100)
    
def AlgBrasenhgam():
    #tentukan titik awal dan akhir
    x1 = 4
    y1 = 1
    x2 = 14
    y2 = 8
    x = x1
    y = y1

    #hitung dx dan dy
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    
    #hitung p 
    p = 2 * dy - dx
    duady = 2 * dy
    duadydx = 2 * (dy - dx)
    
    #tentukan titik awal dan akhir
    if (x1 > x2):
        x = x2
        y = y2
        xend = x1
    else:
        x = x1
        y = y1
        xend = x2
    

    #gambar titik awal
    glBegin(GL_POINTS)
    glVertex2i(x, y)

    #perulangan untuk menggambar titik-titik 
    while (x < xend):
        x = x+1
        if (p < 0):
            p += duady
        else:
            if (y1 > y2):
                y = y-1
            else:
                y = y+1
            p += duadydx
        glVertex2i(x, y)

    glEnd()
    glFlush()

if __name__ == '__main__':
    glutInit()
    #inisialisasi ukuran layar glut
    glutInitWindowSize(640,480)
    glutCreateWindow("Komputer Grafik - brasenham")
    glutInitDisplayMode(GLUT_RGB)
    glutDisplayFunc(AlgBrasenhgam)
    initFun()
    glutMainLoop()