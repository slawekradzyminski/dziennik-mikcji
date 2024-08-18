import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

# Simplified column titles
columns_print = [
    "Godzina", 
    "Ilość \n wypitego \n płynu \n (ml)", 
    "Rodzaj \n wypitego \n płynu", 
    "Uczucie parcia \n na pęcherz \n (0-4)", 
    "Ilość \n oddanego \n moczu \n (ml)", 
    "Epizody \n nietrzymania \n moczu \n (mało, średnio, \n dużo)", 
    "Uwagi"
]

# Generate hours from 06:00 to 06:00 next day
hours = [f"{hour:02d}:00" for hour in range(6, 30)]
hours = [f"{int(hour.split(':')[0]) % 24:02d}:00" for hour in hours] + ["06:00"]

# Create initial empty dataframe
data = {col: [""] * 25 for col in columns_print}
data["Godzina"] = hours
df = pd.DataFrame(data)

# Creating the PDF
pdf_filename_new = "Dziennik_Mikcji_Pacjentka_New_Format.pdf"

with PdfPages(pdf_filename_new) as pdf:
    fig, ax = plt.subplots(figsize=(10, 12))  # Adjust the figure size as needed
    ax.axis('tight')
    ax.axis('off')
    
    # Table Title
    table_title_new = "Dziennik Mikcji, Pacjent/ka .................................. , Waga ............... , Wiek .................... , Data ......................"
    plt.text(0.5, 1.05, table_title_new, ha='center', fontsize=12, transform=ax.transAxes, fontname='Arial')
    
    # Create the table
    tbl = ax.table(cellText=df.values, colLabels=df.columns, cellLoc='center', loc='center')
    tbl.auto_set_font_size(False)
    tbl.set_fontsize(10)
    tbl.scale(1, 2)  # Adjust table size and increase row height

    # Adjust the row height and bold the headers
    for key, cell in tbl.get_celld().items():
        if key[0] == 0:  # this is the header row
            cell.set_height(0.15)
            cell.set_text_props(weight='bold', fontname='Arial')
    
    pdf.savefig(fig, bbox_inches='tight', pad_inches=0.2)
    plt.close()

print(f"PDF generated: {pdf_filename_new}")