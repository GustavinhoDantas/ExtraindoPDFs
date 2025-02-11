#biblioteca que faz o processo 
from pypdf import PdfReader, PdfWriter

# Caminho do arquivo de entrada e saída
input_pdf_path = ''#pegue o caminho completo como, r"C:\Users\Eu\Documents\PDF\PDF_Completo.pdf"
output_pdf_path = ''#pcoloque o caminho completo como, r"C:\Users\Eu\Documents\PDF\PDF_Estraido.pdf"

# Lista das páginas que deseja extrair (Python conta do 0, então subtraímos 1)
paginas_desejadas = []

# Abrir o PDF original
with open(input_pdf_path, "rb") as input_pdf:
    reader = PdfReader(input_pdf)
    writer = PdfWriter()
    
    # Adicionar as páginas desejadas ao novo PDF
    for page_num in paginas_desejadas:
        if page_num <= len(reader.pages):  # Verifica se a página existe no documento
            writer.add_page(reader.pages[page_num - 1])  # Ajustando para indexação Python
        else:
            print(f"Aviso: Página {page_num} não existe no documento.")

    # Salvar o novo PDF
    with open(output_pdf_path, "wb") as output_pdf:
        writer.write(output_pdf)

print("PDF criado com sucesso:", output_pdf_path)
