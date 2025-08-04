import ttkbootstrap as ttk
import customtkinter as ctk
import tkinter as tk
from functions import *
import customtkinter as ctk


DADOS_CONEXAO = ("DRIVER={MySQL ODBC 9.4 Unicode Driver};"
                 "SERVER=localhost;"
                 "DATABASE=db_exemplo;"
                 "UID=root;"
                 "PWD=root")


conexao = conectar_bd(DADOS_CONEXAO)
cursor = criar_cursor(conexao)

def popup_course():
    popup = ctk.CTkToplevel(window, fg_color="#FFFFFF")  # Fundo branco

    # Centralizar na tela
    popup_width = 400
    popup_height = 300
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = int((screen_width / 2) - (popup_width / 2))
    y = int((screen_height / 2) - (popup_height / 2))
    popup.geometry(f"{popup_width}x{popup_height}+{x}+{y}")
    popup.resizable(False, False)
    popup.overrideredirect(True)

    # Frame principal com bordas arredondadas
    frame = ctk.CTkFrame(popup, fg_color="#FFFFFF", corner_radius=12, border_color="#E5E7EB", border_width=1)
    frame.pack(expand=True, fill="both")
    frame.columnconfigure(0, weight=1)

    # Título
    title = ctk.CTkLabel(frame, text="Adicionar Curso", font=("Inter", 20, "bold"), text_color="#111827")
    title.grid(row=0, column=0, sticky="w", padx=20, pady=(15, 5))

    # Botão fechar
    close_button = ctk.CTkButton(
        frame,
        text="✕",
        width=25,
        height=25,
        font=("Inter", 14),
        fg_color="transparent",
        hover_color="#F1F5F9",
        text_color="#6B7280",
        command=popup.destroy
    )
    close_button.place(relx=1.0, rely=0.0, anchor="ne", x=-10, y=10)

    # Inputs
    entry_nome = ctk.CTkEntry(frame, placeholder_text="Nome Curso", height=40, corner_radius=6)
    entry_nome.grid(row=1, column=0, padx=20, pady=(15, 5), sticky="ew")

    entry_preco = ctk.CTkEntry(frame, placeholder_text="Preço", height=40, corner_radius=6)
    entry_preco.grid(row=2, column=0, padx=20, pady=5, sticky="ew")

    # Botão Salvar
    save_button = ctk.CTkButton(
        frame,
        text="Save",
        height=40,
        corner_radius=6,
        fg_color="#3B82F6",
        hover_color="#2563EB",
        text_color="white",
        command=lambda: adicionar_curso(cursor, entry_nome.get(), entry_preco.get(), var_cursos=var_cursos)
    )
    save_button.grid(row=4, column=0, padx=20, pady=(20, 8), sticky="ew")

    # Botão Cancelar
    cancel_button = ctk.CTkButton(
        frame,
        text="Cancel",
        height=40,
        corner_radius=6,
        fg_color="white",
        border_color="#D1D5DB",
        border_width=1,
        text_color="#6B7280",
        hover_color="#F9FAFB",
        command=popup.destroy
    )
    cancel_button.grid(row=5, column=0, padx=20, pady=(0, 20), sticky="ew")

    popup.grab_set()
    window.wait_window(popup)


def popup_student():
    popup = ctk.CTkToplevel(window, fg_color="#FFFFFF") 

    # Centralizar na tela
    popup_width = 400
    popup_height = 340
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = int((screen_width / 2) - (popup_width / 2))
    y = int((screen_height / 2) - (popup_height / 2))
    popup.geometry(f"{popup_width}x{popup_height}+{x}+{y}")
    popup.resizable(False, False)
    popup.overrideredirect(True)

    # Frame principal com bordas arredondadas
    frame = ctk.CTkFrame(popup, fg_color="#FFFFFF", corner_radius=12, border_color="#E5E7EB", border_width=1)
    frame.pack(expand=True, fill="both")
    frame.columnconfigure(0, weight=1)

    # Título
    title = ctk.CTkLabel(frame, text="Adicionar Estudante", font=("Inter", 20, "bold"), text_color="#111827")
    title.grid(row=0, column=0, sticky="w", padx=20, pady=(15, 5))

    # Botão fechar
    close_button = ctk.CTkButton(
        frame,
        text="✕",
        width=25,
        height=25,
        font=("Inter", 14),
        fg_color="transparent",
        hover_color="#F1F5F9",
        text_color="#6B7280",
        command=popup.destroy
    )
    close_button.place(relx=1.0, rely=0.0, anchor="ne", x=-10, y=10)

    # Inputs
    entry_name = ctk.CTkEntry(frame, placeholder_text="Nome Completo", height=40, corner_radius=6)
    entry_name.grid(row=1, column=0, padx=20, pady=(15, 5), sticky="ew")

    entry_email = ctk.CTkEntry(frame, placeholder_text="Email", height=40, corner_radius=6)
    entry_email.grid(row=2, column=0, padx=20, pady=5, sticky="ew")

    entry_nasc = ctk.CTkEntry(frame, placeholder_text="Data de Nascimento AAAA-MM-DD", height=40, corner_radius=6)
    entry_nasc.grid(row=3, column=0, padx=20, pady=5, sticky="ew")

    # Botão Salvar
    save_button = ctk.CTkButton(
        frame,
        text="Save",
        height=40,
        corner_radius=6,
        fg_color="#3B82F6",
        hover_color="#2563EB",
        text_color="white",
        command=lambda: adicionar_aluno(cursor, nome=entry_name.get(), email=entry_email.get(), dt_nascimento=entry_nasc.get(), var_alunos=var_alunos)
    )
    save_button.grid(row=5, column=0, padx=20, pady=(20, 8), sticky="ew")

    # Botão Cancelar
    cancel_button = ctk.CTkButton(
        frame,
        text="Cancel",
        height=40,
        corner_radius=6,
        fg_color="white",
        border_color="#D1D5DB",
        border_width=1,
        text_color="#6B7280",
        hover_color="#F9FAFB",
        command=popup.destroy
    )
    cancel_button.grid(row=6, column=0, padx=20, pady=(0, 20), sticky="ew")

    popup.grab_set()
    window.wait_window(popup)


