from tkinter import *
from tkinter import ttk
from tkinter import filedialog  # Import filedialog for saving files
from tkinter import Text  # Import Text widget for the bill area
from tkinter import PhotoImage  # Import PhotoImage for displaying images
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

class Medicines:
    def __init__(self, root, medicines):
        self.root = root
        self.root.geometry("1100x700")
        self.root.title("Billing Software")
        bg_color = "#badc57"
        title = Label(self.root, text="Medicines", font=('times new roman', 30, 'bold'), pady=2, bd=12,
                      bg="#008080", fg="Black", relief=GROOVE)
        title.pack(fill=X)

        self.medical_price = StringVar()
        self.medical_tax = StringVar()

        F5 = Frame(self.root, bd=10, relief=GROOVE)
        F5.place(x=725, y=75, width=380, height=500)

        bill_title = Label(F5, text="Bill Area", font=('times new roman', 15, 'bold'), bd=7, relief=GROOVE)
        bill_title.pack(fill=X)
        scroll_y = Scrollbar(F5, orient=VERTICAL)
        self.txtarea = Text(F5, yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH, expand=1)

        F6 = LabelFrame(self.root, text="Bill Menu", font=('times new roman', 15, 'bold'), bd=10, fg="Black",
                        bg="#008080")
        F6.place(x=0, y=570, width=1100, height=130)

        m1_lbl = Label(F6, text="Total Medicine Price", font=('times new roman', 14, 'bold'), bg='teal', fg="White")
        m1_lbl.grid(row=0, column=0, padx=20, pady=10, sticky="w")
        m1_txt = Entry(F6, width=18, textvariable=self.medical_price, font=('times new roman', 10, 'bold'), bd=7,
                       relief=SUNKEN)
        m1_txt.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        c1_lbl = Label(F6, text="Medicine Tax", font=('times new roman', 14, 'bold'), bg='teal', fg="White")
        c1_lbl.grid(row=1, column=0, padx=20, pady=10, sticky="w")
        c1_txt = Entry(F6, width=18, textvariable=self.medical_tax, font=('times new roman', 10, 'bold'), bd=7,
                       relief=SUNKEN)
        c1_txt.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        self.category_frames = []

        F7 = Frame(self.root, bd=10, relief=GROOVE)
        F7.place(x=0, y=75, width=720, height=495)

        scroll_frame_title = Label(F7, text="Categories", font=('times new roman', 15, 'bold'), bd=7, relief=GROOVE)
        scroll_frame_title.pack(fill=X)

        canvas = Canvas(F7)
        canvas.pack(side=LEFT, fill=BOTH, expand=1)

        category_frame = Frame(canvas)
        category_frame.pack(fill=X)

        style = ttk.Style()
        style.configure("Horizontal.TScrollbar", width=30)

        scroll_x = ttk.Scrollbar(F7, orient=HORIZONTAL, command=canvas.xview, style="Horizontal.TScrollbar")
        scroll_x.pack(side=BOTTOM, fill=X)
        canvas.configure(xscrollcommand=scroll_x.set)

        category_frame = Frame(canvas)
        canvas.create_window((0, 0), window=category_frame, anchor='nw')

        scroll_y2 = Scrollbar(F7, orient=VERTICAL, command=canvas.yview)
        scroll_y2.pack(side=RIGHT, fill=Y)
        canvas.configure(yscrollcommand=scroll_y2.set)

        self.quantity_entries = []
        self.medicine_prices = {
            "Paracetamol": 5,
            "Aspirin": 8,
            "Ibuprofen": 6,
            "Acetaminophen": 7,
            "Cetirizine": 4,
            "Loratadine": 6,
            "Diphenhydramine": 7,
            "Fexofenadine": 5,
            "Pseudoephedrine": 6,
            "Dextromethorphan": 5,
            "Phenylephrine": 7,
            "Loperamide": 6,
            "Ranitidine": 5,
            "Famotidine": 7,
            "Omeprazole": 8,
            "Hydrogen Peroxide": 4,
            "Isopropyl Alcohol": 6,
            "Antibiotic Ointment": 8,
            "Adhesive Bandages": 3,
            "Amoxicillin": 10,
            "Azithromycin": 12,
            "Doxycycline": 11,
            "Ciprofloxacin": 13,
            "Vitamin C": 5,
            "Vitamin D": 7,
            "Vitamin B12": 6,
            "Calcium": 8,
            "Iron": 9,
            "Moisturizer": 10,
            "Sunscreen": 12,
            "Lip Balm": 6,
            "Hand Cream": 8,
            "Eye Drops": 7,
            "Contact Lens Solution": 8,
            "Eyelid Wipes": 5,
            "Eye Vitamins": 9
        }

        def on_configure(event):
            canvas.configure(scrollregion=canvas.bbox("all"))

        category_frame.bind("<Configure>", on_configure)

        for category, medicines in medicines.items():
            category_label = Label(category_frame, text=category, font=('times new roman', 12, 'bold'), bd=7,
                                   relief=GROOVE)
            category_label.pack(fill=X)

            medicine_frame = Frame(category_frame)
            medicine_frame.pack(fill=X)

            self.category_frames.append(category_frame)

            for medicine in medicines:
                image = PhotoImage(file=r"C:\Users\Avadhoot\Downloads\OIP.png")
                resized_image = image.subsample(4, 4)
                medicine_label = Label(medicine_frame, image=resized_image, text=medicine, compound='top')
                medicine_label.image = resized_image
                medicine_label.pack(side=LEFT, padx=10, pady=10)

                quantity_entry = Entry(medicine_frame, width=5, font=('times new roman', 10, 'bold'), bd=5,
                                       relief=SUNKEN)
                quantity_entry.pack(side=LEFT, padx=10, pady=10)
                self.quantity_entries.append(quantity_entry)

        btn_width = 10
        btn_font = 'arial 10 bold'
        pady_value = 8

        total_btn = Button(F6, command=self.total, text="Total", bg="cadetblue", fg="White", pady=pady_value,
                           width=btn_width, bd=2, font=btn_font)
        total_btn.place(x=735, y=20)

        Gen_btn = Button(F6, text="Generate Bill", command=self.bill_area, bg="cadetblue", fg="White", pady=pady_value,
                         width=btn_width, bd=2, font=btn_font)
        Gen_btn.place(x=855, y=20)

        Clear_btn = Button(F6, text="Save Bill", command=self.save_receipt_as_pdf, bg="cadetblue", fg="White", pady=pady_value,
                           width=btn_width, bd=2, font=btn_font)
        Clear_btn.place(x=975, y=20)

       # Email_btn = Button(F6, text="Email", command=self.send_email, bg="cadetblue", fg="White", pady=pady_value,width=btn_width, bd=2, font=btn_font)
        #Email_btn.place(x=855, y=20)

    def total(self):
        total_price = 0
        for i, quantity_entry in enumerate(self.quantity_entries):
            try:
                quantity = int(quantity_entry.get())
                medicine = list(self.medicine_prices.keys())[i]
                price_per_unit = self.medicine_prices.get(medicine, 0)
                total_price += quantity * price_per_unit
            except ValueError:
                pass

        self.medical_price.set(total_price)
        self.medical_tax.set(total_price * 0.05)  # Assuming 5% tax rate

    def bill_area(self):
        # Clear the bill area
        self.txtarea.delete('1.0', END)

        # Header of the bill
        self.txtarea.insert(END, "\t\tBilling Receipt\n")
        self.txtarea.insert(END, "=" * 42 + "\n")
        self.txtarea.insert(END, f"{'Medicine':<20}{'Quantity':<10}{'Price':<10}\n")

        total_price = 0

        # Iterate through quantity entries and calculate total price
        for i, quantity_entry in enumerate(self.quantity_entries):
            try:
                quantity = int(quantity_entry.get())
                medicine = list(self.medicine_prices.keys())[i]
                price_per_unit = self.medicine_prices.get(medicine, 0)
                total_price += quantity * price_per_unit
                self.txtarea.insert(END, f"{medicine:<20}{quantity:<10}{quantity * price_per_unit:<10}\n")
            except ValueError:
                pass

        # Display total price and tax
        self.txtarea.insert(END, "-" * 42 + "\n")
        self.txtarea.insert(END, f"{'Total':<20}{'':<10}{total_price:<10}\n")
        self.txtarea.insert(END, f"{'Tax (5%)':<20}{'':<10}{total_price * 0.05:<10}\n")
        self.txtarea.insert(END, "-" * 42 + "\n")
        self.txtarea.insert(END, f"{'Grand Total':<20}{'':<10}{total_price + total_price * 0.05:<10}\n")
        self.txtarea.insert(END, "=" * 42 + "\n")
        self.txtarea.insert(END, "Deliverd by : Symboisis Pharmacy, Thane\n")
        self.txtarea.insert(END, "Contact No. : 2098324324\n")

    def save_receipt_as_pdf(self):
        filename = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
        if filename:
            c = canvas.Canvas(filename, pagesize=letter)
            y = 750  # Starting y position for the text
            c.setFont("Helvetica-Bold", 16)
            c.drawString(100, y, "Billing Receipt")
            c.setFont("Helvetica", 12)
            y -= 30  # Move y position up
            c.drawString(100, y, "-" * 42)
            y -= 20  # Move y position up

            c.drawString(100, y, f"{'Medicine':<20}{'Quantity':<10}{'Price':<10}")
            y -= 20  # Move y position up
            c.drawString(100, y, "-" * 42)
            y -= 20  # Move y position up

            total_price = 0
            for i, quantity_entry in enumerate(self.quantity_entries):
                try:
                    quantity = int(quantity_entry.get())
                    medicine = list(self.medicine_prices.keys())[i]
                    price_per_unit = self.medicine_prices.get(medicine, 0)
                    total_price += quantity * price_per_unit
                    c.drawString(100, y, f"{medicine:<20}{quantity:<10}{quantity * price_per_unit:<10}")
                    y -= 20  # Move y position up
                except ValueError:
                    pass

            c.drawString(100, y, "-" * 42)
            y -= 20  # Move y position up
            c.drawString(100, y, f"{'Total':<20}{'':<10}{total_price:<10}")
            y -= 20  # Move y position up
            c.drawString(100, y, f"{'Tax (5%)':<20}{'':<10}{total_price * 0.05:<10}")
            y -= 20  # Move y position up
            c.drawString(100, y, "-" * 42)
            y -= 20  # Move y position up
            c.drawString(100, y, f"{'Grand Total':<20}{'':<10}{total_price + total_price * 0.05:<10}")
            y -= 20  # Move y position up
            c.drawString(100, y, "=" * 24)
            y -= 20  # Move y position up

            c.drawString(100, y, "Delivered by: Symboisis Pharmacy, Thane")
            y -= 20  # Move y position up
            c.drawString(100, y, "Contact No.: 2098324324")

            c.save()


root = Tk()
medicines = {
    "Pain Relief": ["Paracetamol", "Aspirin", "Ibuprofen", "Acetaminophen"],
    "Allergy": ["Cetirizine", "Loratadine", "Diphenhydramine", "Fexofenadine"],
    "Cold and Flu": ["Acetaminophen", "Pseudoephedrine", "Dextromethorphan", "Phenylephrine"],
    "Digestive Health": ["Loperamide", "Ranitidine", "Famotidine", "Omeprazole"],
    "First Aid": ["Hydrogen Peroxide", "Isopropyl Alcohol", "Antibiotic Ointment", "Adhesive Bandages"],
    "Antibiotics": ["Amoxicillin", "Azithromycin", "Doxycycline", "Ciprofloxacin"],
    "Vitamins": ["Vitamin C", "Vitamin D", "Vitamin B12", "Calcium", "Iron"],
    "Skin Care": ["Moisturizer", "Sunscreen", "Lip Balm", "Hand Cream"],
    "Eye Care": ["Eye Drops", "Contact Lens Solution", "Eyelid Wipes", "Eye Vitamins"]
}
obj = Medicines(root, medicines)
root.mainloop()
