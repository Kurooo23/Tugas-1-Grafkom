from OpenGL.GL import glClear, glClearColor, glColor3f, glBegin, glEnd, glVertex2f, \
                      glFlush, glPointSize, glLineWidth, GL_COLOR_BUFFER_BIT, \
                      GL_POINTS, GL_PROJECTION, glMatrixMode, \
                      glLoadIdentity, GL_LINES, GL_LINE_LOOP

from OpenGL.GLUT import glutInit, glutInitDisplayMode, glutInitWindowSize, \
                         glutInitWindowPosition, glutCreateWindow, glutDisplayFunc, \
                         glutMainLoop, GLUT_SINGLE, GLUT_RGB

from OpenGL.GLU import gluOrtho2D

# Titik-titik prisma segitiga 2D
points = [
    (100.0, 150.0),   # A (Titik kiri bawah gedung satu)
    (150.0, 150.0),   # B (Titik kanan bawah gedung satu)
    (175.0, 175.0),   # C (Titik samping bawah gedung satu)
    (100.0, 350.0),   # D (Titik kiri atas gedung satu)
    (150.0, 350.0),   # E (Titik kanan atas gedung satu)
    (175.0, 375.0),   # F (Titik samping atas gedung satu)
    (137.5, 450.0),   # G (Titik puncak gedung satu)
    
    (200.0, 175.0),   # H (Titik samping bawah gedung dua)
    (225.0, 150.0),   # I (Titik kiri bawah gedung dua)
    (275.0, 150.0),   # J (Titik kanan bawah gedung dua)
    (200.0, 375.0),   # K (Titik samping atas gedung dua)
    (225.0, 350.0),   # L (Titik kiri atas gedung dua)
    (275.0, 350.0),   # M (Titik kanan atas gedung satu)
    (237.5, 450.0),   # N (Titik puncak gedung dua)
    
    (162.5, 240.0),   # O (Titik bawah penghubung gedung satu)
    (162.5, 260.0),   # P (Titik atas penghubung gedung satu)
    (212.5, 240.0),   # Q (Titik bawah penghubung gedung dua)
    (212.5, 260.0)    # R (Titik  atas penghubung gedung dua)
]

def draw():
    glClear(GL_COLOR_BUFFER_BIT)  # Bersihkan layar

    # Gambar outline segitiga depan (tanpa warna)
    glColor3f(0.0, 0.0, 0.0)  # Warna hitam untuk garis
    glLineWidth(2)
    glBegin(GL_LINE_LOOP)
    glVertex2f(*points[0])  # A
    glVertex2f(*points[1])  # B
    glVertex2f(*points[2])  # C
    glVertex2f(*points[3])  # D
    glVertex2f(*points[4])  # E
    glVertex2f(*points[5])  # F
    glVertex2f(*points[6])  # G
    glVertex2f(*points[7])  # H
    glVertex2f(*points[8])  # I
    glVertex2f(*points[9])  # J
    glVertex2f(*points[10]) # K
    glVertex2f(*points[11]) # L
    glVertex2f(*points[12]) # M
    glVertex2f(*points[13]) # N
    glVertex2f(*points[14]) # O
    glVertex2f(*points[15]) # P
    glVertex2f(*points[16]) # Q
    glVertex2f(*points[17]) # R
    glEnd()

    # Gambar titik-titik (Merah, ukuran 8)
    glColor3f(1.0, 0.0, 0.0)  # Warna merah
    glPointSize(8)
    glBegin(GL_POINTS)
    for x, y in points:
        glVertex2f(x, y)
    glEnd()

    # Gambar garis penghubung (putih)
    glColor3f(1.0, 1.0, 1.0)  # Warna putih
    glLineWidth(2)
    glBegin(GL_LINES)
    glVertex2f(*points[0]); glVertex2f(*points[6])    # A ke G
    glVertex2f(*points[2]); glVertex2f(*points[3])    # C ke D
    glVertex2f(*points[0]); glVertex2f(*points[17])   # A ke R
    glVertex2f(*points[6]); glVertex2f(*points[7])    # G ke H
    glVertex2f(*points[13]); glVertex2f(*points[14])  # N ke O
    glVertex2f(*points[9]); glVertex2f(*points[10])   # J ke K
    glVertex2f(*points[15]); glVertex2f(*points[16])  # P ke Q
    
    glEnd()

    glFlush()  # Pastikan semua perintah OpenGL dieksekusi
    
    # Gambar garis penghubung  (Hitam)
    glColor3f(0.0, 0.0, 0.0)  # Warna hitam
    glLineWidth(3)
    glBegin(GL_LINES)
    glVertex2f(*points[0]); glVertex2f(*points[1])  # A ke B
    glVertex2f(*points[1]); glVertex2f(*points[2])  # B ke C
    glVertex2f(*points[0]); glVertex2f(*points[3])  # A ke D
    glVertex2f(*points[1]); glVertex2f(*points[4])  # B ke E
    glVertex2f(*points[2]); glVertex2f(*points[5])  # C ke F
    glVertex2f(*points[3]); glVertex2f(*points[4])  # D ke E
    glVertex2f(*points[4]); glVertex2f(*points[5])  # E ke F
    glVertex2f(*points[3]); glVertex2f(*points[6])  # D ke G
    glVertex2f(*points[4]); glVertex2f(*points[6])  # E ke G
    glVertex2f(*points[5]); glVertex2f(*points[6])  # F ke G
    
    glVertex2f(*points[7]); glVertex2f(*points[8])    # H ke I
    glVertex2f(*points[8]); glVertex2f(*points[9])    # I ke J
    glVertex2f(*points[7]); glVertex2f(*points[10])   # H ke K
    glVertex2f(*points[8]); glVertex2f(*points[11])   # I ke L
    glVertex2f(*points[9]); glVertex2f(*points[12])   # J ke M
    glVertex2f(*points[10]); glVertex2f(*points[11])  # K ke L
    glVertex2f(*points[11]); glVertex2f(*points[12])  # L ke M
    glVertex2f(*points[10]); glVertex2f(*points[13])  # K ke N
    glVertex2f(*points[11]); glVertex2f(*points[13])  # L ke N
    glVertex2f(*points[12]); glVertex2f(*points[13])  # M ke N
    
    glVertex2f(*points[14]); glVertex2f(*points[16])  # O ke Q
    glVertex2f(*points[15]); glVertex2f(*points[17])  # P ke R
    glEnd()

    glFlush()  # Pastikan semua perintah OpenGL dieksekusi
    

def init():
    glClearColor(1.0, 1.0, 1.0, 1.0)  # Latar belakang putih
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, 500, 0, 500)  # Atur sistem koordinat

def main():
    glutInit()
    glutInitDisplayMode(int(GLUT_SINGLE) | int(GLUT_RGB))
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Gedung")
    
    init()
    glutDisplayFunc(draw)
    glutMainLoop()

if __name__ == "__main__":
    main()
