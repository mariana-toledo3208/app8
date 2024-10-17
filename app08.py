import flet as ft


def main(page: ft.Page):
#establecer tamaño de pantalla

    page.window_width=800
    page.window_height=800
    
    page.bgcolor="black"
    page.title="Mictlan"
    page.fgcolor="gray"
    
    Intro=ft.audio(src="Intro.mp3",volumen=1,balace=0)
    page.owertay.append(Intro)  
    
    Primernivel=ft.audio(src="Primer_Nivel.mp3",volumen=1,balance=0)
    
    segundonivel=ft.audio(src="Segundo_Nivel.mp3",volumen=1,balance=0)

    Tercernivel=ft.audio(src="Tercer_Nivel.mp3",volumen=1,balance=0)

    Cuartonivel=ft.audio(src="Cuarto_Nivel.mp3",volumen=1,balance=0)

    Quintonivel=ft.audio(src="Quinto_Nivel.mp3",volumen=1,balance=0)

    Sextonivel=ft.audio(src="Sexto_Nivel.mp3",volumen=1,balance=0)
    
    Septimonivel=ft.audio(src="Septimo_Nivel.mp3",volumen=1,balance=0)
    
    Octavonivel=ft.audio(src="Octavo_Nivel.mp3",volumen=1,balance=0)
    
    Novenonivel=ft.audio(src="Noveno_nivel.mp3",volumen=1,balance=0)


ft.app(main)