def popup_enroll():
    popup = ctk.CTkToplevel(window, fg_color="#FFFFFF")  # Fundo branco

    # Centralizar na tela
    popup_width = 400
    popup_height = 340
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = int((screen_width / 2) - (popup_width / 2))
    y = int((screen_height / 2) - (popup_height / 2))
    popup.geometry(f"{popup_width}x{popup_height}+{x}+{y}")
    popup.resizable(False, False)
    popup.overrideredirect(True)

    # Frame principal com bordas arredondadas
    frame = ctk.CTkFrame(popup, fg_color="#FFFFFF", corner_radius=12, border_color="#E5E7EB", border_width=1)
    frame.pack(expand=True, fill="both")
    frame.columnconfigure(0, weight=1)

    # Título
    title = ctk.CTkLabel(frame, text="Adicionar Matrícula", font=("Inter", 20, "bold"), text_color="#111827")
    title.grid(row=0, column=0, sticky="w", padx=20, pady=(15, 5))

    # Botão fechar
    close_button = ctk.CTkButton(
        frame,
        text="✕",
        width=25,
        height=25,
        font=("Inter", 14),
        fg_color="transparent",
        hover_color="#F1F5F9",
        text_color="#6B7280",
        command=popup.destroy
    )
    close_button.place(relx=1.0, rely=0.0, anchor="ne", x=-10, y=10)

    # Inputs
    entry_id_aluno = ctk.CTkEntry(frame, placeholder_text="ID Aluno", height=40, corner_radius=6)
    entry_id_aluno.grid(row=1, column=0, padx=20, pady=(15, 5), sticky="ew")

    entry_id_curso = ctk.CTkEntry(frame, placeholder_text="ID Curso", height=40, corner_radius=6)
    entry_id_curso.grid(row=2, column=0, padx=20, pady=5, sticky="ew")

    dt_matricula = ctk.CTkEntry(frame, placeholder_text="Data Matrícula AAAA-MM-DD", height=40, corner_radius=6)
    dt_matricula.grid(row=3, column=0, padx=20, pady=5, sticky="ew")

    # Botão Salvar
    save_button = ctk.CTkButton(
        frame,
        text="Save",
        height=40,
        corner_radius=6,
        fg_color="#3B82F6",
        hover_color="#2563EB",
        text_color="white",
        command=lambda: adicionar_matricula(cursor, entry_id_aluno.get(), entry_id_curso.get(), dt_matricula.get(), var_matriculas=var_matriculas)
    )
    save_button.grid(row=5, column=0, padx=20, pady=(20, 8), sticky="ew")

    # Botão Cancelar
    cancel_button = ctk.CTkButton(
        frame,
        text="Cancel",
        height=40,
        corner_radius=6,
        fg_color="white",
        border_color="#D1D5DB",
        border_width=1,
        text_color="#6B7280",
        hover_color="#F9FAFB",
        command=popup.destroy
    )
    cancel_button.grid(row=6, column=0, padx=20, pady=(0, 20), sticky="ew")

    popup.grab_set()
    window.wait_window(popup)


window = ctk.CTk(fg_color="white")
window.minsize(400, 300)
window.columnconfigure(0, weight=1)
# security
window.bind("<Escape>", lambda event: window.quit())
window.attributes('-fullscreen', True)

top_frame = ctk.CTkFrame(window, fg_color="white")
top_frame.columnconfigure(0, weight=1) 

title = ttk.Label(top_frame, text="Sistema de Estudantes e Cursos", foreground='#1E293B', font="Inter 24 bold")
title.grid(row=0, column=0, sticky='ew', padx=250, pady=(25,3))

subtitle = ttk.Label(top_frame, text="Gerencie alunos, cursos e matrículas", foreground='#64748B', font="Inter 16")
subtitle.grid(row=1, column=0, sticky='ew', padx=250)

separator = ttk.Separator(top_frame, orient="horizontal")
separator.grid(row=2, column=0, sticky='ew', pady=20)
top_frame.grid(row=0, column=0, sticky="ew")


