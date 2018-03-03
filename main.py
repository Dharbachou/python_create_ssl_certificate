from tkinter import *
from tkinter import messagebox
from OpenSSL import crypto
import os


KEY_FILE = "app.key"
CERT_FILE = "app.crt"

def create_self_signed_cert(cert_dir, varible_id , varible_county, varible_region, varible_city, varible_organization, varible_xNama):
    if not check_important(varible_organization) or not check_important(varible_xNama):
        block_info("error", "Not all line is field!!!")
        return

    k = crypto.PKey()
    k.generate_key(crypto.TYPE_RSA, 1024)

    cert = crypto.X509()
    cert.get_subject().C = varible_id 
    cert.get_subject().ST = varible_county   
    cert.get_subject().L = varible_region   
    cert.get_subject().O = varible_city  
    cert.get_subject().OU = varible_organization   
    cert.get_subject().CN = varible_xNama  
    cert.set_serial_number(1000)
    cert.gmtime_adj_notBefore(0)
    cert.gmtime_adj_notAfter(10*365*24*60*60) 
    cert.set_issuer(cert.get_subject())
    cert.set_pubkey(k)
    cert.sign(k, 'sha1')

    with open(os.path.join(cert_dir, CERT_FILE), "wb") as f:
        f.write(crypto.dump_certificate(crypto.FILETYPE_PEM, cert))

    with open(os.path.join(cert_dir, KEY_FILE), "wb") as f:
        f.write(crypto.dump_privatekey(crypto.FILETYPE_PEM, k))

    block_info("Ok", "certificate was create!!!")

def display_full_name():
    l_id = check_varible_id( id_country.get() )
    l_county = check_varible_county( country.get() )
    l_region = check_varible_region( region.get() )
    l_city = check_varible_city( city.get() )
    l_region = check_varible_region( region.get() )
    create_self_signed_cert('./', l_id , l_county, l_region, l_city, organization.get(), xNama.get())
   

def check_important(string_l):
    temp = FALSE
    if string_l.isalpha() and len(string_l) > 0:
        temp = TRUE
    return temp

def block_info(caption_l, text_l):
     messagebox.showinfo(caption_l, text_l)

def check_varible_id(varible_id):
    if varible_id.isalpha() and len(varible_id) > 0:
        return varible_id
    return "BY"

def check_varible_county(varible_id):
    if varible_id.isalpha() and len(varible_id) > 0:
        return varible_id
    return "Belarus"

def check_varible_region(varible_id):
    if varible_id.isalpha() and len(varible_id) > 0:
        return varible_id
    return "Minsk"

def check_varible_city(varible_id):
    if varible_id.isalpha() and len(varible_id) > 0:
        return varible_id
    return "Minsk"


root = Tk()
root.title("Certificate center")

id_country = StringVar()
country = StringVar()
region = StringVar()
city = StringVar()
organization = StringVar()
xNama = StringVar()


id_country_label = Label(text="Enter Id country:").grid(row=0, column=0, sticky="w")
country_label = Label(text="Enter country:").grid(row=1, column=0, sticky="w")
region_label = Label(text="Enter region:").grid(row=2, column=0, sticky="w")
city_label = Label(text="Enter city:").grid(row=3, column=0, sticky="w")
organization_label = Label(text="Enter organization:").grid(row=4, column=0, sticky="w")
xNama_label = Label(text="Enter xName:").grid(row=5, column=0, sticky="w")

id_country_entry = Entry(textvariable=id_country).grid(row=0, column=1, padx=5, pady=5)
country_entry = Entry(textvariable=country).grid(row=1, column=1, padx=5, pady=5)
region_entry = Entry(textvariable=region).grid(row=2, column=1, padx=5, pady=5)
city_entry = Entry(textvariable=city).grid(row=3, column=1, padx=5, pady=5)
organization_entry = Entry(textvariable=organization).grid(row=4, column=1, padx=5, pady=5)
xNama_entry = Entry(textvariable=xNama).grid(row=5, column=1, padx=5, pady=5)

message_button = Button(text="Generic certificate", command=display_full_name)
message_button.grid(row=6, column=1, padx=5, pady=5, sticky="e")

root.mainloop()
