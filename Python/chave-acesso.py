import string

texto = "35-2408-21.494.615/0001-91-55-001-000.112.303-163.084.921-9"
texto = texto.replace("-","").replace(".","").replace("/","")
texto = list(texto)
