import os
import tkinter as tk
from tkinter import filedialog, messagebox, Text
from analise import importar_arquivo, analisar_texto, gerar_relatorio

class AplicativoAnalisador:
    def __init__(self, master):
        self.master = master
        master.title("Analisador de Jurisprudência")

        self.label = tk.Label(master, text="Selecione um arquivo para análise:")
        self.label.pack()

        self.analisar_button = tk.Button(master, text="Analisar", command=self.analisar)
        self.analisar_button.pack()

        self.resultado_text = Text(master, height=15, width=50)
        self.resultado_text.pack()

    def analisar(self):
        caminho = filedialog.askopenfilename(filetypes=[("Arquivos PDF", "*.pdf"),
                                                        ("Arquivos DOCX", "*.docx"),
                                                        ("Arquivos TXT", "*.txt")])
        if caminho:
            try:
                texto = importar_arquivo(caminho)
                erros = analisar_texto(texto)
                self.resultado_text.delete(1.0, tk.END)  # Limpa a área de texto
                if erros:
                    resultado = "Erros encontrados:\n"
                    for erro, sugestoes in erros.items():
                        resultado += f"Erro: {erro} | Sugestões: {', '.join(sugestoes)}\n"
                else:
                    resultado = "Nenhum erro encontrado."
                self.resultado_text.insert(tk.END, resultado)
                gerar_relatorio(erros, 'relatorio.pdf')
                messagebox.showinfo("Sucesso", "Análise concluída. Relatório gerado como 'relatorio.pdf'.")
            except Exception as e:
                messagebox.showerror("Erro", f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = AplicativoAnalisador(root)
    root.mainloop()


