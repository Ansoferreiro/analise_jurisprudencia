from fpdf import FPDF

def gerar_relatorio(erros, caminho_saida):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt="Relatório de Erros Ortográficos", ln=True, align='C')
    pdf.ln(10)

    for erro, sugestoes in erros.items():
        pdf.cell(0, 10, txt=f"Erro: {erro} | Sugestões: {', '.join(sugestoes)}", ln=True)

    pdf.output(caminho_saida)

