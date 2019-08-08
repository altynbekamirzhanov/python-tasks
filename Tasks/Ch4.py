from math import *
from turtle import *
def polyline (n, length, a) :
    for i in range (n) :
        fd( length )
        lt( a )

def arc (r, a) :
    arc_len = 2 * pi * r * abs(a) / 360
    n = int ( arc_len / 4 ) + 1
    s_len = arc_len / n
    s_angle = float (a) / n
    lt( s_angle / 2 )
    polyline (n, s_len, s_angle)
    rt (s_angle / 2)

def petal (r, a) :
    for i in range (2):
        arc (r, a)
        lt( 180 - a )

def flower (n, r, a) :
    for i in range (n) :
        petal (r, a)
        lt( 360 / n )

def p4_2a():
    flower (7, 60, 60)

def p4_2b() :
    flower (10, 40, 80)

def p4_2c() :
    flower (20, 140, 20)

def p4_3 (n, length) :
    for i in range (n) :
        fd(length)
        a = 90 + 180 / n
        lt( a )
        b = 2 * length * cos( (90 - 180 / n) * pi /180) 
        fd( b )
        lt( a )
        fd( length )
        lt( 180 - 360 / n )
        rt( 360 / n )
    pu()
    fd(60)
    pd()

def letters( word ) :
    word = word . lower ( )
    shape ( 'turtle' )
    pencolor ( 'red' )
    pensize ( '5' )
    pu( )
    bk( 300 )
    pd( )
    def A( ) :
        lt( 60 )
        fd( 60 )
        rt( 120 )
        fd( 30 )
        rt( 120 )
        fd( 30 )
        rt( 180 )
        fd( 30 )
        rt( 60 )
        fd( 30 )
        lt( 60 )
    def B( ) :
        fd( 5 )
        circle( 14, 180 )
        fd( 5 )
        rt(180)
        fd( 5 )
        circle( 11.9807621, 180 )
        fd( 5 )
        lt( 90 )
        fd( 51.9615242 )
        lt( 90 )
        pu( )
        fd( 19 )
    def C( ) :
        pu( )
        fd( 25.9807621 )
        lt( 90 )
        fd( 47.9615242 )
        pd( )
        fd( 4 )
        lt(90)
        circle( 25.9807621, 180 )
        lt( 90 )
        fd( 4 )
        pu( )
        bk ( 4 )
        rt( 90 )
    def D( ) :
        fd( 4 )
        circle( 25.9807621, 180 )
        fd( 4 )
        bk( 4 )
        lt( 90 )
        fd( 51.9615242 )
        lt( 90 )
        pu()
        fd( 25.9807621)
    def E( ) :
        lt( 180 )
        bk( 30 )
        for i in range( 2 ) :
            fd( 30 )
            rt( 90 )
            fd( 25.9807621 )
            lt( 90 )
            bk( 30 )
        pu( )
        lt( 90 )
        fd( 51.9615242 )
        lt( 90 )
    def F( ) :
        lt( 90 )
        fd( 27.9807621 )
        rt( 90 )
        fd( 18 )
        bk( 18 )
        lt( 90 )
        fd( 23.9807621 )
        rt( 90 )
        fd( 30 )
        pu( )
        rt( 90 )
        fd( 51.9615242 )
        lt( 90 )
    def G( ) :
        pu( )
        fd( 25.9807621 )
        lt( 90 )
        fd( 38.97114315 )
        pd( )
        circle( 12.99038105, 180 )
        fd( 25.9807621 )
        circle( 12.99038105, 180 )
        lt( 90 )
        fd( 15 )
        bk( 15 )
        lt( 90 )
        pu( )
        fd( 12.99038105 )
        lt( 90 )
    def H( ) :
        lt( 90 )
        fd( 51.9615242 )
        bk( 25.9807621 )
        rt( 90 )
        fd( 30 )
        lt( 90 )
        fd( 25.9807621 )
        bk( 51.9615242 )
        rt( 90 )
    def I( ) :
        fd( 30 )
        bk( 15 )
        lt( 90 )
        fd( 51.9615242 )
        rt( 90 )
        bk( 15 )
        fd( 30 )
        rt( 90 )
        pu( )
        fd( 51.9615242 )
        lt( 90 )
    def J( ) :
        pu( )
        rt( 90 )
        bk( 10 )
        pd( )
        circle( 10, 180 )
        fd( 41.9615242 )
        rt( 90 )
        bk( 5 )
        fd( 10 )
        rt( 90 )
        pu( )
        fd( 51.9615242 )
        lt( 90 )
    def K( ) :
        lt( 90 )
        fd( 51.9615242 )
        bk( 25.9807621 )
        rt( 45 )
        fd( 36.7423461 )
        bk( 32.7423461 )
        rt( 90 )
        fd( 39.5707732 )
        lt( 45 )
    def L( ) :
        lt( 90 )
        fd( 51.9615242 )
        bk( 51.9615242 )
        rt( 90 )
        fd( 25.9807621 )
    def M( ) :
        lt( 90 )
        fd( 51.9615242 )
        rt( 135 )
        fd( 33.3944963 )
        lt( 90 )
        fd( 33.3944963 )
        rt( 135 )
        fd( 51.9615242 )
        lt( 90 )
    def N( ) :
        lt( 90 )
        fd( 51.9615242 )
        rt( 150 )
        fd( 60 )
        lt( 150 )
        fd( 51.9615242 )
        bk( 51.9615242 )
        rt( 90 )
    def O( ) :
        pu( )
        rt( 90 )
        bk( 30.9807621 )
        pd( )
        for i in range( 2 ) :
            fd( 10 )
            circle( 20.9807621, 180 )
        pu( )
        fd( 10 )
        circle( 20.9807621, 90 )
        fd ( 20.9807621 )
    def P( ) :
        lt( 90 )
        fd( 19.9807621 )
        rt( 90 )
        fd( 5 )
        circle( 15.99038105, 180 )
        fd( 5 )
        lt( 90 )
        fd( 51.9615242 )
        lt( 90 )
        pu( )
        fd( 20.99038105 )
    def Q( ) :
        pu( )
        rt( 90 )
        bk( 30.9807621 )
        pd( )
        for i in range( 2 ) :
            fd( 10 )
            circle( 20.9807621, 180 )
        pu( )
        fd( 10 )
        circle( 20.9807621, 90 )
        rt( 90 )
        bk( 15.9807621 )
        pd( )
        circle( 15.9807621, 90 )
        fd( 5 )
    def R( ) :
        lt( 90 )
        fd( 19.9807621 )
        rt( 90 )
        fd( 5 )
        circle( 15.99038105, 180 )
        fd( 5 )
        lt( 90 )
        fd( 31.9807621 )
        lt( 39 )
        fd( 25.5914662 )
        lt( 51 )
        pu( )
        fd( 5 )
    def S( ) :
        pu( )
        rt( 100 )
        bk( 13.99083105 )
        pd( )
        circle( 13.99083105, 270 )
        rt( 180 )
        circle( 13.99083105, -270 )
        lt( 190 )
        pu( )
        fd( 36.9711432 )
        lt( 90 )
    def T( ) :
        pu( )
        fd( 20 )
        lt( 90 )
        pd( )
        fd( 51.9615242 )
        rt( 90 )
        bk( 20 )
        lt( 90 )
        bk(10)
        fd(10)
        rt( 90 )
        fd( 40 )
        rt( 90 )
        fd( 10 )
        pu()
        fd( 41.9615242 )
        lt( 90 )
    def U( ) :
        rt( 90 )
        pu( )
        bk( 51.9615242 )
        pd( )
        fd( 38.9711432 )
        circle( 12.99083105, 180 )
        fd( 38.9711432 )
        bk( 51.9615242 )
        rt( 90 )
    def V( ) :
        pu( )
        fd( 30.9807621 )
        lt( 120 )
        pd( )
        fd( 58.0947502 )
        lt( 60 )
        fd( 5 )
        bk( 10 )
        pu( )
        bk( 44.9615242 )
        pd( )
        bk( 10 )
        fd( 5 )
        rt( 120 )
        bk( 58.0947502 )
        rt( 60 )
        pu( )
        fd( 30.9807621 )
    def W( ) :
        pu( )
        fd( 5 )
        lt( 90 )
        fd( 51.9615242 )
        rt( 90 )
        pd( )
        bk( 5 )
        fd( 10 )
        bk( 5 )
        lt( 90 )
        bk( 51.9615242 )
        rt( 35 )
        fd( 25 )
        lt( 70 )
        bk( 25 )
        rt( 35 )
        fd( 51.9615242 )
        rt( 90 )
        bk( 5 )
        fd( 10 )
        lt( 90 )
        pu( )
        bk( 51.9615242 )
        rt( 90 )
    def X( ):
        fd( 10 )
        bk( 5 )
        lt( 60 )
        fd( 60 )
        rt( 60 )
        fd( 5 )
        bk( 10 )
        pu( )
        bk( 20 )
        pd( )
        bk( 10 )
        fd( 5 )
        rt( 60 )
        fd( 60 )
        lt( 60 )
        bk( 5 )
        fd( 10 )
    def Y( ) :
        pu( )
        fd( 20 )
        pd( )
        lt( 90 )
        fd( 25.9807621 )
        lt( 38 )
        fd( 32.7871926 )
        bk( 32.7871926 )
        rt( 76 )
        fd( 32.7871926 )
        lt( 38 )
        pu( )
        bk( 51.9615242 )
        rt( 90 )
    def Z( ) :
        pu( )
        lt( 90 )
        fd( 51.9615242)
        pd( )
        rt( 90 )
        fd( 40 )
        rt( 127.58 )
        fd( 65.5743852 )
        lt( 127.58 )
        fd( 40 )
    def spa( ) :
        pu( )
        fd( 10 )
        pd( )
    for i in word :
        if i=='a':
            A( ), spa( )
        elif i=='b':
            B( ), spa( )
        elif i=='c':
            C( ), spa( )
        elif i=='d':
            D( ), spa( )
        elif i=='e':
            E( ), spa( )
        elif i=='f':
            F( ), spa( )
        elif i=='g':
            G( ), spa( )
        elif i=='h':
            H( ), spa( )
        elif i=='i':
            I( ), spa( )
        elif i=='j':
            J( ), spa( )
        elif i=='k':
            K( ), spa( )
        elif i=='l':
            L( ), spa( )
        elif i=='m':
            M( ), spa( )
        elif i=='n':
            N( ), spa( )
        elif i=='o':
            O( ), spa( )
        elif i=='p':
            P( ), spa( )
        elif i=='q':
            Q( ), spa( )
        elif i=='r':
            R( ), spa( )
        elif i=='s':
            S( ), spa( )
        elif i=='t':
            T( ), spa( )
        elif i=='u':
            U( ), spa( )
        elif i=='v':
            V( ), spa( )
        elif i=='w':
            W( ), spa( )
        elif i=='x':
            X( ), spa( )
        elif i=='y':
            Y( ), spa( )
        elif i=='z':
            Z( ), spa( )
        elif i==' ':
            pu( )
            fd( 30 )
            pd( )
        elif i=='-':
            pu( )
            lt( 90 )
            fd( 25.9807621 )
            rt( 90 )
            pd( )
            fd( 20 )
            pu( )
            lt( 90 )
            bk( 25.9807621 )
            rt( 90 )
            pd( )
            spa( )
