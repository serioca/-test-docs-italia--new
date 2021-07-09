
fai un progetto nuovo uguale a test_doc_italia.
ci copi tutta la cartella del submodule test_doc_ingv_italia


i file importanti sono:

	Makefile
	conf.py
	document_settings-yaml
	logo.png
	requirements
	README.md
	
crea due sotto cartelle
	it
	en

ognuna con tutti gli .rst

con la ci oppure con un bash devi fare tutti i passaggi

il bash deve:

1)	copia tutti i file comuni dentro ie e en
2)	fai make html per ogni lingua
3) 	copia la _build/html in gitpages it e gitpages en
4)      dentro gitpages/ ci metti l'index.html con la redirect su it



nella progetto doc_italia_ing-themes...
modifica layouts/documents_action.html
la parte finale  utilizzando le variabili del blocco di codice da 43 a 48






