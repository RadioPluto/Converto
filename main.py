import flet as ft
 

#Main runnning funtion
def main(page: ft.Page):
    page.title = "Converto"
    #page dimensions
    page.width = 500
    page.height = 500
    page.window.resizeable = True
    background_container = ft.Container(
        width = 450,
        height = 450,
        bgcolor = '#041955',
        border_radius = 35,
        blur = 10
    )
    page.add(background_container)
    #Result
    result = ft.Text(value = "0")


ft.run(main)