action_frame = ctk.CTkFrame(window, width=900, height=290, corner_radius=8, border_width=1, border_color='#E2E8F0', fg_color="white")
action_frame.grid_propagate(False)
action_frame.columnconfigure(0, weight=1)

action_label = ttk.Label(action_frame, text="Quick Actions", font="Inter 17", foreground="#1E293B")
action_label.grid(row=0, column=0, padx=25, pady=25, sticky="w")

btn_add_student = ctk.CTkButton(action_frame, text="Adicionar Estudante", corner_radius=4, fg_color='#3B82F6', font=("Inter", 16, "bold"), height=50, command=popup_student)
btn_add_student.grid(row=1, column=0, sticky="ew", padx=25)
btn_add_student.bind("<Enter>", lambda event: btn_add_student.configure(fg_color="#2563EB"))
btn_add_student.bind("<Leave>", lambda event: btn_add_student.configure(fg_color="#3B82F6"))

btn_add_course = ctk.CTkButton(action_frame, text="Adicionar Curso", corner_radius=4, fg_color='#10B981', font=("Inter", 16, "bold"), height=50, command=popup_course)
btn_add_course.grid(row=2, column=0, sticky="ew", padx=25, pady=15)
btn_add_course.bind("<Enter>", lambda event: btn_add_course.configure(fg_color="#0C5E42"))
btn_add_course.bind("<Leave>", lambda event: btn_add_course.configure(fg_color="#10B981"))

btn_enroll_student = ctk.CTkButton(action_frame, text="Matricular Aluno", corner_radius=4, fg_color='#8B5CF6', font=("Inter", 16, "bold"), height=50, command=popup_enroll)
btn_enroll_student.grid(row=3, column=0, sticky="ew", padx=25)
btn_enroll_student.bind("<Enter>", lambda event: btn_enroll_student.configure(fg_color="#5E40A5"))
btn_enroll_student.bind("<Leave>", lambda event: btn_enroll_student.configure(fg_color="#8B5CF6"))

action_frame.grid(row=1, column=0, pady=(100,0))

system_frame = ctk.CTkFrame(window, width=900, height=240, corner_radius=8, border_width=1, border_color='#E2E8F0', fg_color="white")
system_frame.grid_propagate(False)
system_frame.columnconfigure((0,1,2), weight=1)

system_label = ttk.Label(system_frame, text="Visão Geral", font="Inter 17", foreground="#1E293B")
system_label.grid(row=0, column=0, padx=25, pady=25, sticky="w")

frame_student = ctk.CTkFrame(system_frame, fg_color="#E9E9E9", width=200, height=100)
frame_student.grid_propagate(False)
frame_student.grid(row=1, column=0, padx=25)
frame_student.columnconfigure(0, weight=1)

alunos = consultar(cursor, 'alunos')
var_alunos = tk.IntVar(value=len(alunos))

num_student = ctk.CTkLabel(frame_student, font=("Inter", 20, "bold"), text_color='#3B82F6', textvariable=var_alunos)
num_student.grid(column=0, row=0, sticky="nsew", pady=(23,0))

label_student = ctk.CTkLabel(frame_student, text="Estudantes", text_color='#64748B', font=('Inter', 12))
label_student.grid(row=1, column=0, sticky='nsew')

frame_course = ctk.CTkFrame(system_frame, fg_color="#E9E9E9", width=200, height=100)
frame_course.grid_propagate(False)
frame_course.grid(row=1, column=1)
frame_course.columnconfigure(0, weight=1)

cursos = consultar(cursor, 'cursos')
var_cursos = tk.IntVar(value=len(cursos))

num_courses = ctk.CTkLabel(frame_course, text=len(cursos), font=("Inter", 20, "bold"), text_color='#10B981', textvariable=var_cursos)
num_courses.grid(column=0, row=0, sticky="nsew", pady=(23,0))

label_courses = ctk.CTkLabel(frame_course, text="Cursos", text_color='#64748B', font=('Inter', 12))
label_courses.grid(row=1, column=0, sticky='nsew')

frame_enroll = ctk.CTkFrame(system_frame, fg_color="#E9E9E9", width=200, height=100)
frame_enroll.grid_propagate(False)
frame_enroll.grid(row=1, column=2, padx=25)
frame_enroll.columnconfigure(0, weight=1)

matriculas = consultar(cursor, 'matriculas')
var_matriculas = tk.IntVar(value=len(matriculas))

num_enroll = ctk.CTkLabel(frame_enroll, text=len(matriculas), font=("Inter", 20, "bold"), text_color='#8B5CF6', textvariable=var_matriculas)
num_enroll.grid(column=0, row=0, sticky="nsew", pady=(23,0))

label_enroll = ctk.CTkLabel(frame_enroll, text="Matrículas", text_color='#64748B', font=('Inter', 12))
label_enroll.grid(row=1, column=0, sticky='nsew')

system_frame.grid(row=2, column=0, pady=(120,0))

window.mainloop()

fechar_conexao(cursor, conexao)
