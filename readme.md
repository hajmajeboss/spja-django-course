# VYTVORENI NOVE APLIKACE
python manage.py startapp name

---

#PRIDANI MODELU
models.py - pridat tridy
po pridani modelu nutne provest migrace
    python manage.py makemigrations appname
    python manage.py sqlmigrate appname kod (0001_initial.py treba)
pak kdyz souhlasim s sql kodem, tak
    python manage.py migrate

---

#ZOBRAZENI DAT V DB
    python manage.py shell
v shellu:
    from stations.models import Company, Station
    Company.objects.all() - vypíše všechny companies v db

---

#PRIDAVANI DO DB
v shellu:
    c = Company(name="jmeno")
    s = Station(name="mesto", cars_capacity=4, company=Company.objects.get(id=1)

v adminu:
    python manage.py createsuperuser
    localhost/admin - prihlaseni do db
    otevrit admin.py a zaregistrovat modely
    tam jde pridavat do databaze - jednoduche

---

#SELECTY V DJANGU
v shellu:
    importovat modely
    k vyhledavani se daji pouzit dve fce:
        kdyz budu vracet jeden objekt:
        pri hledani pomoci primarniho klice - Station.objects.get(id=primarykey)
        kdyz budu vracet vice objektu:
        Station.objects.filter(id = 2) vraci seznam
        Station.objects.filter(cars_capacity__gt=3) -- @param gt - greater than, dve podtrzitka mezi cars__capacity a parametrem !!!
        Stations.objects.filter(cars_capacity__gte=3, name__contains='o') - vice parametu
        Stations.objects.filter(company__name__contains='s' - filtrovani podle ciziho klice


#TVORBA VIEWS
ve views.py vytvořit metodu s názvem view - je to celkem pochopitelné jen z kódu
pak pridat odkaz na view do urls.py, opět snadno pochopitelné z kódu, jak to udělat - (až na ty regulární výrazy -_-)

#TVORBA TEMPLATU
upravit soubor settings.py - v webstormu už to je udělané defaultně
jinak do seznamu dirs přidat 'templates' a vytvořit složku templates v rootu projektu
vytvorit ve slozce template html soubor, konstrukce jazyka se uvozuji {% for %}
vypis jedne promenne {{ promenna }}
ve views vytovrit view, pouzit fci render, viz komentar v views.py
pridat do urls'

#TVORBA ODKAZU
v urls.py přidat k urls keyword name, do něj string, jakou relativní adresu si přejeme
v html kodu templatu:
    url se uvozuje opet "{% url 'nazev', dalsi parametry do vstupuji do view metody %}"




